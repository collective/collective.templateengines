Introduction
============

collective.templateengines  is an pluggable template language backend manager for Python. 
It defines generic interfaces which abstracts template language basic interfaction.

Template Backend helps you to achieve

* Easy, pluggable, template language switching

* Clean your codebase from template language dependencies

* Interface for getting objectized error and debug output from the template engine

Motivation
----------

All template engines have their shortcomings. Sooner or later you want to try yet another of them,
or someone else wants to use another template engine with your project. This product
is aimed to make that transition as smooth as possible, maybe just one line change.

Features
--------

* EGG deployment and easy install support (PyPi repository)

* Interfaces defined using standard `Zope interfaces <http://wiki.zope.org/Interfaces/FrontPage>`_ package

* Backends for: `Django template Language <http://docs.djangoproject.com/en/dev/topics/templates/>`_, `Cheetah <http://www.cheetahtemplate.org/>`_

* Unit test suite

Usage
-----

The following example shows how one can switch between Django and Cheetah template engines with one line of change.
Naturally, the templates themselves need to be refactored.

Cheetah::

  from collective.templateengines.backends import cheetah

  engine = cheetah.Engine()
  context = DictionaryContext({"foo":"bar"})
  template, syntax_errors = engine.loadString("Show variable $foo", False)
  result, evaluation_errors = template.evaluate(context)
  
Django::

  from collective.templateengines.backends import djangotemplates

  engine = djangotemplates.Engine()
  context = DictionaryContext({"foo":"bar"})
  template, syntax_errors = engine.loadString("Show variable {{ foo", False)
  result, evaluation_errors = template.evaluate(context)


TODO
----

* Generic mechanism to register template tags

* Secure context support (Zope, Plone)

Problems
--------

* Cheetah architecture lacks separate exposed compiling and evaluating phases

* Cheetah exposes the full Python namespace to templates by default, making it hard to secure it

* Cheetah cannot traverse Zope functions or attributes

Examples
--------

Python Template Engines is used in 

* `Easy Template product <http://plone.org/products/easy-template>`_ for Plone.

Author
------

Mikko Ohtamaa

`Red Innovation Oy, Oulu, Finland <http://www.redinnovation.com>`_ - High quality Python hackers for hire





