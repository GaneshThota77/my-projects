# app.py
from flask import Flask
from views import api_bp
from config import Config
from models import db  # Import the db object

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_bp, url_prefix='/')

# Create the database tables
with app.app_context():
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


