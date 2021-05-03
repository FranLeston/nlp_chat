import src.database.build_db as db
import src.nlp_tools.nlp as nlp

import pandas as pd
conn = db.connect_to_mysql()


def get_messages():
    messages = pd.read_sql_query(
        f"""
            SELECT Chats.id, Chats.user_id, Chats.message, Chats.sentiment, Chats.created_at, Users.name, Users.sex,Users.age
            FROM Chats 
            left JOIN Users
            ON Chats.user_id = Users.id
            ORDER BY Chats.created_at DESC
              """, conn.execution_options(autocommit=True)
    )

    return messages


def create_message(message):
    user_id = message["user_id"]
    message = message["message"]

    # Before saving message to DB, lets Process it for NLP
    # Translate if it needs translation
    nlp_result = nlp.process_language(message)

    created_message = conn.execute(
        f'''
            INSERT INTO Chats (user_id, message, sentiment) VALUES
            ({user_id}, '{message}', {nlp_result})
            '''
    )

    chat_id = created_message.lastrowid

    the_message = pd.read_sql_query(
        f"""
              SELECT 
              *
              FROM
              Chats
              WHERE
              id = {chat_id}
              """, conn.execution_options(autocommit=True)
    )

    return the_message
