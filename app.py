# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:20:45 2019

@author: DSC
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

