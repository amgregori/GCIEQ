from . import main_bp
from flask import render_template, redirect, url_for

@main_bp.route('/')
def index():
    return render_template('main/index.html')
   