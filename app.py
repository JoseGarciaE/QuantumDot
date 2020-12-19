from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# current_Directory = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html')



if __name__ == '__main__':
    app.run(debug = True)