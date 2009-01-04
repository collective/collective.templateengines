"""

    Jinja2 and Zope 2 security bridges
    
    Unit tests for this code are available in collective.easytemplate product.
    
    TODO: This security implementation is not verified!

"""

__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__copyright__ = "2008 Red Innovation Oy"
__license__ = "3-Clause BSD"

from jinja2.sandbox import SandboxedEnvironment, SecurityError

from AccessControl import ZopeGuards
from zExceptions import Unauthorized
from jinja2 import Environment, StrictUndefined

class ZopeSandbox(SandboxedEnvironment):
    """ Use Zope 2 AccessCotnrol mechanism to check whether attributes are accessible from Jinja """
    
    def is_safe_attribute(self, obj, attr, value):
        # See ZopeGuards.py / guarded_hasattr
                
        try:
            ZopeGuards.guarded_getattr(obj, attr)
            return True
        except Unauthorized, e:
            raise e # Plone has its own magic for Unauthorized exceptions
            #raise SecurityError("Zope does allow access to %s on object %s: %s" % (str(attr), str(obj), str(e)))
        
    def getattr(self, obj, attribute):
        """Subscribe an object from sandboxed code and prefer the
        attribute.  The attribute passed *must* be a bytestring.
        """
        try:
            value = getattr(obj, attribute)
        except AttributeError:
            try:
                return obj[attribute]
            except (TypeError, LookupError):
                pass
        else:
            if self.is_safe_attribute(obj, attribute, value):
                return value
            return self.unsafe_undefined(obj, attribute)
        return self.undefined(obj=obj, name=attribute)
        
    def call(__self, __context, __obj, *args, **kwargs):
        """ Use Zope guarded apply to call the object."""
        # the double prefixes are to avoid double keyword argument
        # errors when proxying the call.
        if not __self.is_safe_callable(__obj):
            raise SecurityError('%r is not safely callable' % (__obj,))
        
        return ZopeGuards.guarded_apply(__obj, *args, **kwargs)
    

    
    @staticmethod
    def getEnvironment():
        return ZopeSandbox(undefined=StrictUndefined)
    
    