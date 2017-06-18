#encoding: utf-8

from exts import db
from werkzeug.security import generate_password_hash,check_password_hash
import shortuuid
import datetime

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(100),primary_key=True,default=shortuuid.uuid)
    username = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    _password = db.Column(db.String(100),nullable=False)

    def __init__(self,*args,**kwargs):
        password = kwargs.pop('password')
        username = kwargs.pop('username')
        telephone = kwargs.pop('telephone')
        self.password = password
        self.username = username
        self.telephone = telephone

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,rawpwd):
        self._password = generate_password_hash(rawpwd)

    def check_password(self,rawpwd):
        return check_password_hash(self._password,rawpwd)


class QuestionModel(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)
    author_id = db.Column(db.String(100),db.ForeignKey('users.id'))

    author = db.relationship('UserModel',backref='questions')

class AnswerModel(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)
    question_id = db.Column(db.Integer,db.ForeignKey('questions.id'))
    author_id = db.Column(db.String(100),db.ForeignKey('users.id'))

    question = db.relationship('QuestionModel',backref=db.backref('answers',order_by=create_time.desc()))
    author = db.relationship('UserModel',backref='answers')


