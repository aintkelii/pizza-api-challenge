from app import app, db

def seed_data():
    from models.restaurant import Restaurant
    from models.pizza import Pizza
    from models.restaurant_pizza import RestaurantPizza
    
    with app.app_context():
        try:
            # Clear existing data
            db.drop_all()
            db.create_all()
            
            # Create restaurants
            restaurants = [
                Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue"),
                Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100"),
                Restaurant(name="Pizza Inn", address="TRM Drive Thru")
            ]
            db.session.add_all(restaurants)
            db.session.commit()
            
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
                RestaurantPizza(price=10, restaurant_id=restaurants[0].id, pizza_id=pizzas[0].id),
                RestaurantPizza(price=15, restaurant_id=restaurants[0].id, pizza_id=pizzas[1].id),
                RestaurantPizza(price=12, restaurant_id=restaurants[1].id, pizza_id=pizzas[2].id),
                RestaurantPizza(price=20, restaurant_id=restaurants[2].id, pizza_id=pizzas[0].id)
            ]
            db.session.add_all(restaurant_pizzas)
            db.session.commit()
            
            print("Database seeded successfully!")
            
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding database: {e}")
            raise

if __name__ == '__main__':
    seed_data()