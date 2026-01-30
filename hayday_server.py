#!/usr/bin/env python3
"""
Hay Day Private Server - Pentest Edition
Features: Unlimited resources, speed hack, loot injection
Run: python3 hayday_server.py
"""

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import json
import threading
import time
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hayday-pentest-2026'
socketio = SocketIO(app, cors_allowed_origins="*")

# Unlimited resources database
players = {}
loot_multiplier = 1000  # x1000 loot injection

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', 'hacker')
    player_id = f"pentest_{int(time.time())}"
    
    player = {
        'id': player_id,
        'username': username,
        'coins': 999999999,
        'diamonds': 999999,
        'level': 100,
        'xp': 999999,
        'barn': {item: 999999 for item in ['wheat', 'corn', 'sugar', 'egg', 'milk']},
        'speed_multiplier': 0.01,  # 100x speed
        'loot_boost': loot_multiplier
    }
    
    players[player_id] = player
    return jsonify({
        'success': True,
        'player': player,
        'message': 'Pentest server login successful'
    })

@app.route('/api/resources/update', methods=['POST'])
def update_resources():
    player_id = request.json.get('player_id')
    if player_id in players:
        # Inject unlimited resources
        players[player_id]['coins'] += 1000000
        players[player_id]['diamonds'] += 10000
        
        # Loot multiplier injection
        for item in players[player_id]['barn']:
            players[player_id]['barn'][item] += 10000 * loot_multiplier
            
        return jsonify({'success': True, 'player': players[player_id]})
    
    return jsonify({'success': False}), 400

@app.route('/api/harvest', methods=['POST'])
def harvest():
    player_id = request.json.get('player_id')
    crop = request.json.get('crop', 'wheat')
    
    if player_id in players:
        amount = 10000 * loot_multiplier  # Massive loot injection
        players[player_id]['barn'][crop] += amount
        players[player_id]['coins'] += amount * 10
        
        return jsonify({
            'success': True,
            'harvested': amount,
            'new_balance': players[player_id]['barn'][crop]
        })
    
    return jsonify({'success': False}), 400

@app.route('/api/shipments/send', methods=['POST'])
def send_shipment():
    player_id = request.json.get('player_id')
    if player_id in players:
        reward = 50000 * loot_multiplier
        players[player_id]['coins'] += reward
        players[player_id]['diamonds'] += 100
        
        return jsonify({
            'success': True,
            'reward': reward,
            'instant_complete': True  # Bypass timer
        })
    
    return jsonify({'success': False}), 400

@socketio.on('connect')
def handle_connect():
    print('[+] Client connected to Hay Day pentest server')
    emit('server_status', {'message': 'Pentest server active - Unlimited resources enabled'})

@socketio.on('player_update')
def handle_player_update(data):
    player_id = data.get('player_id')
    if player_id in players:
        # Real-time loot injection
        emit('loot_injection', {
            'coins': 999999,
            'diamonds': 99999,
            'items': {item: 999999 for item in ['gold', 'diamond', 'boat_ticket']}
        }, room=request.sid)

def broadcast_loot():
    """Auto-inject loot every 10 seconds"""
    while True:
        socketio.emit('global_loot_event', {
            'type': 'mega_drop',
            'coins': 1000000 * loot_multiplier,
            'diamonds': 10000,
            'message': 'PENTEST: Unlimited loot injection active!'
        })
        time.sleep(10)

if __name__ == '__main__':
    # Start loot broadcaster
    threading.Thread(target=broadcast_loot, daemon=True).start()
    
    print("🚀 Hay Day Pentest Server Starting...")
    print("🌟 Unlimited coins/diamonds/loot enabled")
    print("⚡ 100x speed hack active")
    print("💎 Loot multiplier: x1000")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
