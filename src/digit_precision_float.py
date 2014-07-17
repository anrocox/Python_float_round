#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to define the number of decimal digits of a float in Python?

¿Cómo definir la cantidad de digitos decimales de un float en Python?
'''

#crate a float number
f = 13.9497389867
print(f)

#this method rounded to the number of digits defined after the decimal point.
print(round(f, 2))

#define 4 digits of precision
print(round(f, 4))
