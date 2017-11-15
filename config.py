"""
App configuration variables

Temp DB Credentials
User => kzffhwvbxkqwdx
Port => 5432
Password => aa9ce97f6dc72871206b5a8d92805f311f73aac71d604f4402d7ddf97b735046
"""

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kzffhwvbxkqwdx:aa9ce97f6dc72871206b5a8d92805f311f73aac71d604f4402d7ddf97b735046@ec2-50-17-203-195.compute-1.amazonaws.com:5432/d2d0gj6oiffiu2'
app.config['DEBUG'] = False

app.config['EMAIL'] = ""
app.config['EMAIL_PASSWORD'] = ""
