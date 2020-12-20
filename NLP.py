from flask import Flask, render_template, g, request
import os

def handle_file_upload():
    file_name = request.form['input']

    uploaded_file = request.files['file']
    file_content = uploaded_file.stream.read()

    query = 'INSERT INTO Articles VALUES (?,?)'
    args = [file_name, file_content]
    g.db.execute(query, args)
    g.db.commit()

def get_Articles():
    return g.db.execute('SELECT * FROM Articles').fetchall()


def index():
    if request.method == 'POST':
        button = request.form['button']
        if button == 'file_upload':
            handle_file_upload()
    

    return render_template('index.html', articles=get_Articles())