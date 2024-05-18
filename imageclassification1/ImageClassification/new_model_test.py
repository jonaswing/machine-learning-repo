from keras.models import load_model
import numpy as np
import cv2
import tensorflow as tf
import os

img = cv2.imread('guy6.jpg')

resize = tf.image.resize(img, (256,256))

new_model = load_model(os.path.join('models', 'imageclassifier2.h5'))

yhat = new_model.predict(np.expand_dims(resize/255, 0))

print(yhat)

if yhat > 0.5:
    print(f'Predicted class is Ugly')
else:
    print(f'Predicted class is Hot')

#if yhat > 0.9:
#    print(1)
#elif 0.8 < yhat < 0.9:
#    print(2)
#elif 0.7 < yhat < 0.8:
#    print(3)
#elif 0.6 < yhat < 0.7:
#    print(4)
#elif 0.5 < yhat < 0.6:
#    print(5)
#elif 0.4 < yhat < 0.5:
#    print(6)
#elif 0.3 < yhat < 0.4:
#    print(7)
#elif 0.2 < yhat < 0.3:
#    print(8)
#elif 0.1 < yhat < 0.2:
#    print(9)
#elif yhat < 0.1:
#    print(10)

