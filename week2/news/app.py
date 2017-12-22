#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    content_title = []
    path = '/home/shiyanlou/files/'
    dirs = os.listdir(path)
    for file in dirs:
        file_path = os.path.join(path,file)
        with open(file_path, 'r') as f:
            content = json.loads(f.read())
            content_title.append(content)
    return render_template('index.html', content_title=content_title)


@app.route('/files/<filename>')
def file(filename):
    if filename not in ('helloshiyanlou', 'helloworld'):
        print(filename)
        print(type(filename))
        #abort(404)
        return render_template('404.html')
    else:
        filename += '.json'
        print(filename)
        path = '/home/shiyanlou/files/'
        file_path = os.path.join(path, filename)
        with open(file_path, 'r') as f:
            article_content = json.loads(f.read())
        return render_template('file.html', article_content=article_content)
    
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=1)
