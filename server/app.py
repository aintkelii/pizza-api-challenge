from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure the app directly
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    db.init_app(app)
    
    # Import and register blueprints/routes here
    # from routes import main_bp
    # app.register_blueprint(main_bp)
    
    return app

# Create the app instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)