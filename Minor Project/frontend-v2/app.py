from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('..\Image Classification Model Training and Predicting\saving_model\image_classification_model.h5')
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Preprocess the input image
    img = Image.open(request.files['image']).resize((32, 32))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    # Make predictions
    pred = model.predict(img)
    pred_class = classes[np.argmax(pred)]
    pred_prob = float(np.max(pred))
    # Return the predictions as JSON
    return jsonify({'class': pred_class, 'probability': pred_prob})

if __name__ == '__main__':
    app.run(debug=True)
