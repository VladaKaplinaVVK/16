import json
import datetime
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify, request

from models import *

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:////mybase.db"
app.config['SQLAlchemy_TRACK_MODIFICATTIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        result = []
        for user in User.query_all():
            result.append(user.to_dict())
        return jsonify(result)
    if request.method == 'POST':
        try:
            user = json.loads(request.text)
            result_user = User(
                id=user['id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                age=user['age'],
                email=user['email'],
                role=user['role'],
                phone=user['phone']
            )
            db.session.add(result_user)
            db.session.comit()
            db.session.close()
            return "Пользователь создан", 200
        except Exception as e:
            return e



@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        user = User.query.get(user_id)
        if user is None:
            return "Ничего не найдено"
        else:
            return jsonify(user.to_dict())
    elif request.method == 'PUT':
        user_text = json.loads(request.text)
        user = db.session.query(User).get(user_id)
        if user is None:
            return "Ничего не найдено"
        user = User.query.get(user_id)
        user.user_id = user_text['id']
        user.first_name = user_text['first_name'],
        user.last_name = user_text['last_name'],
        user.age = user_text['age'],
        user.email = user_text['email'],
        user.role = user_text['role'],
        user.phone = user_text['phone']
        db.session.add(user)
        db.session.comit()
        db.session.close()
        return f"Объект с id {user_id} успешно создан", 200
    elif request.method == 'DELETE':
        user = db.session.query(User).get(user_id)
        if user is None:
            return "Ничего не найдено"
        db.session.delete(user)
        db.session.comit()
        db.session.close()
        return f"Объект с id {user_id} успешно удален", 200



@app.route('/orders', methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        result = []
        for order in Order.query_all():
            result.append(order.to_dict())
        return jsonify(result)
    if request.method == 'POST':
        try:
            order = json.loads(request.text)
            month_start, day_start, year_start = [int(num) for num in order['start_date'].split("/")]
            month_end, day_end, year_end = [int(num) for num in order['end_date'].split("/")]
            result_order = Order(
                id=order['id'],
                name=order['name'],
                description=order['description'],
                start_date=datetime.text(year=year_start, month=month_start, day=day_start),
                end_date=datetime.text(year=year_end, month=month_end, day=day_end),
                address=order['address'],
                price=order['price'],
                customer_id=order['customer_id'],
                executor_id=order['executor_id']
            )
            db.session.add(result_order)
            db.session.comit()
            db.session.close()
            return "Предложение  создано", 200
        except Exception as e:
            return e


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def get_order(order_id):
    if request.method == 'GET':
        order = Order.query.get(order_id)
        if order is None:
            return "Ничего не найдено"
        else:
            return jsonify(order.to_dict())
    elif request.method == 'PUT':
        order_text = json.loads(request.text)
        order = db.session.query(Order).get(order_id)
        if order is None:
            return "Ничего не найдено"
        order = Order.query.get(order_id)
        month_start, day_start, year_start = [int(num) for num in order['start_date'].split("/")]
        month_end, day_end, year_end = [int(num) for num in order['end_date'].split("/")]
        order.order_id = order_text['id']
        order.name = order_text['name'],
        order.description = order_text['description'],
        order.start_date = datetime.text(year=year_start, month=month_start, day=day_start),
        order.end_date = datetime.text(year=year_end, month=month_end, day=day_end),
        order.address = order_text['address'],
        order.price = order_text['price'],
        order.customer_id = order_text['customer_id'],
        order.executor_id = order_text['executor_id']
        db.session.add(order)
        db.session.comit()
        db.session.close()
        return f"Объект с id {order_id} успешно создан", 200
    elif request.method == 'DELETE':
        order = db.session.query(Order).get(order_id)
        if order is None:
            return "Ничего не найдено"
        db.session.delete(order)
        db.session.comit()
        db.session.close()
        return f"Объект с id {order_id} успешно удален", 200


@app.route('/offers', methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        result = []
        for offer in Offer.query_all():
            result.append(offer.to_dict())
        return jsonify(result)
    if request.method == 'POST':
        try:
            offer = json.loads(request.text)
            result_offer = Offer(
                id=offer['id'],
                order_id=offer['order_id'],
                executor_id=offer['executor_id']
            )
            db.session.add(result_offer)
            db.session.comit()
            db.session.close()
            return "Пользователь создан", 200
        except Exception as e:
            return e


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer(offer_id):
    if request.method == 'GET':
        offer = Offer.query.get(offer_id)
        if offer is None:
            return "Ничего не найдено"
        else:
            return jsonify(offer.to_dict())
    elif request.method == 'PUT':
        offer_text = json.loads(request.text)
        offer = db.session.query(Offer).get(offer_id)
        if offer is None:
            return "Ничего не найдено"
        offer = User.query.get(offer_id)
        offer.offer_id = offer_text['id']
        offer.order_id = offer_text['order_id'],
        offer.executor_id = offer_text['executor_id'],

        db.session.add(offer)
        db.session.comit()
        db.session.close()
        return f"Объект с id {offer_id} успешно создан", 200
    elif request.method == 'DELETE':
        offer = db.session.query(Offer).query.get(offer_id)
        if offer is None:
            return "Ничего не найдено"
        db.session.delete(offer)
        db.session.comit()
        db.session.close()
        return f"Объект с id {offer_id} успешно удален", 200



if __name__ == '__main__':
    app.run()