# -*- coding: utf-8 -*-
'''
>file name:__init__.py.py
>author:shakey
>create time :2018/10/18  2:08 PM
'''
from flask import Flask,render_template,g
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
def create_blueprint(flask_app):
    from app.instance.instance_api import instance_manage
    from app.dashboard.dashboard_api import dashboard_manage
    flask_app.register_blueprint(instance_manage)
    flask_app.register_blueprint(dashboard_manage)
def create_app():
    flask_app=Flask('psp-controller',static_folder='app.static')
    flask_app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    with flask_app.app_context():
        create_blueprint(flask_app)
    return flask_app

if __name__=="__main__":
    app = create_app()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run('0.0.0.0', 5000, debug=True)