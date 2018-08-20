from flask import Flask, render_template, request, session, redirect, url_for
import os
from src.models.messages.message import Message
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')

app.secret_key = str(os.environ.get('SECRET_KEY'))


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def index():
    return render_template("index.jinja2")


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['sender_email']
        name = request.form['sender_name']
        content = request.form['message']
        newMsg = Message(name, email, content)
        newMsg.save_to_database()
    return render_template("index.jinja2")