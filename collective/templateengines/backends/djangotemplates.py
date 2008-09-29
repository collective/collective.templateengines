"""
    Django backend for evaluating templates.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"

import sys
import logging

from django.template import Context as DjangoContext
from django.template import Template as DjangoTemplate

from zope import interface
from collective.templateengines.interfaces import *
from collective.templateengines.utils import Message

class Engine:
    """ Simple Django backend.
    
    """
    
    interface.implements(ITemplateEngine)

    def loadString(self, s, lazy):
        """ Create a Cheetah template wrapper.
        
        FIXME: The actual Template object is created when the template is evaluted.        
        """
        
        if lazy:
            raise NotImplementedError("This is not implemented")        
        
        try:
            return Template(s), [] 
        except Exception, e:
            return Message.wrapCurrentException()
        
class Template:
    
    interface.implements(ITemplate)
        
    def __init__(self, templateData):
        self.template = DjangoTemplate(templateData)
    
    def evaluate(self, context):
        
        dc = DjangoContext(context.getMappings().copy())
        
        try:
            # Django does not provide callback to notify about missing vars
            return self.template.render(dc), []
        except Exception, e:
            return Message.wrapCurrentException()
        
                                            


    






