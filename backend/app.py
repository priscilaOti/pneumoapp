# -*- coding: utf-8 -*-
"""Create an application instance."""
from core.app import create_app

from core.settings import ProductionConfig

app = create_app(ProductionConfig)