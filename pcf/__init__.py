from flask import Flask

app = Flask(__name__)
app.config.from_object('pcf.config')

from . import views
