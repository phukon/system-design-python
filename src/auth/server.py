import jwt, datetime, os
from dotenv import load_dotenv
from flask import Flask, request
from flask_mysqldb import MySQL

load_dotenv()

server = Flask(__name__)
mysql = MySQL(server)

# config
# config
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

# print(os.environ.get("MYSQL_HOST"))


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
