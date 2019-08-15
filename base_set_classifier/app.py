import os
import csv
import json
import base64
import uuid
from io import BytesIO
from tensorflow.keras.preprocessing import image
from flask import json as j
from flask import Flask, request
from werkzeug.utils import secure_filename

IMG_FOLDER = '/home/dev/Desktop/'
RAW_CSV = '/home/dev/raw.csv'
UNLABELED_CSV = '/home/dev/unlabeled.csv'
TF_SERVER = ''
IMG_SIZE = (550, 400)
SPACE = True

app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER

@app.route('/base_set_classifier/predict/', methods=['POST'])
def base_set_classifier():
    payload = None # paload to send to TF server
    for sample in request.form.getlist('samples'):
        img = image.load_img(BytesIO(base64.b64decode(sample['image'])), target_size=IMG_SIZE)
        # if there is enough space to store images
        if SPACE:
            # save image
            filename = get(sample, 'filename')
            filename = get_secure_filename(filename)
            path = os.path.join(app.config['IMG_FOLDER'], filename)
            img.save(path, format=img.format)
            # write to csv files
            label = get(sample, 'label')
            img_label = get(sample, 'img_label')
            if check_img_label(img_label) and check_label(label):
                with open(RAW_CSV, 'a') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([filename, label, img_label])
            else:
                with open(UNLABELED_CSV, 'a') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([filename])
        img = image.img_to_array(img)
        ### add img to payload in correct way
    # querying TF server
    r = requests.post(TF_SERVER, json=payload)
    # decoding the response from the TF server and loading it into a json object
    predictions = j.loads(r.content.decode('utf-8'))
    return j.jsonify(predictions) # dumping the json object to a response object that is returned



######## Helper functions

def check_img_label(img_label):
    if (img_label == 'pkmn_card') or (img_label == 'not_pkmn_card'):
        return True
    else:
        return False

def check_label(label):
    if (label == 'base_set') or (label == 'not_base_set'):
        return True
    else:
        return False

def get(d, key):
    try:
        user_key = d[key]
    except KeyError:
        user_key = None
    return user_key

def get_secure_filename(filename, file_path):
    if filename == None:
        fname = unique_random_filename(file_path)
        return fname
    else:
        fname = secure_filename(filename)
        fname = os.path.splitext(fname)[0]
        if (fname == '') or (fname in {i[0] for i in map(os.path.splitext, os.listdir(file_path))}):
            fname = unique_random_filename(file_path)
        return fname

def unique_random_filename(file_path):
    fname = str(uuid.uuid4())
    while fname in {i[0] for i in map(os.path.splitext, os.listdir(file_path))}:
        fname = str(uuid.uuid4())
    return str(uuid.uuid4())
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
