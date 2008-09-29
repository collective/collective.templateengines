"""

    Test Django backend.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"



import unittest

from base_test import BaseTemplateEngineTestCase


# Django assumes we have done some preinit setup magic
from django.core.management import setup_environ
from collective.templateengines import backends
setup_environ(backends) # Give any dummy module as parameter and Django will use default settings


from collective.templateengines.utils import DictionaryContext
from collective.templateengines.interfaces import *
from collective.templateengines.backends import djangotemplates

class DjangoTestCase(BaseTemplateEngineTestCase, unittest.TestCase):

    def getEngine(self):
        return djangotemplates.Engine()
    
    def getFooTemplate(self):
        """ Return template using foo variable. """
        return "{{ foo }}"
    
    def getBrokenTemplate(self):
        """ Return template having syntax errors. """
        return "{% if %}"
    
    def test_syntax_errors(self):
        """ Test Cheetah template having syntax errors. """
        engine = self.getEngine()
        
        context = DictionaryContext({})
        
        # No {% endif %}
        template, errors = engine.loadString(self.getBrokenTemplate(), False)
        
        self.assertEqual(len(errors), 1)
        
            
    
    def test_missing_var(self):
        """ Django does not detect missing template variables but substitutes them with an empty string. """
        pass
        
if __name__ == "__main__":
    unittest.main() # run all tests
