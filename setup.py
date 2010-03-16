import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.3.4'

setup(name='collective.templateengines',
      version=version,
      description="Template engine abstraction layer for Python",
      long_description=open("README.txt").read() + read('docs', 'HISTORY.txt'),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        
        ],
      keywords='template templates engine python interface zope cheetah django backend utils generic',
      author='Mikko Ohtamaa',
      author_email='mikko.ohtamaa@twinapex.com',
      url='http://www.twinapex.com/for-developers/open-source/for-plone/easy-template',
      license='License :: OSI Approved :: BSD License',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',          
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
