"""
Flask application factory
"""
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from config import Config
from app.database import db

# Load environment variables from .env file
load_dotenv()

login_manager = LoginManager()

def create_app(config_class=Config):
    """Create and configure the Flask application"""
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'
    
    # User loader for Flask-Login
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app