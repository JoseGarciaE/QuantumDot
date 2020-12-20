# Libraries
from flask import Flask, render_template, g, request
import sqlite3

# Files
import NLP


app = Flask(__name__)

#Routes
app.add_url_rule('/', view_func=NLP.index)


# Database setup
@app.before_request
def before_request():
    g.db = sqlite3.connect('./data/data.sqlite')
    g.db.row_factory = sqlite3.Row

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


if __name__ == '__main__':
    app.run(debug = True)