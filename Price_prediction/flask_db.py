from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from appconfig import db, app
from flask_login import UserMixin


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bedrooms = db.Column(db.Float, unique=False, nullable=False)
    bathrooms = db.Column(db.Float, unique=False, nullable=False)
    sqft_living = db.Column(db.Integer, unique=False, nullable=False)
    sqft_lot = db.Column(db.Integer, unique=False, nullable=False)
    floors = db.Column(db.Float, unique=False, nullable=False)
    condition = db.Column(db.Integer, unique=False, nullable=False)
    sqft_above = db.Column(db.Integer, unique=False, nullable=False)
    sqft_basement = db.Column(db.Integer, unique=False, nullable=False)
    years_old = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.String(100), unique=False, nullable=False)
    prize = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class User2(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return f"{self.username} {self.email}"


def create_db(file_name):
    if not os.path.isfile(file_name):
        db.create_all()  
