# -*- coding: utf-8 -*-
"""Classifier views."""
import os
import hashlib
import operator

from werkzeug.utils import secure_filename
from flask import Blueprint, jsonify, request, current_app

from core.classifier.utils import load_model, allowed_file, preprocess_image, build_labels

blueprint = Blueprint('classifiers', __name__, url_prefix='/api/classifiers')

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

model = None

def start_model():
  global model

  path_model = os.path.join(
                CURRENT_DIR, 'algorithms', 'lenet_v1.json')
    
  path_weights = os.path.join(
                  CURRENT_DIR, 'algorithms', 'lenet_v1.h5')

  model = load_model(path_model, path_weights)


@blueprint.route('/predict/', methods = ['POST'])
def get_results():
  global model

  data = {
    'error' : {
      'status' : 400,
      'message' : "Bad Request: Missing or empty field. Please upload an image with the extension jpeg." 
    }
  }

  if 'image' not in request.files:
    return data, 400

  image = request.files.get('image')

  if not image or image.filename == '':
    return data, 400

  if not allowed_file(image.filename):
    return data, 400
  
  filename = secure_filename(image.filename)
  image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename) 
  
  image.save(image_path)

  path_model = os.path.join(CURRENT_DIR, 'algorithms', 'lenet_v1.json')
  
  path_weights = os.path.join(CURRENT_DIR, 'algorithms', 'lenet_v1.h5')

  if model is None:
    start_model()

  image = preprocess_image(image_path)

  labels = ['NORMAL', 'PNEUMONIA']
  results = model.predict(image)
  probabilities = build_labels(labels, results[0])

  os.remove(image_path)

  return {
    'success': True,
    'prediction': max(probabilities.items(), key=operator.itemgetter(1))[0],
    'probabilities': probabilities
  }
