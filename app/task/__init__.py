from flask import Blueprint

bp = Blueprint('task', __name__, static_folder='static')

from app.task import routes
