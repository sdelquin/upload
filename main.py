import os
from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import settings
from lib import models, utils

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    db = models.DBHandler()
    if request.method == 'POST':
        file = request.files['file']
        if not utils.allowed_file(file.filename):
            return render_template(
                'status.html', error='El tipo de fichero subido no está permitido'
            )
        context = db.get_context(context_name=request.form['context'])
        if request.form['password'] != context.password:
            return render_template('status.html', error='La contraseña es incorrecta')

        filename = Path(secure_filename(file.filename))
        name = secure_filename(request.form['name'].split()[0].lower())
        upload_filename = f'{filename.stem}-{name}{filename.suffix}'
        file.save(os.path.join(context.folder, upload_filename))
        return render_template(
            'status.html', error=None, upload_filename=upload_filename, context=context
        )

    return render_template(
        'index.html',
        allowed_extensions=settings.ALLOWED_EXTENSIONS,
        contexts=db.get_contexts(),
    )
