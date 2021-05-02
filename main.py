from src.routes.ChatRoutes import ChatRoutes
from src.routes.UserRoutes import UserRoutes
import src.database.build_db as db
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import requests
import os
import pymysql
import sys
import json
from flask import Flask, request, jsonify
from flask_cors import CORS


# My functions

if __name__ == '__main__':
    conn = db.connect_to_mysql()
    if conn:
        db.create_schemas(conn)

    app = Flask(__name__)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.register_blueprint(UserRoutes)
    app.register_blueprint(ChatRoutes)


    app.run("0.0.0.0", 5000, debug=True)
