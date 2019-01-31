from flask import Blueprint

bp = Blueprint('errors', __name__)

from testwebapp.errors import handlers
