#!/usr/bin/env python3
"""
Hay Day APK Patcher - Bypass official server check
Usage: python3 hayday_patcher.py official_hayday.apk
"""

import zipfile
import re
import sys
import base64

def patch_hayday_apk(apk_path, output_path):
    print("[+] Patching Hay Day APK for private server...")
    
    with zipfile.ZipFile(apk_path, 'r') as apk:
        files = apk.namelist()
        
        # Patch server URLs
        server_patches = {
            r'"https://[^"]*hayday\.com[^"]*"': '"http://YOUR_IP:5000"',
            r'serverUrl\s*:\s*["\'][^"\']*hayday[^"\']*["\']': 'serverUrl: "http://YOUR_IP:5000"',
            r'api\.hayday\.com': 'YOUR_IP:5000'
        }
        
        # Extract and patch smali files
        for file in files:
            if file.endswith('.smali'):
                content = apk.read(file).decode('utf-8')
                
                for pattern, replacement in server_patches.items():
                    content = re.sub(pattern, replacement, content)
                
                # Bypass SSL pinning
                content = re.sub(r'checkServerCertificate', 'const/4 v0, 0x1', content)
                content = re.sub(r'validateCertificate', 'return-void', content)
                
                # Unlimited resources flag
                content = content.replace('const/4 v0, 0x0', 'const/4 v0, 0x1')  # Enable cheats
                
                # Write patched file
                with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as patched:
                    for f in files:
                        if f == file:
                            patched.writestr(f, content.encode('utf-8'))
                        else:
                            patched.writestr(f, apk.read(f))
    
    print(f"[+] Patched APK saved: {output_path}")
    print("[+] Replace YOUR_IP with your server IP")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 hayday_patcher.py input.apk output_patched.apk")
        sys.exit(1)
    
    patch_hayday_apk(sys.argv[1], sys.argv[2])
