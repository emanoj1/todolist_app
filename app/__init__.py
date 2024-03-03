from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import modules for Flask-login
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Set your secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/todo_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'  # Set the login view for Flask-Login
login_manager.init_app(app)

# Create a loader function for Flask-Login to load users:
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))    

# Import routes after initializing the app to avoid circular imports
from app import routes
