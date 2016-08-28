from flask import Flask, request
import json 
from pprint import pprint

app = Flask(__name__)

users = []

@app.route('/')
def hello():
    return "Hello World!"
    
@app.route("/users")
def list_users():
    global users
    return json.dumps(users)
    
@app.route("/users", methods=["POST"])
def create_user():
    global users

    user_data = request.get_json(force=True)
    users.append(user_data["name"])
    
    return json.dumps(user_data), 201

if __name__ == "__main__":
    app.run()
    