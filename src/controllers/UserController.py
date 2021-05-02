import src.database.build_db as db
import pandas as pd
conn = db.connect_to_mysql()


def get_all_users():
    try:

        users = pd.read_sql_query(
            f"""
                SELECT
                Users.id,
                Users.name,
                Users.sex,
                Users.age,
                AVG(IFNULL(Chats.sentiment, 0)) as mean
                FROM Users
                LEFT OUTER JOIN Chats
                ON Chats.user_id = Users.id
                GROUP BY Users.id
                """, conn.execution_options(autocommit=True)
        )

        return users
    except:
        # return empty DF
        return pd.DataFrame()


def get_user(user_id):
    # Check if name is in DB

    try:
        id = int(user_id)
        user = pd.read_sql_query(
            f"""
                SELECT
                *
                FROM
                Users
                WHERE
                id = {id}
                """, conn
        )
        return user
    except:
        # return empty DF
        return pd.DataFrame()


def create_user(user):
    name = user["name"]
    sex = user["sex"]
    age = user["age"]

    # Check if name is in DB
    name_exists = pd.read_sql_query(
        f"""
              SELECT
              name
              FROM
              Users
              WHERE
              name = '{name}'
              """, conn
    )

    if name_exists.empty:
        created_user = conn.execute(
            f'''
            INSERT INTO Users (name, sex, age, role) VALUES
            ('{name}', '{sex}', {age}, 0)
            '''
        )

        user_id = created_user.lastrowid

        user_db = pd.read_sql_query(
            f"""
                SELECT 
                *
                FROM
                Users
                WHERE
                id = {user_id}
                """, conn
        )

        return user_db
    else:
        return pd.DataFrame()
