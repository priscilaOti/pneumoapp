# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask
from flask_cors import CORS

from core.extensions import db, migrate
from core import commands

from core import classifier


def register_blueprints(app):
  """Register Flask blueprints."""
  app.register_blueprint(classifier.views.blueprint)


def register_extensions(app):
  """Register Flask extensions."""
  db.init_app(app)
  migrate.init_app(app)


def register_commands(app):
  """Register Click commands."""    
  app.cli.add_command(commands.test)
  app.cli.add_command(commands.clean)
  app.cli.add_command(commands.db)


def create_app(config_object):
  """
  Application factory.

  :param config_object: The configuration object to use.
  """
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(config_object)

  register_blueprints(app)
  register_extensions(app)
  register_commands(app)

  return app
