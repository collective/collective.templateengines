"""

    Cheetah template engine backend.
    
    http://www.cheetahtemplate.org/

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__docformat__ = "epytext"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-clause BSD"

import logging

from zope import interface 

from Cheetah.Template import Template as CheetahTemplate
from Cheetah.ErrorCatchers import ListErrors

from collective.templateengines.interfaces import *
from collective.templateengines.utils import Message, exposeContextToFunctions


class Engine:
    """ Define a template engine back end for Cheetah.
    
    Notes.
    
    1) Cheetah registers tags (functions) on a template context level

    """
    
    zope.interface.implements(ITemplateEngine)
    
    def __init__(self):
        
        # Engine wide tags
        self.tags = {}
  
    def loadString(str, lazy):
        
        if lazy:
            raise NotImplementedError("This is not implemented")
        
        return Message.wrapExceptions(lambda: Template(text))
        
        
    def loadFile(file, lazy):
        """ Load template from a file.

        This function never raises an exception, but returns errors as ITemplateMesssage list.

        If the template cannot be loaded None is returned instead of ITemplate.
                
        @param lazy: Boolean, should template compiliation be posted until it is evaluated
        @return: (ITemplate object or None, [ list of ITemplateMessage objects ])
        """
        raise NotImplementedError("This is not implemented")
                
    def addTag(name, func):
        """ Register a new engine wide template tag.        
        """  
        
        # Cheetah does not have a global scope,
        # functions are added to the template context variables
        raise NotImplementedError("This is not implemented")
            
class Template:
    """ Cheetah template wrapper.
    """
    
    zope.interface.implements(ITemplate)    
    
    def __init__(self, text):
        
        self.text = text
        self.catcher =  ListErrors()
        
        # Cheetah does not have separate phases for compiling and evaluation
        #
        
    def evalute(context):
        """
        """
   
        # TODO: This is very ugly and not thread safe
        exposeContextToFunctions(context)
        
        def wrapped():
            self.template = CheetahTemplate(text, searchList=context.getMappings(), errorCatcher=self.catcher)
            output = str(self.template)
            return [output, Message.createFromStrings(self.catcher.listErrors())]
        
        return Message.wrapExceptions(wrapped)
        
    
    