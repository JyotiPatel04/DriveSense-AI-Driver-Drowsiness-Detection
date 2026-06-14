import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("drowsiness_model.h5")

img = cv2.imread("test.jpg")
img = cv2.resize(img, (64,64))
img = np.expand_dims(img, axis=0)

pred = model.predict(img)

print("Prediction:", pred)