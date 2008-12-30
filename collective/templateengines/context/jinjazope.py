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

class ZopeSandbox(SandboxedEnvironment):
    """ Use Zope 2 AccessCotnrol mechanism to check whether attributes are accessible from Jinja """
    
    def is_safe_attribute(self, obj, attr, value):
        # See ZopeGuards.py / guarded_hasattr
        try:
            ZopeGuards.guarded_getattr(object, name)
            return True
        except Unauthorized, e:
            raise SecurityError("Zope does allow access to %s on object %s: %s" % (str(attr), str(obj), str(e)))
    
    def is_safe_callable(self, obj):
        return self.is_safe_attribute(obj)
    
    