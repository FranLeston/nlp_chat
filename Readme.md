# NLP Chat Flask Server

![alt text](https://media-exp1.licdn.com/dms/image/C5112AQHCHW6AdtPdHw/article-cover_image-shrink_720_1280/0/1523069318051?e=1625702400&v=beta&t=y97tMi0GpvYUPPKluVDYWJhGkIh2pwigxa06g9a9pks)

## About

This project consists of a Python Flask API using MySQL. The endpoints will allow you to create a user, then once created, let you post chat messages to
the api. Before the chat message is stored in the DB, it is ran through the NLPTK library. The natural language processing algorithm will assign a value of -1 to 1
to the message. -1 being the most Negative sentiment, 0 is Neutral, and 1 being the most positive.

In this repo, there is also a jupiter notebook in which you may execute the requests in real-time to get an overall analysis of the chat.

## Installation

To get the server up and running you must first pip install the libraries in the requirements.txt and have a valid MYSQL DB_URL in a .env file.
Afterwards, you may run Python3 main.py and the server should spin up on localhost.

A current build is hosted on Heroku with VueJs in which you and others can participate in the chat in real-time.

The Heroku URL is: https://ironhack-nlp-client.herokuapp.com/

The repo for my VueJS Client is: https://github.com/FranLeston/nlp_chat_client

## API ENDPOINTS

CREATE USER -- POST https://ironhack-nlp.herokuapp.com/api/users
{
"name": "Emilio",
"sex": "M",
"age": 23,
"role": 0
}

GET ALL USERS -- GET https://ironhack-nlp.herokuapp.com/api/users

GET USER BY ID -- GET https://ironhack-nlp.herokuapp.com/api/users/125

GET ALL MESSAGES -- GET https://ironhack-nlp.herokuapp.com/api/chats

CREATE MESSAGE -- POST https://ironhack-nlp.herokuapp.com/api/chats
{
"user_id": 12,
"message": "A chat message"
}

## Here is a schema of the simple db setup

![alt text](https://github.com/FranLeston/nlp_chat/blob/master/notebooks/images/dbSchema.png?raw=true)

## Finally, here is an example of a KDE chart inside notebooks/chatAnalisys.ipynb

![alt text](https://github.com/FranLeston/nlp_chat/blob/master/notebooks/images/sentikde.png?raw=true)
