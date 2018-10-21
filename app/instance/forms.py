# -*- coding: utf-8 -*-
'''
>file name:forms.py
>author:shakey
>create time :2018/10/18  3:45 PM
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired

class CreateInstanceForm(FlaskForm):
    image = StringField(u'Your image <name:tag>', validators=[DataRequired()])
    port = IntegerField(u'Your image port', validators=[DataRequired()])
    volumes = StringField(u'Your image volumes', validators=[DataRequired()])
    submit = SubmitField(u'create')

