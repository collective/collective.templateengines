import unittest

from collective.templateengines.interfaces import *

from collective.templateengines.backends import cheetah

class CheetahTestCase(unittest.TestCase):
    
    def test_ok(self):
        
        variables = { "foo" : "bar" }
        engine = cheetah.Engine()
        
        template, messages = engine.loadFromString("$foo")
        self.assertNotEqual(template, None)
        self.assertTrue(ITemplate.providedBy(template))
        self.assertEqual(len(message), 0)
        
        result, messages = template.evaluate()
        
        self.assertEqual(result, "bar")
        self.assertEqual(len(message), 0)
            
    def test_syntax_error(self):
        """ Cheetah tells about syntax errors during run time """
        pass
    
    def test_missing_var(self):
        """ Cheetah tells about missing variables during run time """
        pass

    



if __name__ == "__main__":
    unittest.main()
