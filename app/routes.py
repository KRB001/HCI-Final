from app import app, db
from flask import request, redirect, url_for, flash, render_template
from app.models import *
import datetime
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, CreateCharacterForm
#from app.ai_api import write_description

#@app.route('/')
#def main():
#    ai = write_description()
#    return render_template('main.html', ai = ai)


@app.route('/updateplayer/<player_id>', methods=['GET'])
@login_required
def update_player(player_id):
    pass

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


@app.route('/index')
def index():
    return ""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect((url_for('index')))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    now = datetime.datetime.now()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration complete!")
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
