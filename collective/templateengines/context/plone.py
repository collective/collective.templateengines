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

from Products.CMFCore.utils import getToolByName

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
        
        portal_state = context.restrictedTraverse("@@plone_portal_state")
        
        site = getSite()

        self.namespace = {
            "portal" : site,
            "context" : context,
            "portal_url" : getToolByName(context, 'portal_url'),
            "object_url" : context.absolute_url(),
            "user" : security.getUser(),
            "request" : context.REQUEST,
            "uid" : context.UID(), # Archetypes unique identifier number
            "portal_state" : portal_state
        }        
        
        if expose_schema:
            schema = context.Schema()
            for f in schema.fields():
                name = f.getName()
                value = f.get(context)
                self.namespace[name] = value

        
    def addMapping(self, name, var):
        self.namespace[name] = var
        
    def getMappings(self):
        return self.namespace
    
    def getTraversingContext(self):
        """ Get zope traversing context - don't confuse context with context! """
        return self.namespace["context"]
        
    
    
