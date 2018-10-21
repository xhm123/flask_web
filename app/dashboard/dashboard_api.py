# -*- coding: utf-8 -*-
'''
>file name:dashboard_api.py
>author:shakey
>create time :2018/10/18  3:00 PM
'''
from flask import Blueprint
from .dashboard import index

dashboard_manage=Blueprint('dashboard_manage',__name__)

dashboard_manage.add_url_rule('/',endpoint='index',view_func=index,methods=['POST','GET'])