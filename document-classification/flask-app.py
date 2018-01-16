"""
Flask application that facilates categorical predictions for 
dam removal text documents. 

Requires "filename.txt" document as input for classification
"""
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import pickle


app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt'])  # only txt files for now


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def get():
    return 'Hello there...\n\n🤠'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return 'Needs to be a .txt file type'
            file = request.files['file']
            
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                return 'No file...'
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
            # pre-process
            tfidf = load_tfidf.transform([file.read()])
            prediction = clf.predict(tfidf)
            if prediction == 0:
                return jsonify({'Classification': 'Abiotic'})
            if prediction == 1:
                return jsonify({'Classification': 'Biotic'})
            if prediction == 2:
                return jsonify({'Classification': 'Biotic & Abiotic'})
        except Exception as e:
            print(e)
            return 'Exception occured' + e

    return '''
    <!doctype html>
    <title>Prediction</title>
    <h1>Select File to predict</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    try:
        # Load scikit learn model
        clf = pickle.load(open('random_forest_classifier.sklearn', 'rb'))
        # Load previous tfidf representation
        load_tfidf = pickle.load(open('tfidf.sklearn', 'rb'))
        print('Resources Loaded')

    except Exception as e:
        print(e)
        clf = None

    app.run(host='0.0.0.0', port=9999, debug=True)