# -*- coding: utf-8 -*-
"""The factory function."""
import json

import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array

from core.settings import Config


def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def load_model(model_path = '', weights_path = ''):
  json_file = open(model_path, 'r')
  loaded_model_json = json_file.read()
  json_file.close()

  loaded_model = model_from_json(loaded_model_json)
  loaded_model.load_weights(weights_path, by_name=True)

  return loaded_model


def preprocess_image(image_path, target_size = (28, 28)):
  image = cv2.imread(image_path)
  image = cv2.resize(image, target_size)
  image = img_to_array(image)

  return np.array([image], dtype="float") / 255.0 


def build_labels(labels, probs=[]):
  return { labels[i] : float(prob) for i, prob in enumerate(probs) }
