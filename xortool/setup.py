#!/usr/bin/env python
#-*- coding:utf-8 -*-

from distutils.core import setup

import xortool

setup(name='xortool',
      version=xortool.__version__,

      author='hellman',
      author_email='hellman1908@gmail.com',
      license="MIT",

      url='https://github.com/hellman/xortool',
      description='Tool for xor cipher analysis',
      long_description=open("README.md").read(),  # not in rst, but something
      keywords="xor xortool analysis",

      packages=['xortool'],
      provides=['xortool'],
      install_requires=['docopt>=0.6.1'],
      scripts=["xortool/xortool", "xortool/xortool-xor"],

      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Information Technology',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'Topic :: Security :: Cryptography',
                   ],
      )
