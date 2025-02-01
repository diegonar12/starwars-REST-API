from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    eyecolor = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(50), nullable=True)
    mass = db.Column(db.String(50), nullable=True)
    hair_color = db.Column(db.String(50), nullable=True)
    birth_year = db.Column(db.String(50), nullable=True)
    homeworld = db.Column(db.String(120), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eyecolor": self.eyecolor,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "birth_year": self.birth_year,
            "homeworld": self.homeworld
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=True)
    population = db.Column(db.String(120), nullable=True)
    terrain = db.Column(db.String(120), nullable=True)
    orbital_period = db.Column(db.String(120), nullable=True)
    rotation_period = db.Column(db.String(120), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    favorite_type = db.Column(db.String(50), nullable=False)
    note = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean(), default=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
            "date_added": self.date_added,
            "updated_at": self.updated_at,
            "favorite_type": self.favorite_type,
            "note": self.note,
            "is_active": self.is_active
        }
