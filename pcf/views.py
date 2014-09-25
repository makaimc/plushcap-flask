from flask import request, render_template

from . import app

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')
