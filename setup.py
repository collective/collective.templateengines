from setuptools import setup, find_packages
import os

version = '0.3.0'

setup(name='collective.templateengines',
      version=version,
      description="Generic interface for Python template engines",
      long_description=open("README.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        
        ],
      keywords='template templates engine python interface zope cheetah django backend utils generic',
      author='Mikko Ohtamaa',
      author_email='mikko.ohtamaa@twinapex.com',
      url='http://pypi.python.org/pypi?%3Aaction=pkg_edit&name=collective.templateengines',
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
