# -*- coding: utf-8 -*-
'''
>file name:dashboard.py
>author:shakey
>create time :2018/10/18  3:01 PM
'''
from flask import render_template,request

def index():
    return render_template('index.html')