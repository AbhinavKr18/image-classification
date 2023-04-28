from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Making an array containing 5 models
model = []
for i in range(10):
    model_name = "..\Image Classification Model Training and Predicting\saving_model\model"+str(i+1)+".h5"
    model.append(tf.keras.models.load_model(model_name))

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Preprocess the input image
    img = Image.open(request.files['image']).resize((32, 32))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Make predictions in all 5 models
    pred = []
    pred_class = []
    pred_prob = []

    for i in range(len(model)):
        pred.append(model[i].predict(img))
        pred_class.append(classes[np.argmax(pred[i])])
        pred_prob.append(float(np.max(pred[i])))
        print("Probability:"+str(pred_prob[i])+", Class:"+pred_class[i])    

    # Finding the best probability and storing its index
    final_pred_class = pred_class[0]
    final_pred_prob = pred_prob[0]

    for i in range(1,5):
        if pred_prob[i] > final_pred_prob:
            final_pred_prob = pred_prob[i]
            final_pred_class = pred_class[i]


    # Return the predictions as JSON
    return jsonify({'class': final_pred_class, 'probability': final_pred_prob})

if __name__ == '__main__':
    app.run(debug=True)
