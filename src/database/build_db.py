import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import requests
import os
import pymysql
import sys
import json


load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


def connect_to_mysql():
    #connectionData = f"mysql+pymysql://{db_user}:{db_password}@localhost/nlpchat"
    connectionData ="mysql://b87d1e8870618d:981537d6@eu-cdbr-west-01.cleardb.com/heroku_445b736ffbf8040?reconnect=true"
    try:

        engine = create_engine(connectionData, echo=False)
        engine.execution_options(isolation_level="AUTOCOMMIT")
        if not database_exists(engine.url):
            create_database(engine.url)

        print(database_exists(engine.url))
        print("Great..we have connected to the DB")
        conn = engine.connect()

        return conn
    except Exception as error:
        print("Oh no..could not connect to the DB. Exiting...")
        print(error)
        sys.exit()


def create_schemas(conn):
    # drop all tables and re create
    # Users Schema
    try:
        print("Creating Users tables...")
        #conn.execute('DROP TABLE IF EXISTS Chats;')
        #conn.execute('DROP TABLE IF EXISTS Users;')

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS Users(
            id int not null auto_increment primary key,
            name varchar(50) not null,
            sex varchar(50) not null,
            age int not null,
            role int DEFAULT 0,
            updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
            ENGINE=INNODB;
            '''
        )
        print("Finished!")
    except Exception as error:
        print("There was an error creating the Teams Table...exiting")
        print(error)
        sys.exit()

    # Chats Schema

    try:
        print("Creating Chats tables...")

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS Chats(
            id int not null auto_increment primary key,
            user_id int not null,
            message varchar(200) not null,
            sentiment float not null,
            FOREIGN KEY(user_id) REFERENCES Users(id),
            updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
            ENGINE=INNODB;
            '''
        )
        print("Finished!")
    except Exception as error:
        print("There was an error creating the Teams Table...exiting")
        print(error)
        sys.exit()
