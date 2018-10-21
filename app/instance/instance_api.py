# -*- coding: utf-8 -*-
'''
>file name:instance_api.py
>author:shakey
>create time :2018/10/18  2:10 PM
'''
from flask import Blueprint
from .instance import create_instace,list_instance,restart_instance,stop_instance
instance_manage=Blueprint('isinstance_manage',__name__)

instance_manage.add_url_rule(rule='/v1/instance',endpoint='create_instance',view_func=create_instace,methods=['GET','POST'])
instance_manage.add_url_rule(rule='/v1/instance_list',endpoint='list_instance',view_func=list_instance,methods=['GET'])

instance_manage.add_url_rule(rule='/v1/restart_instance',endpoint='restart_instance',view_func=restart_instance,methods=['GET'])
instance_manage.add_url_rule(rule='/v1/stop_instance/<instance_id>',endpoint='stop_instance',view_func=stop_instance,methods=['GET','POST'])