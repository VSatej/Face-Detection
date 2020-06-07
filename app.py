from flask import Flask,render_template,request,redirect,jsonify
from face_detection import face_detect
import json
import os

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = '../Face Detection/static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-image',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if request.files:
            picture = request.files['image']
            picture.save(os.path.join(app.config['IMAGE_UPLOADS'],picture.filename))
            face_list = face_detect(picture)
            print(face_list)
    return render_template('image.html',detect=face_list)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
