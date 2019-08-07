# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:20:45 2019

@author: DSC
"""
from flask import Flask
hello = Flask(__name__)

@hello.route('/')
def home():
    return 'hello world'

if __name__=='__main__':
    hello.run()