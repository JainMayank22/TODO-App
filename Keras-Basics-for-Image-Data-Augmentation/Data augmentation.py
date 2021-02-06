#!/usr/bin/env python
# coding: utf-8

# # Image Data Augmentation with Keras
# 
# ![Horizontal Flip](assets/horizontal_flip.jpg)

# # Task 1: Import Libraries

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import os
import numpy as np
import tensorflow as tf

from PIL import Image
from matplotlib import pyplot as plt

print('Using TensorFlow', tf.__version__)


# # Task 2: Rotation

# In[2]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range = 40
)


# In[3]:


image_path = 'images/train/cat/cat.jpg'

plt.imshow(plt.imread(image_path));


# In[6]:


x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 3: Width and Height Shifts

# In[7]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    width_shift_range = [-100, -50, 0, 50, 100],
    height_shift_range = [-50, 0, 50]
)


# In[8]:


x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 4: Brightness

# In[9]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    brightness_range = (0.5, 2)
)

x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 5: Shear Transformation

# In[13]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    # Your code here
    shear_range=40
)

x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 6: Zoom

# In[19]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    zoom_range = 0.5
)

x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 7: Channel Shift

# In[17]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    channel_shift_range = 100
)

x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 8: Flips

# In[25]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    horizontal_flip = True,
    vertical_flip = True,
    rotation_range = 30
)

x, y = next(generator.flow_from_directory('images', batch_size=1))
plt.imshow(x[0].astype('uint8'));


# # Task 9: Normalization
# 
# ### Featurewise

# In[27]:


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

generator = tf.keras.preprocessing.image.ImageDataGenerator(
    featurewise_center = True,
    featurewise_std_normalization = True
)

generator.fit(x_train)


# In[28]:


x, y = next(generator.flow(x_train, y_train, batch_size=1))
print(x.mean(), x.std(), y)
print(x_train.mean())


# ### Samplewise

# In[30]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    samplewise_center = True,
    samplewise_std_normalization = True
)

x, y = next(generator.flow(x_train, y_train, batch_size=1))
print(x.mean(), x.std(), y)


# # Task 10: Rescale and Preprocessing Function

# In[31]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1.,
    preprocessing_function = tf.keras.applications.mobilenet_v2.preprocess_input
)


# In[32]:


x, y = next(generator.flow(x_train, y_train, batch_size=1))


# In[35]:


print(x.mean(), x.std(), y)


# # Task 11: Using in Model Training

# In[ ]:


generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1.,
    preprocessing_function = tf.keras.applications.mobilenet_v2.preprocess_input
    horizontal_flip = True,
    rotation_range = 20
)


# In[36]:


model = tf.keras.models.Sequential([
    tf.keras.applications.mobilenet_v2.MobileNetV2(
        include_top = False, input_shape=(32, 32, 3),
        pooling='avg'
    ),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer = 'adam',
    metrics = ['accuracy']
)


# In[38]:


_ = model.fit(
generator.flow(x_train, y_train, batch_size = 32),
epochs = 1, steps_per_epoch = 10)


# In[ ]:




