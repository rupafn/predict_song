import pickle
import numpy as np 
import re
from flask import Flask, request, jsonify, render_template
import os
import sys
sys.path.insert(1, '/controllers')
from app.controllers import mp3_to_wav as convert
from app.controllers import extract_low_features as extract
from app.controllers import process_audio 
import sklearn
app = Flask(__name__)
model = pickle.load(open('app/svm-ll-withoutstats-all-feats.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html',title='Classify the song')

@app.route('/result', methods=['POST'])
def predict():
    print(request.files)
    audio_file = request.files['Name']
    filename = request.files['Name'].filename
    print(filename)
    audio_file.save('app/media/'+filename)
    # print('done')
    convert.convertToWav(filename)
   
    filename = filename.split('.')[0]

    extract.extractFeatures('app/wav/'+filename+'.wav','app/output/'+filename+'.csv')
    process_audio.process_data('app/output/'+filename+'.csv')
    feats = process_audio.process_data('app/output/'+filename+'.csv')
    result = process_audio.predict(feats)[0]
    # print(result)
    return render_template('result.html', result=result,title='Result')



if __name__ == '__main__':
    app.run(debug=True)

