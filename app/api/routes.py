from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, CarInventory, car_schema, cars_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'vroom': 'vroom'}

# @api.route('/data')
# def viewdata():
#     data = get_contact()
#     response = jsonify(data)
#     print(response)
#     return render_template('index.html', data = data)

@api.route('/inventory', methods = ['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    color = request.json['color']
    year = request.json['year']
    price = request.json['price']
    top_speed = request.json['top_speed']
    _range= request.json['_range']
    fast_charge = request.json['fast_charge']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    car_inventory = CarInventory(make, model, color, year, price, top_speed, _range, fast_charge, user_token = user_token )

    db.session.add(car_inventory)
    db.session.commit()

    response = car_schema.dump(car_inventory)
    return jsonify(response)

@api.route('/inventory', methods = ['GET'])
@token_required
def retrieve_single_car(current_user_token):
    a_car = current_user_token.token
    cars = CarInventory.query.filter_by(user_token = a_car).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

@api.route('/inventory/<id>', methods = ['GET'])
@token_required
def retrieve_all_cars(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        car_inventory = CarInventory.query.get(id)
        response = car_schema.dump(car_inventory)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401

# UPDATE endpoint
@api.route('/inventory/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car_inventory = CarInventory.query.get(id) 
    car_inventory.make = request.json['make']
    car_inventory.model = request.json['model']
    car_inventory.color = request.json['color']
    car_inventory.year = request.json['year']
    car_inventory.price = request.json['price']
    car_inventory.top_speed = request.json['top_speed']
    car_inventory._range = request.json['_range']
    car_inventory.fast_charge = request.json['fast_charge']
    car_inventory.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car_inventory)
    return jsonify(response)


# DELETE car ENDPOINT
@api.route('/inventory/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car_inventory = CarInventory.query.get(id)
    db.session.delete(car_inventory)
    db.session.commit()
    response = car_schema.dump(car_inventory)
    return jsonify(response)