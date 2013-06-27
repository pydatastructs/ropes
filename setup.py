#!/usr/bin/python 
from distutils.core import setup, Extension

ropes_module=Extension('ropes',
                       sources=['src/ropes.c'])

setup(name='Ropes',
      version='1.0',
      description='A Ropes datatype for Python.',
      ext_modules=[ropes_module])

      
