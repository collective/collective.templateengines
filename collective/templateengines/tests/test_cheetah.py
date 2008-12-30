"""

    Test Cheetah backend.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"


import unittest

from base_test import BaseTemplateEngineTestCase

from collective.templateengines.backends import cheetah

class CheetahTestCase(BaseTemplateEngineTestCase, unittest.TestCase):

    def getEngine(self):
        return cheetah.Engine()
    
    def getFooTemplate(self):
        """ Return template using foo variable. """
        return "$foo"
    
    def getTestTagTemplate(self):
        """ Return template using foo function. """
        return "$test_tag('123')"    
    
    def getBrokenTemplate(self):
        """ Return template having syntax errors. """
        return "#if"
        
if __name__ == "__main__":
    unittest.main() # run all tests
