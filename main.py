#!/usr/bin/env python3
from flask import Flask, jsonify
from flasgger import Swagger

DEBUG_SQL = True
USE_FLASK_TEMPLATES = True

if DEBUG_SQL:
    import logging
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

# Can be used for auth. Now it is used only to run all scripts in db directory
from db import db

# Creating Flask app object
app = Flask(__name__)
# ... and adding swagger support
swagger = Swagger(app)

# Flask Blueprints section. Register blueprints here!
from controller.lessons import lessons
app.register_blueprint(lessons)

# For development purposes, we can use flask to serve static files
# But you can turn this off and serve static with nginx for example
if USE_FLASK_TEMPLATES:
    from controller.static import static
    app.register_blueprint(static)

# To run on uwsgi: uwsgi --http 0.0.0.0:8000 --wsgi-file main.py --callable app --master

if __name__ == '__main__':
    app.run(debug=True)