from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.templateengines',
      version=version,
      description="Generic interface for Python template engines",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Mikko Ohtamaa',
      author_email='mikko@redinnovation.com',
      url='',
      license='3-Clause BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.templateengines'],
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