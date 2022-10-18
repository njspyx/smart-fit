from keras.models import model_from_json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dense, Dropout, Flatten
from keras.callbacks import ModelCheckpoint

batch_size = 128
num_classes = 12
num_epochs = 20
img_rows, img_cols = 100, 100
optimizer = Adam()

idx_cls_dict = {0: 'Apple Red Yellow', 1: 'Banana', 2: 'Cauliflower', 3: 'Eggplant', 4: 'Lemon', 5: 'Mandarine',
                6: 'Pear', 7: 'Pepper Green', 8: 'Pepper Red', 9: 'Strawberry', 10: 'Tomato', 11: 'Watermelon'}


def predict_using_model(img_path):
    json_file = open('C:\\Users\\neelj\\PycharmProjects\\cac2020\\classifier\\s_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("C:\\Users\\neelj\\PycharmProjects\\cac2020\\classifier\\s_model.h5")

    loaded_model.compile(loss="binary_crossentropy",
                  optimizer=optimizer,
                  metrics=["accuracy"], )

    predict_generator = ImageDataGenerator(rescale=1 / 255.)

    predict_generator = predict_generator.flow_from_directory("C:\\Users\\neelj\\PycharmProjects\\cac2020\\classifier",
                                                              classes=["test-images"],
                                                              class_mode=None,
                                                              shuffle=False,
                                                              target_size=(img_rows, img_cols),
                                                              )
    predictions = loaded_model.predict_generator(predict_generator)
    preds_cls_idx = predictions.argmax(axis=1)
    if "Capture" in img_path:
        return idx_cls_dict[preds_cls_idx[1]]
    else:
        return idx_cls_dict[preds_cls_idx[0]]