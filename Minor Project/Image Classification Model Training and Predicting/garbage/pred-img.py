import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
#loading the 10 models saved
models = []
for i in range(9):
    model_path = f'Minor Project\Image Classification Model Training and Predicting\saving_model\image_classification_model_{i+1}.h5'
    model = keras.models.load_model(model_path)
    models.append(model)
#loading the desired image
image_path = input("Enter image path: ")
image = Image.open(image_path)
image = image.resize((32, 32))
image = np.array(image)
image = image.astype('float32')
image /= 255
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
#Here we are now predicting the class for the selected image, by using the model having the most accuracy
predictions = []
for model in models:
    prediction = model.predict(np.array([image]))
    predictions.append(prediction)
# choose the model with highest accuracy
best_model_idx = np.argmax([pred[0][np.argmax(pred[0])] for pred in predictions])
best_model = models[best_model_idx]
# make prediction using the best model
prediction = best_model.predict(np.array([image]))
predicted_class = class_names[np.argmax(prediction)]
print('Predicted class:', predicted_class)