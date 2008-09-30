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
    """
    
    interface.implements(ITemplateMessage)
    
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
        
    def getLevel(self):
        return self.level
    
    def getMessage(self):
        return self.message
    
    def getException(self):
        return self.exception
    
    def getDebugInfo(self):
        return self.debug
    
    @staticmethod 
    def createFromStrings(msgs, level=logging.ERROR):
        """ Create error messages from strings.
        """
        return [ Message(msg, level) for msg in msgs ]
    
    @staticmethod
    def wrapCurrentException():
        """ Call inside an exception handler to return the exception as message list format. """
        tb_info = sys.exc_info()
        return (None, [Message(tb_info[0], exception=tb_info)])        
    
    @staticmethod
    def wrapExceptions(func, *args, **kwargs):
        """ Call function and wrap possible exceptions to ITemplateMessages.
        
        If exception is not raised return the result as is.
                
        @return: function result or tuple (None, [ITemplateMessage]) 
        """
        try:
            return func(*args, **kwargs)
        except Exception, e:
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
    
        
def exposeContextToFunctions(context):
    """ A hack function to expose the template context to functions in 
    engines which do not pass the context around (Cheetah).
    
    We add context directly as a variable to the function object itself.
    This of course kills performance on non CPython implementations and
    is not thread safe!!
    
    A proper solution would be use some sort of interfaces thread specific storage,
    but this does it for now.
    """
        
    # TODO: Temporary hack - cheetah does not pass template context to the functions
    # We add namespace directly as a function attribute, 
    # so that it is accessible in the function without
    # explitcly passing it there. There must be a smarter
    # way to do this, but Cheetag docs didn't tell it.
    # This is not threadsafe, but Zope doesn't use threads...        
    mappings = context.getMappings()
    
    for func in mappings.values():
        if type(func) == types.FunctionType:
            func.namespace = mappings
    
        
    
    
    
    
        
