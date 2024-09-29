# create_db.py

from flask_blog import db, app  # Import the app and db instances
from flask_blog.models import User, Post  # Import the models to register them

with app.app_context():
    db.create_all()  
    print("Database tables created successfully.")
