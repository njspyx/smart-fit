import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dense, Dropout, Flatten
from tensorflow_core.python.keras.callbacks import ModelCheckpoint

train_image_path = "C:\\Users\\neelj\\Documents\\Python\\fruits-360" \
                   "\\modified-sets\\Training-modified"
test_image_path = "C:\\Users\\neelj\\Documents\\Python\\fruits-360" \
                  "\\modified-sets\\Test-modified"

batch_size = 128
num_classes = 115
num_epochs = 20
img_rows, img_cols = 50, 50
optimizer = Adam()

train_data_gen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
)
validation_data_gen = ImageDataGenerator(rescale=1./255,
                                         validation_split=0.2,)

train_data_gen = train_data_gen.flow_from_directory(
    train_image_path,
    # save_to_dir="C:\\Users\\neelj\\Documents\\Python\\fruits-360" \
    # "\\modified-sets\\training-processed",
    # save_format="jpeg",
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode="categorical",
    subset="training",
)

validation_data_gen = validation_data_gen.flow_from_directory(
    train_image_path,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode="categorical",
    subset="validation",
)

# Model Creation
model = Sequential()
model.add(Conv2D(16, kernel_size=(3, 3),
                 activation="relu", input_shape=(img_cols, img_rows, 3)))
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(128, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(150, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation="sigmoid"))

model.compile(loss="binary_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"],)

"""
CNN_model = model.fit(
    train_data_gen,
    epochs=num_epochs,
    shuffle=True,
    verbose=2,
    validation_data=validation_data_gen,
)
"""

CNN_model = model.fit_generator(
    train_data_gen,
    steps_per_epoch=train_data_gen.samples // batch_size,
    validation_data=validation_data_gen,
    validation_steps=validation_data_gen.samples // batch_size,
    epochs=num_epochs,
    verbose=0,
)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.sample_weights("model.h5")
print("Saved model to disk")









