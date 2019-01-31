from flask import Blueprint

bp = Blueprint('auth', __name__)

from testwebapp.auth import routes
