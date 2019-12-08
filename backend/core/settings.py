# -*- coding: utf-8 -*-
"""Application configuration."""
import os
import datetime

class Config(object):
  """Base configuration."""
  SECRET_KEY   = os.environ.get('SECRET_KEY')
  APP_DIR      = os.path.abspath(os.path.dirname(__file__))
  PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  UPLOAD_FOLDER      = os.path.join(PROJECT_ROOT, 'static', 'uploads')
  ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])


class DevConfig(Config):
  """Development configuration."""
  ENV = 'development'
  DEBUG = True

class ProductionConfig(Config):
  """Production configuration."""
  ENV = 'production'
  DEBUG = False