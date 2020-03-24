#!/usr/bin/env python3
from flask import Flask, jsonify
from flasgger import Swagger

# Can be used for auth. Now it is used only to run all scripts in db directory
from db import db

# Creating Flask app object
app = Flask(__name__)
# ... and adding swagger support
swagger = Swagger(app)

# Flask Blueprints section. Register blueprints here!
from controller.lessons import lessons
app.register_blueprint(lessons)

# To run on uwsgi: uwsgi --http 0.0.0.0:8000 --wsgi-file main.py --callable app --master

if __name__ == '__main__':
    app.run(debug=True)