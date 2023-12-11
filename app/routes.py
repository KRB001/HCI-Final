from app import app, db
from flask import request, redirect, url_for, flash, render_template
from app.models import *
import datetime
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, CreateCharacterForm, BioGenerator, CreateCampaignForm
from app.ai_api import write_description


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Home', user=current_user)

@app.route('/characters')
@login_required
def characters():
    chars = current_user.players
    return render_template('characters.html', title='Your Characters',
                           user=current_user, characters=chars)

@app.route('/campaigns')
@login_required
def campaigns():
    camps = current_user.campaigns
    return render_template('campaigns.html', title='Your Campaigns',
                           user=current_user, campaigns=camps)

@app.route('/campaign/<campaign_id>')
@login_required
def campaign(campaign_id):
    camp = Campaign.query.filter_by(id=campaign_id).first()
    pass

@app.route('/create_bio/<char_id>', methods=['GET', 'POST'])
@login_required
def create_bio(char_id):
    character = Player.query.filter_by(id=int(char_id)).first()
    class_id = character.player_class
    race_id = character.player_race
    alignment_id = character.player_alignment
    char_class = PlayerClass.query.filter_by(id=int(class_id)).first()
    char_race = PlayerRace.query.filter_by(id=int(race_id)).first()
    char_alignment = PlayerAlignment.query.filter_by(id=int(alignment_id)).first()
    ai_inital_prompt = 'Create me a D&D character that is named {}, and is the gender of {}. They are a class of {}, race ' \
                       'of {}, and an alignment of {}'.format(character.name, character.gender, char_class.name,
                                                              char_race.name, char_alignment.name)
    form = BioGenerator()
    print("In the form")
    if form.validate_on_submit():
        print("submitted")
        if form.generate_bio.data:
            print(form.bio_prompt.data)
            ai_prompt = form.bio_prompt.data
            ai_feedback = write_description(ai_prompt)
            form.bio.data = ai_feedback
        elif form.submit_bio.data:
            print(form.bio.data)
            character.set_bio(form.bio.data)
            character.update()
            db.session.commit()
            return redirect("/updatechar/" + str(char_id))

    elif request.method == 'GET':
        form.bio_prompt.data = ai_inital_prompt
        print(form.bio_prompt.data)

    return render_template('generate_bio.html', char_id=char_id, form=form)

@app.route('/newchar')
@login_required
def new_char():
    found = False
    next = 1
    while found is False:
        if Player.query.filter_by(id=next).first() is None:
            found = True
            return redirect("/updatechar/" + str(next))
        next = next + 1

@app.route('/newcampaign', methods=['GET', 'POST'])
@login_required
def new_campaign():
    form = CreateCampaignForm()
    if form.validate_on_submit():
        campaign = Campaign(
            name=form.name.data, description=form.description.data, user_id=current_user.id
        )
        db.session.add(campaign)
        db.session.commit()
        flash("Created new campaign!")
        return redirect("/index")

    return render_template('create_campaign.html', title='Create Campaign', form=form, user=current_user)

@app.route('/updatechar/<char_id>', methods=['GET', 'POST'])
@login_required
def update_player(char_id):
    character = Player.query.filter_by(id=int(char_id)).first()
    form = CreateCharacterForm()
    form.player_race.choices = [(r.id, r.name) for r in PlayerRace.query.order_by('name')]
    form.player_class.choices = [(c.id, c.name) for c in PlayerClass.query.order_by('name')]
    form.player_alignment.choices = [(a.id, a.name) for a in PlayerAlignment.query.order_by('id')]
    form.campaign.choices = [(c.id, c.name) for c in Campaign.query.order_by('name')]

    if character is None:
        print("CHAR DOES NOT EXIST")
        form.level.data = 1
        form.xp.data = 0


        if form.validate_on_submit():
            character = Player(
                name=form.name.data, str=int(form.strength.data),
                dex=int(form.dexterity.data), con=int(form.constitution.data),
                int=int(form.intelligence.data), wis=int(form.wisdom.data),
                cha=int(form.charisma.data), level=int(form.level.data),
                xp=int(form.xp.data)
            )
            character.player_race = int(form.player_race.data)
            character.player_class = int(form.player_class.data)
            character.player_alignment = int(form.player_alignment.data)
            character.player_campaign = int(form.campaign.data)
            character.update()
            character.user_id = int(current_user.id)
            db.session.add(character)
            db.session.commit()
            flash("Character updated!")

    else:
        print("CHAR DOES EXIST")
        print(character)

        if form.submit_bio.data:
            print("asked to generate bio")
            print("Char id:", char_id)
            return redirect("/create_bio/" + str(char_id))

        if form.name.data == None:
            form.name.data = character.name
            form.gender.data = character.gender
            form.player_bio.data = character.bio
            form.strength.data = character.str
            form.dexterity.data = character.dex
            form.constitution.data = character.con
            form.intelligence.data = character.int
            form.wisdom.data = character.wis
            form.charisma.data = character.cha
            form.level.data = character.level
            form.xp.data = character.xp
            form.player_race.data = character.player_race
            form.player_class.data = character.player_class
            form.player_alignment.data = character.player_alignment
            form.campaign.data = character.player_campaign

        if form.validate_on_submit():
            character.set_name(form.name.data)
            character.set_gender(form.gender.data)
            character.set_bio(form.player_bio.data)
            character.set_str(form.strength.data)
            character.set_dex(form.dexterity.data)
            character.set_con(form.dexterity.data)
            character.set_int(form.intelligence.data)
            character.set_wis(form.wisdom.data)
            character.set_cha(form.charisma.data)
            character.set_level(form.level.data)
            character.set_xp(form.xp.data)
            character.set_race(form.player_race.data)
            character.set_class(form.player_class.data)
            character.set_alignment(form.player_alignment.data)
            character.set_campaign(form.campaign.data)

            character.update()
            db.session.commit()
            flash("Character updated!")

    return render_template('create_character.html', title='Edit Character', form=form, user=current_user)


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

    alignments = [
        PlayerAlignment(
            name="Lawful Good"
        ),
        PlayerAlignment(
            name="Neutral Good"
        ),
        PlayerAlignment(
            name="Chaotic Good"
        ),
        PlayerAlignment(
            name="Lawful Neutral"
        ),
        PlayerAlignment(
            name="True Neutral"
        ),
        PlayerAlignment(
            name="Chaotic Neutral"
        ),
        PlayerAlignment(
            name="Lawful Evil"
        ),
        PlayerAlignment(
            name="Neutral Evil"
        ),
        PlayerAlignment(
            name="Chaotic Evil"
        ),
    ]

    for player_alignment in alignments:
        db.session.add(player_alignment)

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
    return render_template('login.html', title='Sign In', form=form, user=current_user)


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
    return render_template('register.html', title='Register', form=form, user=current_user)
