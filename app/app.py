 
from flask import Flask,render_template,request
import os
static_dir = os.path.abspath('./static')
template_dir = os.path.abspath('./templates')
app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.environ['SECRECT_KEY']