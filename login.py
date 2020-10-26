# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:25:42 2020

@author: cesar
"""


from flask import Flask
app = Flask(__name__)

        
@app.route('/login', methods=['POST'])
def datos_registro():
    datos = request.get_json()
    name = datos.get('nombre')    
    password = datos.get('password')
