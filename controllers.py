import database as db
import datetime
import jwt
from flask import request

SECRET_KEY="aAsdi(?it1985mojJOy*&%$^12.k./khy"

def authenticate(username, password):
    res=db.getUser(username,password)
    return res


def createJWT(username, res):
    expiration = datetime.datetime.now() + datetime.timedelta(hours=1)  # 1 hour expiration
    payload = {
        'username': username,
        'name': res[1] ,
        'id': res[0],
        'exp': expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verifyCookie():
    token = request.cookies.get('jwt_token')
    if not token:
        return None
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    name = decoded_token['name']
    return name