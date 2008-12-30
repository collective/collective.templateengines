"""

    Generic, test and internal tags.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"

from zope import interface

from collective.templateengines.interfaces import *

class TestTag(object):
    """ Demostrate custom tags. """
    
    interface.implements(ITag)
    
    def render(self, context, parameter, *args, **kwargs):
        return "bar is " + parameter
        
    def getName(self):
        return "test_tag"
    