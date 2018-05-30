# coding=utf-8

from flask_cors import CORS
from flask import Flask, render_template
from entities.views.exams import exams_page

# creating the Flask application
app = Flask(__name__)
app.config.from_pyfile('settings.py')

CORS(app, resources={r"/api/*": {"origins": "*"}}) #TODO: configurate cors http://flask-cors.readthedocs.io/en/latest/#resource-specific-cors

@app.route('/api/')
def home():
    return render_template('home.html')

app.register_blueprint(exams_page, url_prefix='/api/')

if __name__ == '__main__':
    app.run()
