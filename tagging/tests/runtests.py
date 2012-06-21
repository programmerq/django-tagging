#!/usr/bin/env python

import os
from django.utils import unittest

if not 'DJANGO_SETTINGS_MODULE' in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tagging.tests.settings'

from django.conf import settings
from django.db import connection
from django.test.utils import setup_test_environment
from django.test.utils import teardown_test_environment
from django.utils.importlib import import_module

TEST_MODULES = ["tagging.tests.tests"]

def run_tests():
    setup_test_environment()
    db_name = settings.DATABASE_NAME
    suite = unittest.TestSuite()
    for module_name in TEST_MODULES:
        module = import_module(module_name)
        suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    connection.creation.create_test_db()
    unittest.TextTestRunner().run(suite)
    teardown_test_environment()

if __name__ == "__main__":
    run_tests()
