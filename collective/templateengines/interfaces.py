"""

    Define generic interfaces to interact with template engines.
    
    NOTE: Work is still much in the progress and not everything in these interfaces have been implemented.

"""

from zope.interface import Interface

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__version__ = "0.1" # Match with egg package version
__docformat__ = "epytext"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-clause BSD"

class ITemplateEngine(Interface):
    """ Define a template engine back end.
    """
    
    def loadString(str, lazy):
        """ Load template from a string.
        
        This function never raises an exception, but returns errors as ITemplateMesssage list.
        
        If the template cannot be loaded None is returned instead of ITemplate.
        
        @param lazy: Boolean, should template compiliation be posted until it is evaluated
        @return: (ITemplate object or None, [ list of ITemplateMessage objects ])
        """
        
    def loadFile(file, lazy):
        """ Load template from a file.

        This function never raises an exception, but returns errors as ITemplateMesssage list.

        If the template cannot be loaded None is returned instead of ITemplate.
                
        @param lazy: Boolean, should template compiliation be posted until it is evaluated
        @return: (ITemplate object or None, [ list of ITemplateMessage objects ])
        """
        
    def addTag(name, tag):
        """ Register a new engine wide template tag.
        
        TODO 
        """

class ITemplate(Interface):
    """ One loaded template. 
    
    This object is created by a template engine loading functions. It exposes
    generic template related methods.
    """
    
    def evalute(context):
        """
        
        @param context: ITemplateContext object
        @return (The result as string, [ list of ITemplateMessage objects ])
        """
        
class ITemplateContext(Interface):
    """ Expose Python objects to the template language. 
    
    TODO: Needs polish
    """
    
    
    def addMapping(name, obj):
        """ Add new export mapping.
        
        @param name: Variable name
        @param obj: Python object
        """
        
    def getMappings():
        """ Export mappings as a Python dictionary
        @return: Dictionary
        """
        

class ITemplateMessage(Interface):
    """ Wrapper to diagnose error and debugging conditions in the templates.
    
    """
    
    def getLevel():
        """ One of Python logging package levels.
        
        E,g. logging.WARNING, logging.INFO. This is used to filter debugging output.
        """
        
    def getMessage():
        """ One line string containing the message
        """
        
    def getDebugInfo():
        """ Many lines of template language specific debugging info attached to the message.
        
        @return: plain text string
        """
        
    def getException():
        """ Python traceback associated with the message.
        
        @return: tuple (exception, message, traceback)
        """
        
class ITag(Interface):
    """ Simple function exposed to the template engine. 
    
    This allows call the function with context and parameters. E.g::
    
        {% do_random_crap("foo", "bar") %}
    """
    
    def getName():
        """
        @return: String, name of the tag as used in templates
        """
    
    def render(context, *args, **kwargs):
        """
        @param context: ITemplateContext
        @return: generated document code as string 
        """
    
        