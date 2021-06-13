from flask import Flask, render_template, request, jsonify
import base64
from face_recognizer_image import image_rec
import numpy as np


app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/video_feed', methods=['GET', 'POST'])
def video_feed():
    image = request.json['image']
    # print(image)
    image = image.split(',')[1]
    with open('snapshot.jpg', 'wb') as f:
        f.write(base64.b64decode(image))
    
    image_rec(np.frombuffer(base64.b64decode(image), dtype=np.uint8))
    return jsonify(image)


if __name__ == '__main__':
    app.run(debug=True)