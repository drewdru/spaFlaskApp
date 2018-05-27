# coding=utf-8

from flask_cors import CORS
from flask import Flask, render_template
from .entities.views.exams import exams_page

# creating the Flask application
app = Flask(__name__)
app.config.from_pyfile('settings.py')

CORS(app) #TODO: configurate cors http://flask-cors.readthedocs.io/en/latest/#resource-specific-cors

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(exams_page)
