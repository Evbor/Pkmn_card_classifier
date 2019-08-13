import os
import sys
import json
import base64
from io import BytesIO
from keras.preprocessing import image
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/dev/Desktop/'
IMG_SIZE = (550, 400)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/base_set_classifier/predict/', methods=['POST'])
def base_set_classifier():
    for sample in request.form.getlist('samples'):
        img = image.load_img(BytesIO(base64.b64decode(sample['image'])), target_size=IMG_SIZE)
        label = sample['label']
        pkmn_card = sample['pkmn_card']

"""
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'images' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('images')
        for file in files:
        # if user does not select file, browser also
        # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=images multiple>
      <input type=submit value=Upload>
    </form>
    '''

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
"""



if __name__ == "__main__":
    app.run(debug=True)
