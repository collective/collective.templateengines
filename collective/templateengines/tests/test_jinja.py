"""

    Test Jinja backend.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"

import unittest

from base_test import BaseTemplateEngineTestCase

from collective.templateengines.utils import DictionaryContext, TagProxy
from collective.templateengines.interfaces import *
from collective.templateengines.backends import jinja

class JinjaTestCase(BaseTemplateEngineTestCase, unittest.TestCase):

    def getEngine(self):
        return jinja.Engine()
    
    def getFooTemplate(self):
        """ Return template using foo variable. """
        return "{{ foo }}"
    
    def getTestTagTemplate(self):
        """ Return template using foo variable. """
        return "{{ test_tag('123') }}"
    
    def getBrokenTemplate(self):
        """ Return template having syntax errors. """
        return "{% if %}"
    

    
if __name__ == "__main__":
    unittest.main() # run all tests
