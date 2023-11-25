# # app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from models import db
from models import *
from views import bp
from flask_cors import CORS  # Import CORS
from main import *
from config import config
# app = Flask(__name__)
CORS(app)
# app.config.from_object(Config)
# # Initialize the database object
# db.init_app(app)

# app.register_blueprint(bp)


# # Create the database tables
# with app.app_context():
#     db.create_all()



# if __name__ == '__main__':
#     app.run()


def create_app():
    app.config.from_object(config)
    
    # Configure the Flask app to use the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.register_blueprint(bp)
    # Create the database tables
    with app.app_context():
        db.create_all()
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)