#New one
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
#loading the saved model
model = keras.models.load_model('Minor Project\Image Classification Model Training and Predicting\saving_model\image_classification_model.h5')
#loading the desired image
image_path = input("Enter image path: ")
image = Image.open(image_path)
image = image.resize((32, 32))
image = np.array(image)
image = image.astype('float32')
image /= 255
#making prediction
prediction = model.predict(np.array([image]))
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
               'dog', 'frog', 'horse', 'ship', 'truck']
predicted_class = class_names[np.argmax(prediction)]
print('Predicted class:', predicted_class)
