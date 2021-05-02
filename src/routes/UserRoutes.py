from flask import Blueprint, request, Response, jsonify
import src.controllers.UserController as UserController
import json
import datetime
from flask_cors import CORS


UserRoutes = Blueprint('UserRoutes', __name__)
CORS(UserRoutes)


@UserRoutes.route('/api/users', methods=["GET"])
def get_all_users():
    users = UserController.get_all_users()

    if users.empty:
        msg = {'message': 'No Users Exist!'}
        js = json.dumps(msg)
        resp = Response(js, status=404, mimetype='application/json')
        return resp
    else:
        users = users.to_dict('records')
        js = json.dumps(users)
        resp = Response(js, status=201, mimetype='application/json')
        return resp


@UserRoutes.route('/api/users', methods=["POST"])
def create_user():
    user = request.get_json()
    created_user = UserController.create_user(user)

    if created_user.empty:
        msg = {'message': 'User already exists.'}
        js = json.dumps(msg)
        resp = Response(js, status=409, mimetype='application/json')
        return resp
    else:
        created_user = created_user.to_dict('records')
        js = json.dumps(created_user[0], default=myconverter)
        resp = Response(js, status=201, mimetype='application/json')
        return resp


@UserRoutes.route('/api/users/<id>', methods=["GET"])
def get_user(id):

    user = UserController.get_user(id)
    if not user.empty:
        user = user.to_dict('records')
        js = json.dumps(user[0], default=myconverter)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    else:
        msg = {'message': 'User does not exist.'}
        js = json.dumps(msg)
        resp = Response(js, status=404, mimetype='application/json')
        return resp


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
