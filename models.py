# imports 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'New User {self.email}, is adding to the database'
    
class CarInventory (db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(50), nullable = False)
    model = db.Column(db.String(50))
    color = db.Column(db.String(20))
    year = db.Column(db.Integer)
    price = db.Column(db.String(20))
    top_speed = db.Column(db.String(50))
    _range = db.Column(db.String(50))
    fast_charge = db.Column(db.String(50))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, make, model, color, year, price, top_speed,_range, fast_charge, user_token, id = ''):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.top_speed = top_speed
        self._range = _range
        self.fast_charge = fast_charge
        self.user_token = user_token


    def __repr__(self):
        return f'The following vehicls has been added to the inventory: {self.color}, {self.year}, {self.make}, {self.model}'

    def set_id(self):
        return (secrets.token_urlsafe())

class CarInventorySchema(ma.Schema):
    class Meta:
        fields = ['id', 'make','model','color', 'year', 'price', 'top_speed', '_range', 'fast_charge']

car_schema = CarInventorySchema()
cars_schema = CarInventorySchema(many=True)