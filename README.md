# pizza-api-challenge
 Pizza Restaurant API
A RESTful API for managing pizza restaurants, pizzas, and their relationships. Built with Flask and SQLAlchemy following the MVC (Model-View-Controller) pattern.
 Table of Contents

Features
Project Structure
Setup Instructions
Database Migration & Seeding
API Routes
Validation Rules
Testing with Postman
Example Requests & Responses

 Features

Restaurant Management: Create, read, and delete restaurants
Pizza Catalog: View available pizzas with ingredients
Restaurant-Pizza Relationships: Associate pizzas with restaurants and set prices
Data Validation: Ensure data integrity with built-in validations
Cascading Deletes: Automatically clean up related data when restaurants are deleted

 Project Structure
.
├── server/
│   ├── __init__.py
│   ├── app.py                           # Flask app setup
│   ├── config.py                        # Database configuration
│   ├── models/                          #  Data models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/                     #  Route handlers (Controllers)
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py                          # Database seeding
├── migrations/                          # Database migrations
├── challenge-1-pizzas.postman_collection.json
└── README.md
 Setup Instructions
1. Clone the Repository
bashgit clone <your-repo-url>
cd pizza-api-challenge
2. Create and Activate Virtual Environment
bash# Using pipenv (recommended)
pipenv install flask flask-sqlalchemy flask-migrate
pipenv shell

# Or using venv
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask flask-sqlalchemy flask-migrate
3. Set Environment Variables
bashexport FLASK_APP=server/app.py
export FLASK_ENV=development
 Database Migration & Seeding
Initialize Database
bashflask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the Database
bashpython server/seed.py
This will create sample data:

3 restaurants (Dominion Pizza, Pizza Hut, Pizza Inn)
3 pizzas (Cheese, Pepperoni, Vegetarian)
4 restaurant-pizza relationships with prices

Start the Server
bashflask run
The API will be available at http://localhost:5000
🛠️ API Routes
MethodEndpointDescriptionGET/restaurantsGet all restaurantsGET/restaurants/<int:id>Get a specific restaurant with its pizzasDELETE/restaurants/<int:id>Delete a restaurant and its relationshipsGET/pizzasGet all pizzasPOST/restaurant_pizzasCreate a new restaurant-pizza relationship
 Validation Rules
RestaurantPizza

Price: Must be between 1 and 30 (inclusive)
Restaurant ID: Must reference an existing restaurant
Pizza ID: Must reference an existing pizza

 Testing with Postman
Import Collection

Open Postman
Click Import
Select challenge-1-pizzas.postman_collection.json
Click Import

Run Tests

Ensure your Flask server is running (flask run)
Execute each request in the collection
Verify responses match expected formats

 Example Requests & Responses
GET /restaurants
Request:
httpGET http://localhost:5000/restaurants
Response:
json[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
GET /restaurants/int:id
Request:
httpGET http://localhost:5000/restaurants/1
Success Response (200):
json{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
Error Response (404):
json{
  "error": "Restaurant not found"
}
DELETE /restaurants/int:id
Request:
httpDELETE http://localhost:5000/restaurants/1
Success Response:

Status: 204 No Content
Body: Empty

Error Response (404):
json{
  "error": "Restaurant not found"
}
GET /pizzas
Request:
httpGET http://localhost:5000/pizzas
Response:
json[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
POST /restaurant_pizzas
Request:
httpPOST http://localhost:5000/restaurant_pizzas
Content-Type: application/json

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
Success Response (201):
json{
  "id": 5,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
}
Validation Error Response (400):
json{
  "errors": ["Price must be between 1 and 30"]
}
 Models Overview
Restaurant

Attributes: id, name, address
Relationships: has many RestaurantPizzas
Cascade: Deleting a restaurant removes all its RestaurantPizza relationships

Pizza

Attributes: id, name, ingredients
Relationships: has many RestaurantPizzas

RestaurantPizza

Attributes: id, price, restaurant_id, pizza_id
Relationships: belongs to Restaurant and Pizza
Validations: price must be between 1 and 30

 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
 Troubleshooting
Common Issues

Import Error: Ensure you're in the correct directory and virtual environment is activated
Database Not Found: Run the migration commands in the correct order
Port Already in Use: Change the port with flask run --port 5001
Module Not Found: Check your FLASK_APP environment variable

Getting Help
If you encounter issues:

Check that all dependencies are installed
Verify your virtual environment is activated
Ensure the database migrations have been run
Check the Flask server logs for detailed error messages


Happy Coding! 