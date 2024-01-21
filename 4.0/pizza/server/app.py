
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Pizza, Restaurant, RestaurantPizza
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

#restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

#pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    try:
        restaurant_pizza = RestaurantPizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify({'id': restaurant_pizza.pizza.id, 'name': restaurant_pizza.pizza.name, 'ingredients': restaurant_pizza.pizza.ingredients})
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555,debug=True)
