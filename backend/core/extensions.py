# -*- coding: utf-8 -*-
"""Extensions utilities."""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import current_app

db = SQLAlchemy()
migrate = Migrate(db=db)
