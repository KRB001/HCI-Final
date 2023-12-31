from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(256), unique=True)
    pw_hash = db.Column(db.String(128))

    players = db.relationship('Player', backref='user', lazy='dynamic')
    campaigns = db.relationship('Campaign', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(4096), unique=True)
    players = db.relationship('Player', backref='campaign', lazy='dynamic')


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(128), index=True)
    gender = db.Column(db.String(128), index=True)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    str = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)
    level = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    ac = db.Column(db.Integer)
    spd = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    hp_max = db.Column(db.Integer)
    insp = db.Column(db.Integer)
    bio = db.Column(db.String(4096))
    player_class = db.Column(db.Integer, db.ForeignKey('player_class.id'), nullable=False)
    player_race = db.Column(db.Integer, db.ForeignKey('player_race.id'), nullable=False)
    player_alignment = db.Column(db.Integer, db.ForeignKey('player_alignment.id'), nullable=False)
    player_campaign = db.Column(db.Integer, db.ForeignKey('campaign.id'))

    def __repr__(self):
        return '<Player {}'.format(self.name)

    def update(self):
        self.last_updated = datetime.utcnow()

    def set_user(self, user_id):
        self.user_id = user_id

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_bio(self, bio):
        self.bio = bio

    def set_campaign(self, campaign):
        self.player_campaign = campaign

    def set_alignment(self, alignment):
        self.player_alignment = alignment

    def set_str(self, strength):
        self.str = strength

    def set_dex(self, dex):
        self.dex = dex

    def set_con(self, con):
        self.con = con

    def set_int(self, intelligence):
        self.int = intelligence

    def set_wis(self, wis):
        self.wis = wis

    def set_cha(self, cha):
        self.cha = cha

    def set_level(self, level):
        self.level = level

    def set_xp(self, xp):
        self.xp = xp

    def set_race(self, race_id):
        self.player_race = race_id

    def set_class(self, class_id):
        self.player_class = class_id

    def level_check(self):
        # runs thru all levelup xp conditions, should bring player to the right level
        # depending on their xp (can be called at any time, but recommended to be called whenever updating xp)
        if self.level == 1 and self.xp >= 300:
            self.level = 2
            self.xp = self.xp - 300
        if self.level == 2 and self.xp >= 900:
            self.level = 3
            self.xp = self.xp - 900
        if self.level == 3 and self.xp >= 2700:
            self.level = 4
            self.xp = self.xp - 2700
        if self.level == 4 and self.xp >= 6500:
            self.level = 5
            self.xp = self.xp - 6500
        if self.level == 5 and self.xp >= 14000:
            self.level = 6
            self.xp = self.xp - 14000
        if self.level == 6 and self.xp >= 23000:
            self.level = 7
            self.xp = self.xp - 23000
        if self.level == 7 and self.xp >= 34000:
            self.level = 8
            self.xp = self.xp - 34000
        if self.level == 8 and self.xp >= 48000:
            self.level = 9
            self.xp = self.xp - 48000
        if self.level == 9 and self.xp >= 64000:
            self.level = 10
            self.xp = self.xp - 64000
        if self.level == 10 and self.xp >= 85000:
            self.level = 11
            self.xp = self.xp - 85000
        if self.level == 11 and self.xp >= 100000:
            self.level = 12
            self.xp = self.xp - 100000
        if self.level == 12 and self.xp >= 120000:
            self.level = 13
            self.xp = self.xp - 120000
        if self.level == 13 and self.xp >= 140000:
            self.level = 14
            self.xp = self.xp - 140000
        if self.level == 14 and self.xp >= 165000:
            self.level = 15
            self.xp = self.xp - 165000
        if self.level == 15 and self.xp >= 195000:
            self.level = 16
            self.xp = self.xp - 195000
        if self.level == 16 and self.xp >= 225000:
            self.level = 17
            self.xp = self.xp - 225000
        if self.level == 17 and self.xp >= 265000:
            self.level = 18
            self.xp = self.xp - 265000
        if self.level == 18 and self.xp >= 305000:
            self.level = 19
            self.xp = self.xp - 305000
        if self.level == 19 and self.xp >= 355000:
            self.level = 20
            self.xp = self.xp - 355000


class PlayerClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    hit_die = db.Column(db.Integer)
    players = db.relationship('Player', backref='class', lazy='dynamic')


class PlayerRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    players = db.relationship('Player', backref='race', lazy='dynamic')


class PlayerAlignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    players = db.relationship('Player', backref='alignment', lazy='dynamic')


class UserToPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
