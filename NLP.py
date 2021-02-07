from flask import Flask, render_template, g, request
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = './data/uploads'

def handle_file_upload():
    uploaded_file = request.files['file']
    article_name = request.form['input']

    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], article_name))

    file_content = uploaded_file.stream.read()

    
    g.db.execute('INSERT INTO Articles VALUES (?,?)', [article_name, file_content])
    g.db.commit()

def get_Articles():
    return g.db.execute('SELECT * FROM Articles').fetchall()

def get_Article(name):
    return g.db.execute('SELECT * FROM Articles WHERE Name = ?', [name]).fetchone()

def delete_Article(name):
    os.remove(os.path.join(app.config['UPLOAD_PATH'], name))

    g.db.execute('DELETE FROM Articles WHERE Name = ?', [name])
    g.db.commit()    

def index():
    if request.method == 'POST':
        if request.form['button'] == 'file_upload':
            handle_file_upload()
        if request.form['button'] == 'view_article':
            return render_template('view.html', article=get_Article(request.form.get('select_article')))
        if request.form['button'] == 'delete_article':
            delete_Article(request.form.get('select_article'))
        

        return render_template('refresh.html')
    
    else:  
        return render_template('index.html', articles=get_Articles())