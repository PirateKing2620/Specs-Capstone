import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    lists = db.relationship("List", backref = "user", lazy = True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self,password):
        if self.password == password:
            return True
        else:
            return False


class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    ordered_list = db.Column(db.String(255), nullable = False)
    check_off = db.Column(db.Boolean, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)


class Bosses(db.Model):
    __tablename__ = "bosses"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    boss_name = db.Column(db.String(255), nullable = False)
    boss_description = db.Column(db.String(500), nullable = False)
    weapons = db.relationship("Weapons", backref = "boss", lazy = True)
    armors = db.relationship("Armor", backref = "boss", lazy = True)


class Weapons(db.Model):
    __tablename__ = "weapons"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    weapon_name = db.Column(db.String(255), nullable = False)
    bosses_id = db.Column(db.Integer, db.ForeignKey("bosses.id"), nullable = False)


class Armor(db.Model):
    __tablename__ = "armors"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    armor_name = db.Column(db.String(255), nullable = False)
    bosses_id = db.Column(db.Integer, db.ForeignKey("bosses.id"), nullable = False)




def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")