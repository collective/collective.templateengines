"""

    Plone specific context stubs.

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__docformat__ = "epytext"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-clause BSD"

        
def getArchetypesContext(instance):
    """ Expose Archetypes object to the template language. """
        
    security=getSecurityManager()
    
    namespace = {
        "context" : instance,
        "portal_url" : getToolByName(self, 'portal_url'),
        "user" : security.getUser(),
        "request" : self.REQUEST
    }
        
    return namespace
