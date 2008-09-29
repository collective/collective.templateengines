Introduction
=================

Python Template Engines is an pluggable template language backend manager for Python. 
It defines generic interfaces which you can use to communicate with any template language.

Template Backend helps you to achieve

* Easy, pluggable, template language switching

* Clean your codebase from template language dependencies

Features
--------

* EGG deployment and easy install support (PyPi repository)

* Interfaces defined using standard ``Zope interfaces <http://wiki.zope.org/Interfaces/FrontPage>``_ package

* Secure context support (Zope, Plone)

* Backends for: ``Django template Language <http://docs.djangoproject.com/en/dev/topics/templates/>``_, ``Cheetah <http://www.cheetahtemplate.org/>``_

* Unit test suite

Usage
-----

The following example shows how one can switch between Django templates and Cheetah.


TODO
----

* Generic mechanism to register template tags

Problems
--------

* Cheetah architecture lacks separate exposed compiling and evaluating phases

* Cheetah exposes the full Python namespace to templates by default, making it hard to secure it

Examples
--------

Python Template Engines is used in 

* Easy Template product for Plone.

