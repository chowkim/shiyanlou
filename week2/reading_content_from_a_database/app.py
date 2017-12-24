#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/article'
db = SQLAlchemy(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('files'))
    content = db.Column(db.Text) 
    created_time = db.Column(db.DateTime)
    
    def __init__(self, title, category, content, created_time=None):
        self.title = title
        self.category = category
        self.content = content
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time

    def __repr__(self):
        return '<Article_title %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>'% self.name
@app.route('/')
def index():
    files = File.query.all()
    print(files)
    return render_template('index.html', files=files)


@app.route('/files/<file_id>')
def file(file_id):
    title = File.query.filter_by(category_id=file_id).first()
    if file_id in ('5', '6'):
        return render_template('file.html', title=title)
    else:
        print('123')
        return render_template('404.html')
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=1)
