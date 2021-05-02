from flask import Blueprint, request, Response, jsonify
import src.controllers.ChatController as ChatController
import json
import datetime
from flask_cors import CORS


ChatRoutes = Blueprint('ChatRoutes', __name__)
CORS(ChatRoutes)


@ChatRoutes.route('/api/chats', methods=["GET"])
def get_messages():
    messages = ChatController.get_messages()
    messages = messages.to_dict('records')
    js = json.dumps(messages, default=myconverter)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@ChatRoutes.route('/api/chats', methods=['POST'])
def create_message():
    message = request.get_json()
    created_message = ChatController.create_message(message)
    cm = created_message.to_dict('records')
    js = json.dumps(cm[0], default=myconverter)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
