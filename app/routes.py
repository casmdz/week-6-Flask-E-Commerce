from app import app
from flask import render_template, request, redirect, url_for
from .forms import PostForm, SearchForm
from .models import Post, Likes, User
from flask_login import current_user, login_required
import requests
import os

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

@app.route('/')
def homePage():
    
    return render_template('index.html', people = people, my_text = text )