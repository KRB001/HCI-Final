from app import app
from flask import request
from dnd_character.classes import *


@app.route('/updateplayer/<player_id>-<name>-<level>', methods=['GET'])
def create_player(player_id, name, level):
    new_char = Barbarian(
        name="name",
        level=int(level)
    )

    return "New " + new_char.class_name + " " + new_char.name + " has been created with level " + new_char.level
