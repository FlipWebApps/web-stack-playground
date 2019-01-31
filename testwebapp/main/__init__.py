from flask import Blueprint

bp = Blueprint('main', __name__)

from testwebapp.main import routes
