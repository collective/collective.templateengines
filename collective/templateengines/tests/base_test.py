"""

    Implement few generic tests which can be run against all test cases.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"


import unittest

from collective.templateengines.utils import DictionaryContext, dump_messages
from collective.templateengines.interfaces import *

from collective.templateengines.context.tags import TestTag

class BaseTemplateEngineTestCase:
    """ Implement few tests for any template backend. """
    
    def setUp(self):
        """Call before every test case."""
                
    def tearDown(self):
        pass
    
    def getEngine(self):
        raise RuntimeError("Subclasses must implement this")

    def getFooTemplate(self):
        """ Return template using foo variable. """
        raise RuntimeError("Subclasses must implement this")

    def getTestTagTemplate(self):
        """ Return template using foo function. """
        raise RuntimeError("Subclasses must implement this")

    def getBrokenTemplate(self):
        """ Return template having syntax errors. """
        raise RuntimeError("Subclasses must implement this")
    
    def test_success(self):
        """ Test succesful Cheetah template. """
        engine = self.getEngine()
        
        context = DictionaryContext({"foo":"bar"})
        
        template, errors = engine.loadString(self.getFooTemplate(), False)
        
        if errors:
            dump_messages(errors)

        self.assertEqual(len(errors), 0)
        self.assertTrue(ITemplate.providedBy(template))
        
        result, errors = template.evaluate(context)

        if errors:
            dump_messages(errors)

        self.assertEqual(len(errors), 0)
        self.assertEqual(result, "bar")

    def test_syntax_errors(self):
        """ Test Cheetah template having syntax errors. """
        engine = self.getEngine()
        
        context = DictionaryContext({})
        
        template, errors = engine.loadString(self.getBrokenTemplate(), False)
        #
        #self.assertEqual(len(errors), 1)
        raise RuntimeError("This test b0rks - don't know why unclosed #if is accepted")
        
    def test_missing_var(self):
        """ Test template having a missing variable. """
        engine = self.getEngine()
        
        context = DictionaryContext({})
        
        template, errors = engine.loadString(self.getFooTemplate(), False)
        
        self.assertEqual(len(errors), 0)
        self.assertTrue(ITemplate.providedBy(template))
        
        result, messages = template.evaluate(context)
        self.assertEqual(len(messages), 1)
        self.assertEqual(result, None)

    def test_custom_tag(self):
        """ Test that adding custom tags via ITag interface works """

        engine = self.getEngine()
        
        context = DictionaryContext({})
        
        tag = TestTag()
        
        engine.addTag(tag)
        
        template, errors = engine.loadString(self.getTestTagTemplate(), False)
        
        if errors:
            dump_messages(errors)

        self.assertEqual(len(errors), 0)
        self.assertTrue(ITemplate.providedBy(template))        
        
        result, errors = template.evaluate(context)

        if errors:
            dump_messages(errors)

        self.assertEqual(len(errors), 0)
        self.assertEqual(result, u"bar is 123")

        
if __name__ == "__main__":
    unittest.main() # run all tests
