# -*- coding: utf-8 -*-
"""Click commands."""
import os

import click
from flask_migrate import MigrateCommand

HERE         = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH    = os.path.join(PROJECT_ROOT, 'tests')


@click.command()
def test():
  """Run the tests."""
  import unittest
  
  testsuite = unittest.TestLoader().discover(TEST_PATH)
  unittest.TextTestRunner(verbosity=2).run(testsuite)


@click.command()
def db():
  """Run the tests."""
  return MigrateCommand

@click.command()
def clean():
  """Remove files recursively starting at current directory."""
  blacklist_filename = ['test.db']
  blacklist_extensions = ['.pyc', '.pyo']
  ignore_path = ['./venv', './.git', './static']

  for dirpath, _, filenames in os.walk('.'):
    has_ignore_path = any(map(dirpath.startswith, ignore_path))

    if not has_ignore_path:
      for filename in filenames:
        has_extension = any(
          [filename.endswith(end) for end in blacklist_extensions])

        if filename in blacklist_filename or has_extension:
          full_pathname = os.path.join(dirpath, filename)
          click.echo('Removing {}'.format(full_pathname))
          os.remove(full_pathname)