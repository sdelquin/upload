# https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import settings
from lib import utils

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if not utils.allowed_file(file.filename):
            return render_template('status.html', error='Given filetype is not allowed')
        bucket = request.form['bucket']
        if not utils.check_bucket_password(request.form['password'], bucket):
            return render_template('status.html', error='Wrong password')

        filename = secure_filename(file.filename)
        name = secure_filename(request.form['name'].split()[0].lower())
        upload_filename = f'{name}_{filename}'
        upload_folder = settings.UPLOAD_BASE_FOLDER / bucket
        file.save(upload_folder / upload_filename)
        return render_template(
            'status.html', error=None, upload_filename=upload_filename, bucket=bucket
        )

    return render_template(
        'index.html',
        allowed_extensions=settings.ALLOWED_EXTENSIONS,
        buckets=settings.BUCKETS.keys(),
    )
