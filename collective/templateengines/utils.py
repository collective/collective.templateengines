"""

    Helper functions and classes.

"""

import sys
import types
import traceback

from zope.interface import Interface

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__docformat__ = "epytext"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-clause BSD"

import logging

from zope import interface 

from collective.templateengines.interfaces import *

class Message:
    """ Generic message implementation. 
    
    This class has helper functions to convert string and exception objects
    to wrapped messages.
    
    TODO: Convert to instance service which can be given to the engine as a environment parameter.
    """
    
    interface.implements(ITemplateMessage)
    
    # List of exceptions which should not be automatically wrapped
    # and are handled by the lower parts of the framework using
    # collective.templateengines. 
    # E.g. Zope's Unauthorized exceptions
    unwrappableExceptions = []
    
    def __init__(self, message, level=logging.ERROR, exception=None, debug=None):
        """
        
        @param message: One liner describing the condition
        @param level: Python logging package logging level
        @param traceback: Tuple (exception, msg, traceback)
        @param debug: Debug info, as a plain-text string
        """
        self.message = message
        self.level = level
        self.exception = exception
        self.debug = debug
        
        
    def __str__(self):
        """ Helper function to easy error output from code. """
        return str(self.level) + ":" + str(self.message)
        
    def getLevel(self):
        return self.level
    
    def getMessage(self):
        return self.message
    
    def getException(self):
        return self.exception
    
    def getDebugInfo(self):
        return self.debug
    
    @staticmethod
    def isUnwrappable(e):
        """ Return True if exception should not be converted to Message instance
        @param e: Exception     
        """
        for ue in Message.unwrappableExceptions:
            if isinstance(e, ue):
                return True
            
        return False
    
    @staticmethod 
    def createFromStrings(msgs, level=logging.ERROR):
        """ Create error messages from strings.
        """
        return [ Message(msg, level) for msg in msgs ]
    
    @staticmethod
    def wrapCurrentException():
        """ Call inside an exception handler to return the exception as message list format. """
                
        tb_info = sys.exc_info()            
        return (None, [Message(str(tb_info[0]) + str(tb_info[1]), exception=tb_info)])        
    
    @staticmethod
    def wrapExceptions(func, *args, **kwargs):
        """ Call function and wrap possible exceptions to ITemplateMessages.
        
        If exception is not raised return the result as is.
                
        @return: function result or tuple (None, [ITemplateMessage]) 
        """
        try:
            return func(*args, **kwargs)
        except Exception, e:
            
            if Message.isUnwrappable(e):
                raise e
            
            tb_info = sys.exc_info()
            return (None, [Message(str(e), exception=tb_info)])
    
    
def log_messages(logger, messages):
    """ Write template messges to logger output
    
    @param logger: Python logging logger
    @param messages: Sequence of ITemplateMessage objects
    """
    for msg in messages: 
        assert ITemplateMessage.providedBy(msg)
        logger.log(msg.getLevel(), msg.getMessage())
        if msg.getException():
            exc, note, traceback = msg.getException()
            logger.exception(exc)
            
def dump_messages(messages, stream=sys.stdout):        
    """ Print ITemplateMessage objects to standard output.
    
    @param messages: Sequence of ITemplateMessage objects
    @param stream: Python file like object
    """
    for msg in messages:
        print str(msg)
        assert ITemplateMessage.providedBy(msg)
        print >> stream, msg.getMessage()
        
        exc, msg, tb = msg.getException()
        traceback.print_tb(tb, file=stream)
    
            
class DictionaryContext:
    """ Simple context holding exposed template variables in passthrough dictionary. """
    
    interface.implements(ITemplateContext)
    
    def __init__(self, mappings={}):
        self.mappings = mappings.copy()
        
    def addMapping(self, name, obj):
        self.mappings[name] = obj
        
    def getMappings(self):
        return self.mappings
    
    
class TagProxy:
    """ Map collective.templateengines Tag interface to any Python function call context as the first argument.
    
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
        