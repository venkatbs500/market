from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/venky/Desktop/Market/market/market.db'
app.config['SECRET_KEY'] = '2391ea8fa7b17029d0a01a7f'
db = SQLAlchemy(app)

from market import routes