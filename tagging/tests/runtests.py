#!/usr/bin/env python

"""Boilerplate runtests.py for using django-nose to test this app. Adapted from
dcramer's post on https://github.com/jbalogh/django-nose/issues/46"""

import sys
import os, os.path
from optparse import OptionParser

from django.conf import settings

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tagging.tests.settings'

from django_nose import NoseTestSuiteRunner

def runtests(*test_args, **kwargs):
    if 'south' in settings.INSTALLED_APPS:
        from south.management.commands import patch_for_test_db_setup
        patch_for_test_db_setup()

    test_runner = NoseTestSuiteRunner(**kwargs)

    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)
