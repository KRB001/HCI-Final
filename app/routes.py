from app import app
from flask import request


@app.route('/roll/<player_id>-<stat>-<mod>', methods=['GET'])
def roll(player_id, stat, mod):
    return "INPUT:\n Player ID: " + player_id + "\n Stat: " + stat + "\n Modifier: " + mod