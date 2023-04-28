import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from keras.datasets import cifar10
import os

# Here we are loading CIFAR-10 Dataset
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# Now we are preprocessing Data
train_images = train_images / 255.0
test_images = test_images / 255.0

for i in range(10):
# Defining the model
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10))
    
    #Compiling the model
    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
    
    #Training the model
    history = model.fit(train_images, train_labels, epochs=15, 
                        validation_data=(test_images, test_labels))
    
    #Evaluating the modellll
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test accuracy:', test_acc)
    
    #Saving the model
    x='image_classification_model_'+str(i+1)+'.h5'
    path=os.path.join('Minor Project\Image Classification Model Training and Predicting\saving_model',x)
    model.save(path)