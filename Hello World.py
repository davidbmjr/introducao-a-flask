# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:22:40 2021

@author: DavidJr
"""

#pip install virtualenv
#virtualenv env
#1 .'\env\Scripts\activate.bat'  2 ".\\env\Scripts\activate.bat"  3 \\env\\Scripts\\activate.bat 4 \pathto\env\Scripts\activate 5 C:\Users\DavidJr\venv\Scripts\activate.bat 
#FINALLY 6 source '.\env\Scripts\activate'

#(env) pip install -r requirements.txt

#(env) python 'Hello World.py'
    
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World!"

if __name__== "__main__":
    app.run(debug=True)
