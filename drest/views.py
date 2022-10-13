from app import app
from flask import Blueprint

api_drest = Blueprint('drest',__name__)

@api_drest.route('/app',['GET','POST'])
def this_app():
    return 'drest is accepting conns'


@api_drest.route('/doc_diff',['POST'])
def doc_diff():
    pass    
