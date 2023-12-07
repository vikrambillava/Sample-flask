from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)




class Account_Customer(db.Model):
    Config - UID = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(80))
    email_id = db.Column(db.String(255),unique=True)
    Male =db.Column(db.String(80))
    registration_date=db.Column(db.datetime())
    Age=db.Column(db.Integer())
    city=db.Column(db.String(80))
    birthday=db.Column(db.datetime())
    phone_no=db.Column(db.Integer(10))
    primary_address=db.Column(db.String(255))


class Activity_Customer(db.Model):
    UID = db.Column(db.Integer, primary_key=True)
    productID =db.Column(db.Integer)
    add_to_cart =db.Column(db.Boolean, default=False, nullable=False)
    Time Series - Timestamp=db.Column(db.TIMESTAMP, default=False)
    order_placed=db.Column(db.Boolean, default=False, nullable=False)
    

class Inventory(db.Model):
    productID = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    warehouse =db.Column(db.String(255))
    sellerID =db.Column(db.String(255))


class Role_Mapping(db.Model):
    user = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(255))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)