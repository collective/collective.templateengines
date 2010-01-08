"""

    Plone-specific security and context mappings.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"


from zope import interface
from zope.app.component.hooks import getSite
from zope.component import getMultiAdapter, getSiteManager

from collective.templateengines.interfaces import *

from AccessControl import ClassSecurityInfo
from AccessControl import getSecurityManager
from AccessControl import Unauthorized

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.interfaces import IBaseObject
 
class ArchetypesSecureContext:
    """ Wrap Archetypes object inside a secure context.
    
    Use the priviledges of currently logged in user.
    
    TODO: Field access rights are not respected
    """
    
    interface.implements(ITemplateContext)

    def __init__(self, context, expose_schema=True):
        """
        
        @param expose_schema: Map AT schema accessors directly to template variables for
            engines which cannot traverse Zope content (Cheetah).
        """
        
        security=getSecurityManager()
        
        #portal_state = getMultiAdapter((context, context.REQUEST), name=u'plone_portal_state')
        
        try:
            portal_state = context.restrictedTraverse("@@plone_portal_state")
        except Unauthorized:
            # portal_state may be limited to admin users only
            portal_state = None
        except AttributeError:
            # traversing it not yet proplerly set up
            # may happen with some contexts, e.g. with LinguaPlone translate
            portal_state = None
            
                                
        site = getSite()
        
        # Site might not have portal url or REQUEST when it is being duplicated through ZMI...
        # corner cases... you must love them!
        portal_url = getattr(site, "portal_url", None)        
        request = getattr(site, "REQUEST", None)
        

        self.namespace = {
            "portal" : site,
            "context" : context,
            "portal_url" : portal_url,
            "object_url" : context.absolute_url(),
            "user" : security.getUser(),
            "request" : request,            
            "portal_state" : portal_state
        }   
        
        try:
            # Archetypes unique identifier number
            # not available on non-archetypes content
            self.namespace["UID"] = context.UID()  
        except:
            pass
        
        if expose_schema and IBaseObject.providedBy(context):
            
            # The following applies to Archetypes objects only
            
            schema = context.Schema()
            for f in schema.fields():
                name = f.getName()
                try:
                    value = f.get(context)
                    
                    # Make sure that template engine receives all variables in Unicode
                    if isinstance(value, str):
                        value = value.decode("utf-8")
                    
                    self.namespace[name] = value
                except TypeError:
                    # membrane field "listed" gives TypeError, don't know why
                    pass
                
    def addMapping(self, name, var):
        self.namespace[name] = var
        
    def getMappings(self):
        return self.namespace
    
    def getTraversingContext(self):
        """ Get zope traversing context - don't confuse context with context! """
        return self.namespace["context"]
        
    
    
    