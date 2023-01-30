from app import app
from flask import render_template, request, redirect, url_for, flash, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/home')
def homePage():
    return render_template("index.html")