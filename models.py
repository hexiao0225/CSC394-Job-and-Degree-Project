"""


Database Schema

Creates the tables for the database and abstraction layer for
Python use


"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app

#Database Connection instance
db = SQLAlchemy(app)


#keyword table
class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False)

    #Name representation for python
    def __repr__(self):
        return '<Keyword %r>' % self.key

#job table
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)

    #Name representation for python
    def __repr__(self):
        return '<Job %r>' % self.title

#degree table
class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)

    #Name representation for python
    def __repr__(Self):
        return '<Degree %r>' % self.title

# Reference -> http://flask-sqlalchemy.pocoo.org/2.3/models/
#The job to keyword relationship table
class JobKeywords(db.Model):
    keywordID = db.Column(db.Integer, db.ForeignKey('keyword.id'), primary_key=True)
    jobID = db.Column(db.Integer, db.ForeignKey('job.id'), primary_key=True)

#the degree to keyword relationship table
class DegreeKeywords(db.Model):
    keywordID = db.Column(db.Integer, db.ForeignKey('keyword.id'), primary_key=True)
    degreeID = db.Column(db.Integer, db.ForeignKey('degree.id'), primary_key=True)

class KeywordAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionID = db.Column(db.Integer, db.ForeignKey('keyword_question.id'))
    answer = db.Column(db.Text)
    correct = db.Column(db.Boolean, default=False)

class KeywordQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keywordID = db.Column(db.Integer, db.ForeignKey('keyword.id'))
    question = db.Column(db.Text)
