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

load_dotenv()

# My functions
app = Flask(__name__)
#app = Flask(__name__, static_folder='client/dist/', static_url_path='/')
app.config.from_object(__name__) 


conn = db.connect_to_mysql()
if conn:
    db.create_schemas(conn)



# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

app.register_blueprint(UserRoutes)
app.register_blueprint(ChatRoutes)

port = int(os.environ.get("PORT", 5000))
#app.run(host='0.0.0.0', port=port,threaded=True)
app.run()