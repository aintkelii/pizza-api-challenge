from app import create_app,db
# from . import db
from models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza
def seed_data():
    app = create_app()
    with app.app_context():
        # Clear existing data
        # db.drop_all()
        db.create_all()
        
        # Create restaurants
        restaurants = [
            Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue"),
            Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100"),
            Restaurant(name="Pizza Inn", address="TRM Drive Thru")
        ]
        db.session.add_all(restaurants)
        
        # Create pizzas
        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Vegetables")
        ]
        db.session.add_all(pizzas)
        
        db.session.commit()
        
        # Create restaurant_pizzas
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=12, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=20, restaurant_id=3, pizza_id=1)
        ]
        db.session.add_all(restaurant_pizzas)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()