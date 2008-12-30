"""
    Jinja 2 backend for evaluating templates.
    
    http://jinja.pocoo.org/2/

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"

import sys
import logging

from jinja2 import Environment, StrictUndefined

from zope import interface
from collective.templateengines.interfaces import *
from collective.templateengines.utils import Message

#class RaiseExceptionAlwaysUndefined(Undefined):
    
class Engine:
    """ Simple Jinja2 backend.
    
    Wraps jinja Environment for template creation.
    
    """
    
    interface.implements(ITemplateEngine)
    
    def __init__(self):
        
        # Raise exception always when a variable is missing
        self.env = Environment(undefined=StrictUndefined)
        self.tags = []
        
    def loadString(self, s, lazy):
        """ Create a template wrapper from string..
                
        """
        
        if lazy:
            raise NotImplementedError("This is not implemented")        
        
        
        
        try:
            return Template(self, s), [] 
        except Exception, e:
            return Message.wrapCurrentException()
        
    def addTag(self, tag):        
        """ Create generic tag -> Jinja2 function adaption. 
        
        Tags are directly given as a template context parameters.
        """
        self.tags.append(tag)
                    
class Context:
    """ Wrap template context variables for Jinja """
    
    interface.implements(ITemplateContext)
    
    def __init__(self, jinjacontext):
        self.jinjacontext = jinjacontext
    
    def addMapping(name, obj):
        """ Add new export mapping.
        
        @param name: Variable name
        @param obj: Python object
        """
        
    def getMappings():
        """ Export mappings as a Python dictionary
        @return: Dictionary
        """    
        return self.jinjacontext
    
    
class Template:
    """ Wrap Jinja2 template """
    
    interface.implements(ITemplate)
        
    def __init__(self, engine, templateData):
        self.engine = engine
        self.template = self.engine.env.from_string(templateData)
    
    def evaluate(self, context):
        
        # In Jinja, custom tags go directly to the template context
        tagged_context = context.getMappings().copy()        
        for tag in self.engine.tags:            
            tagged_context[tag.getName()] = TagProxy(context, tag)
        
        try:
            return self.template.render(tagged_context), []
        except Exception, e:
            return Message.wrapCurrentException()
        
                                            
class TagProxy:
    """ Map collective.templateengines Tag interface to Jinja implementation.
    
    All generic collective.templatenegines tags are exposed to Jinja through this implementatin.
    """
    
    
    
    def __init__(self, context, tag):
        """ 
        
        @param tag: ITag interface implementor
        """
        if not ITag.providedBy(tag):
            raise RuntimeError("Invalid tag declaration:" + str(tag))
        
        self.context = context
        self.tag = tag
        
    def __call__(self, *args, **kwargs):
        """ Internally ITag uses Jinja calling convention so we do direct argument mapping here. """
                
        return self.tag.render(self.context, *args, **kwargs)
        
        





