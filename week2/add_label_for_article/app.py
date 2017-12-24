#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/article'
db = SQLAlchemy(app)
client = MongoClient('127.0.0.1', 27017)
db1 = client.article


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

    def add_tag(self, tag_name):
        file_tag = db1.files.find_one({'file_id': self.id})
        print(file_tag)
        if file_tag:
            tags = file_tag['tags']
            if tag_name not in tags:
                tags.append(tag_name)
                db1.files.update_one({'file_id': self.id}, {'$set': {'tags': tags}})
        else:
            tags=[tag_name]
            db1.files.insert_one({'file_id': self.id,'tags': tags})
        return  tags

    def remove_tag(self, tag_name):
        file_tag = db1.files.find_one({'file_id': self.id})
        if file_tag:
            tags = file_tag.get('tags')
            try:
                tags.remove(tag_name)
                new_tags = tags
            except ValueError:
                return tags
            db1.file.update_one({'file_id': self.id}, {'$set': {'tags': new_tags}})
            return new_tags
        return []

    @property
    def tags(self):
        file_tag = db1.files.find_one({'file_id': self.id})
        return file_tag['tags']

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    file = db.relationship('File')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>'% self.name

def insert():
        java = Category('Java')
        python = Category('Python')
        file1 = File('Hello Java', java, 'File Content - Java is cool!')
        file2 = File('Hello Python', python, 'File Content - Python is cool!')
        db.session.add(java)
        db.session.add(python)
        db.session.add(file1)
        db.session.add(file2)
        db.session.commit()
        file1.add_tag('tech')
        file1.add_tag('java')
        file1.add_tag('linux')
        file2.add_tag('tech')
        file2.add_tag('python')

db.create_all()
insert()

@app.route('/')
def index():
    files = File.query.all()
    return render_template('index.html', files=files)


@app.route('/files/<file_id>')
def file(file_id):
    file_id = File.query.get_or_404(file_id)
    return render_template('file.html', file_id=file_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=1)
