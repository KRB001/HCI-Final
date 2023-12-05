from app import app
from flask import request


@app.route('/updateplayer/<player_id>-<name>-<level>', methods=['GET'])
def create_player(player_id, name, level):

    return ""


@app.route('/login', methods=['GET', 'POST'])
def login():
    return ""