from flask import Flask, render_template, g, request

def index():

    query = 'SELECT * FROM Articles'
    data = g.db.execute(query).fetchall()

    return render_template('index.html', data=data)