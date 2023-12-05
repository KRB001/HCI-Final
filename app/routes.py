from app import app
from flask import request
from app.models import *


@app.route('/updateplayer/<player_id>-<name>-<level>', methods=['GET'])
def create_player(player_id, name, level):

    return ""

@app.route("/resetdb", methods=['GET'])
def reset_db():

    clear_db()
    print("Cleared DB")

    classes = [
        PlayerClass(
            name="Barbarian",
            hit_die=12
        ),
        PlayerClass(
            name="Bard",
            hit_die=8
        ),
        PlayerClass(
            name="Cleric",
            hit_die=8
        ),
        PlayerClass(
            name="Druid",
            hit_die=8
        ),
        PlayerClass(
            name="Fighter",
            hit_die=10
        ),
        PlayerClass(
            name="Monk",
            hit_die=8
        ),
        PlayerClass(
            name="Paladin",
            hit_die=10
        ),
        PlayerClass(
            name="Ranger",
            hit_die=10
        ),
        PlayerClass(
            name="Rogue",
            hit_die=8
        ),
        PlayerClass(
            name="Sorcerer",
            hit_die=6
        ),
        PlayerClass(
            name="Warlock",
            hit_die=8
        ),
        PlayerClass(
            name="Wizard",
            hit_die=6
        ),
        PlayerClass(
            name="Artificer",
            hit_die=8
        ),
        PlayerClass(
            name="Blood Hunter",
            hit_die=10
        ),
    ]

    for player_class in classes:
        db.session.add(player_class)

    db.session.commit()

    races = [
        PlayerRace(
            name="Dragonborn"
        ),
        PlayerRace(
            name="Dwarf"
        ),
        PlayerRace(
            name="Elf"
        ),
        PlayerRace(
            name="Gnome"
        ),
        PlayerRace(
            name="Half-Elf"
        ),
        PlayerRace(
            name="Halfling"
        ),
        PlayerRace(
            name="Half-Orc"
        ),
        PlayerRace(
            name="Human"
        ),
        PlayerRace(
            name="Tiefling"
        ),
        PlayerRace(
            name="Aarakocra"
        ),
        PlayerRace(
            name="Aasimar"
        ),
        PlayerRace(
            name="Air Genasi"
        ),
        PlayerRace(
            name="Bugbear"
        ),
        PlayerRace(
            name="Centaur"
        ),
        PlayerRace(
            name="Changeling"
        ),
        PlayerRace(
            name="Deep Gnome"
        ),
        PlayerRace(
            name="Duergar"
        ),
        PlayerRace(
            name="Earth Genasi"
        ),
        PlayerRace(
            name="Eladrin"
        ),
        PlayerRace(
            name="Fairy"
        ),
        PlayerRace(
            name="Firbolg"
        ),
        PlayerRace(
            name="Fire Genasi"
        ),
        PlayerRace(
            name="Githyanki"
        ),
        PlayerRace(
            name="Githzerai"
        ),
        PlayerRace(
            name="Goblin"
        ),
        PlayerRace(
            name="Goliath"
        ),
        PlayerRace(
            name="Harengon"
        ),
        PlayerRace(
            name="Hobgoblin"
        ),
        PlayerRace(
            name="Kenku"
        ),
        PlayerRace(
            name="Kobold"
        ),
        PlayerRace(
            name="Lizardfolk"
        ),
        PlayerRace(
            name="Minotaur"
        ),
        PlayerRace(
            name="Orc"
        ),
        PlayerRace(
            name="Satyr"
        ),
        PlayerRace(
            name="Sea Elf"
        ),
        PlayerRace(
            name="Shadar-kai"
        ),
        PlayerRace(
            name="Shifter"
        ),
        PlayerRace(
            name="Tabaxi"
        ),
        PlayerRace(
            name="Tortle"
        ),
        PlayerRace(
            name="Triton"
        ),
        PlayerRace(
            name="Water Genasi"
        ),
        PlayerRace(
            name="Yuan-ti"
        ),
        PlayerRace(
            name="Kender"
        ),
        PlayerRace(
            name="Astral Elf"
        ),
        PlayerRace(
            name="Autognome"
        ),
        PlayerRace(
            name="Giff"
        ),
        PlayerRace(
            name="Hadozee"
        ),
        PlayerRace(
            name="Plasmoid"
        ),
        PlayerRace(
            name="Thri-kreen"
        ),
        PlayerRace(
            name="Owlin"
        ),
        PlayerRace(
            name="Leonin"
        ),
        PlayerRace(
            name="Satyr"
        ),
        PlayerRace(
            name="Changeling"
        ),
        PlayerRace(
            name="Kalashtar"
        ),
        PlayerRace(
            name="Warforged"
        ),
        PlayerRace(
            name="Verdan"
        ),
        PlayerRace(
            name="Loxodon"
        ),
        PlayerRace(
            name="Simic Hybrid"
        ),
        PlayerRace(
            name="Vedalken"
        ),
        PlayerRace(
            name="Feral Tiefling"
        ),
        PlayerRace(
            name="Locathah"
        ),
        PlayerRace(
            name="Grung"
        )
    ]

    for player_race in races:
        db.session.add(player_race)

    db.session.commit()

    print("DB has been reset")
    return "DB HAS BEEN RESET"


def clear_db():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()