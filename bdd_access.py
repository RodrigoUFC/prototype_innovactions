from marshmallow import ValidationError
from models import *
from config import db
from datetime import datetime
import hashlib


def save_user(user_data):
    new_user = {
        'last_name': user_data.last_name,
        'first_name': user_data.first_name,
        'pass_word': hashlib.sha256(str(user_data.password).encode('utf-8')).hexdigest(),
        'email': user_data.email
    }
    schema = UsersSchema()
    new_data = schema.load(new_user, session=db.session)
    # Add the data to the database
    db.session.add(new_data)
    db.session.commit()


def load_user(email, password_in):
    new_user = Users()
    data = UsersModel.query.order_by(
        UsersModel.email.desc()).filter(UsersModel.email == email).first()  #
    if data is None:
        print("User not found")
    elif data.pass_word == hashlib.sha256(str(password_in).encode('utf-8')).hexdigest():
        new_user.last_name = data.last_name
        new_user.first_name = data.first_name
        new_user.email = data.email
        new_user.password = password_in
    else:
        print("Wrong password")
    return new_user


def save_code(user, code_data):
    new_code = {
        'user_email': user.email,
        'qr_code': code_data.qr_code,
        'expires_on': code_data.expires_on
    }
    schema = CodesSchema()
    new_data = schema.load(new_code, session=db.session)
    # Add the data to the database
    db.session.add(new_data)
    db.session.commit()


Users.first_name = "Niels"
Users.last_name = "Bohr"
Users.password = "nx-01ENT"
password = "nx-01ENT"
Users.email = "connect@france.fr"


try:
    #save_user(Users)
    #load_user(Users.email, Users.password)
    Codes.qr_code = "www.findit.fr/object#73613?push_greeting"
    print(datetime.now().replace(year=datetime.now().year + 5).strftime("%Y-%m-%d %H:%M"))
    Codes.expires_on = datetime.now().replace(year=datetime.now().year + 5).strftime("%Y-%m-%d %H:%M")
    save_code(load_user(Users.email, Users.password), Codes)
    print(Users.last_name)
except ValidationError as err:
    errors = err.messages
    valid_data = err.valid_data
    print(errors)
    print(valid_data)
