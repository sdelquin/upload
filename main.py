# https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/

from pathlib import Path

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
            return render_template(
                'status.html', error='El tipo de fichero subido no está permitido'
            )
        context = request.form['context']
        if not utils.check_context_password(request.form['password'], context):
            return render_template('status.html', error='La contraseña es incorrecta')

        filename = Path(secure_filename(file.filename))
        name = secure_filename(request.form['name'].split()[0].lower())
        upload_filename = f'{filename.stem}_{name}{filename.suffix}'
        upload_folder = settings.UPLOAD_BASE_FOLDER / context
        file.save(upload_folder / upload_filename)
        return render_template(
            'status.html', error=None, upload_filename=upload_filename, context=context
        )

    return render_template(
        'index.html',
        allowed_extensions=settings.ALLOWED_EXTENSIONS,
        contexts=settings.CONTEXTS.keys(),
    )
