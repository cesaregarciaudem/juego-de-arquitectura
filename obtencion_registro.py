# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:32:17 2020

@author: cesar
"""

from flask import Flask
app = Flask(__name__)

        
@app.route('/register', methods=['POST'])
def datos_registro():
    datos = request.get_json()
    name = datos.get('nombre')    
    mail = datos.get('mail')
    password = datos.get('password')
    password2 = datos.get('password2')
    if password == password2:   
        return '<h1>OK</h1>'
    else:
        return '<h1>Error: passwords do not match</h1>'