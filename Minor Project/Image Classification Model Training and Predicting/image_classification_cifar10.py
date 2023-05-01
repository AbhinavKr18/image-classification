import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers, models
from keras.datasets import cifar10

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data() # Loading CIFAR-10 

train_images = train_images / 255.0 # Pre-Processing the data
test_images = test_images / 255.0

model = models.Sequential() # Defining the model
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']) #Compiling the model

#Keeping the batch size as 64
history = model.fit(train_images, train_labels, epochs=1, batch_size=64 ,validation_data=(test_images, test_labels)) #Training the model

#Evaluating the modellll
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)
#Saving the model
model.save('Minor Project\Image Classification Model Training and Predicting\saving_model\model_epoch50_batch_size64_original_base.h5')
