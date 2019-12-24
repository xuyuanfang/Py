import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
print('tensorflow: v',tf.__version__)

img = cv2.imread('kebi.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(480,480))
print(img.shape)
datas = img
conv0 = tf.layers.conv2d(datas,10,5,activation=tf.nn.relu)
pool0 = tf.layers.max_pooling2d(conv0,[2,2],[2,2])

conv1 = tf.layers.conv2d(pool0,40,4,activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(conv1,[2,2],[2,2])

# flatten = tf.layers.flatten(pool1)
#
# fc = tf.layers.dense(flatten,400,activation=tf.nn.relu)

