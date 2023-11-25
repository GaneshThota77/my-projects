from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# class Config:
#     # Set the SQLAlchemy database URI
#     driver = 'ODBC Driver 17 for SQL Server'
#     server = 'LAPTOP-CMPHGTJN'
#     database = 'gpttables'

#     # Create the connection string
#     connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;CHARSET=UTF8"
#     database_uri = f"mssql+pyodbc:///?odbc_connect={connection_string}"

#     # SQLAlchemy configuration
#     SQLALCHEMY_DATABASE_URI = database_uri
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Set the SQLAlchemy database URI after initializing
    # app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
# Initialize the SQLAlchemy extension with the app
# db = SQLAlchemy()
# db.init_app(app)

class Config:

    driver = 'ODBC Driver 17 for SQL Server'
    server = 'LAPTOP-CMPHGTJN'
    database = 'gpttables'

    # Create the connection string
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;CHARSET=UTF8"
    database_uri = f"mssql+pyodbc:///?odbc_connect={connection_string}"

     # Disable track modifications

    # To be used in your app initialization
config = Config()



# Set up your OpenAI API key
YOUR_OPENAI_API_KEY = "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"