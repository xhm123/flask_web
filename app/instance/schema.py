# -*- coding: utf-8 -*-
'''
>file name:schema.py
>author:shakey
>create time :2018/10/19  11:09 AM
'''
from marshmallow import Schema, fields
class InstanceSchema(Schema):
    name = fields.String(required=True)
    short_id = fields.String(required=True)
    status = fields.String(required=True)
    created = fields.String(required=True)