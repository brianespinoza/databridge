from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_connection_string'
db = SQLAlchemy(app)
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Import and register your API routes here
from app import routes