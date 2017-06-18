#encoding: utf-8

import wtforms
from wtforms import validators

class RegistForm(wtforms.Form):
    telephone = wtforms.StringField(validators=[validators.length(min=11,max=11)])
    username = wtforms.StringField(validators=[validators.InputRequired(message=u'请输入用户名')])
    password1 = wtforms.StringField(validators=[validators.InputRequired()])
    password2 = wtforms.StringField(validators=[validators.InputRequired(),validators.EqualTo('password1')])

