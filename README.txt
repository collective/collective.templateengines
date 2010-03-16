.. contents:: :depth: 2

collective.templateengines  is an template engine abstraction layer for Python. 
It defines generic Zope interfaces for communicating with various Python template engines 
to achieve higher code reuse value.

This package is still much in development. All contributions and comments are welcome.

Features
--------

collective.templateengines helps you to achieve

* Easy, pluggable, template language switching. Write template tag code only once and use it across all template engines
  using abstracted tag plug-ings

* Clean your codebase from template engine dependencies

* Generic error and warning reporting mechanism across template engines

* EGG deployment and easy_install support from PyPi repository

* Interfaces defined using standard `Zope interfaces <http://wiki.zope.org/Interfaces/FrontPage>`_ package

* Backends for Django template Language, Cheetah and Jinja2

* Unit tests


Motivation
----------

All template engines have their shortcomings. Sooner or later you want to try yet another engine,
or someone else wants to use another template engine within your project. This package
is aimed to make that transition as smooth as possible.

Installation
------------

- Install collective.templateengines egg

- Install any of following template engine eggs: Django, Jinja2, Cheetah

Usage
-----

Please take a look on `collective.easytemplate <http://plone.org/products/easy-template>`_ package how to support switching
between template engines and registering tags for them.

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
  template, syntax_errors = engine.loadString("Show variable {{ foo }}", False)
  result, evaluation_errors = template.evaluate(context)
  
  
Tags
----

collective.templateengine uses term tag to refer to functions which you can use in the template engine context. 
In the future tags are indended to be expanded to cover template language structures as well.

collective.templateengines does not come with any tags out of the box. To define tags, I recommend
you to take a look on collective.easytemplate package.

- Tags provide collective.templateengines.interfaces.ITag interface

- Tags are registered to the template engine using Engine.addTag() function.


Problems
--------

* Cheetah architecture lacks separate exposed compiling and evaluating phases

* Cheetah exposes the full Python namespace to templates by default, making it hard to secure it

* Cheetah cannot traverse Zope functions or attributes

Examples
--------

Python Template Engines is used in 

* `Easy Template product <http://plone.org/products/easy-template>`_ for Plone.

Links
-----

`Jinja2 template engines <http://jinja.pocoo.org/2/>`_

`Django templates <http://docs.djangoproject.com/en/dev/ref/templates/>`_

`Cheetah template engine <http://www.cheetahtemplate.org/>`_

Source code
-----------

* https://svn.plone.org/svn/collective/collective.templateengines/trunk

Authors
-------

`mFabrik Research Oy <mailto:info@mfabrik.com>`_ - Python and Plone professionals for hire.

* `mFabrik web site <http://mfabrik.com>`_ 

* `mFabrik mobile site <http://mfabrik.mobi>`_ 

* `Blog <http://blog.mfabrik.com>`_

* `More about Plone <http://mfabrik.com/technology/technologies/content-management-cms/plone>`_ 


