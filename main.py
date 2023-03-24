# https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
import os

from flask import Flask, flash, redirect, render_template, request
from werkzeug.utils import secure_filename

import settings

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = settings.UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in settings.ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        name = request.form['name']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            name = secure_filename(name.split()[0].lower())
            filename = f'{name}_{filename}'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('status.html', filename=filename)
    return render_template('index.html')
