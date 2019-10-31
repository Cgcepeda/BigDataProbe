#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:41:20 2019

@author: cristiancepeda
"""

class Polinomio:
#Se ingresan los coeficientes del polinomio de menor a mayor
#Los numeros reales se representan como un polinomio de grado cero.
  def __init__(self, coeficientes=[]):
    self.coeficientes= coeficientes[:]

  def addition(self, polynomb):
    r= [ a+b for a,b in zip(self.coeficientes, polynomb.coeficientes)]
    if len(self.coeficientes)< len(polynomb.coeficientes):
      r+= polynomb.coeficientes[len(self.coeficientes):]
    else:
      r+= self.coeficientes[len(polynomb.coeficientes):]
    return Polinomio(r)

  def substraction(self, polynomb):
    r= [ a-b for a,b in zip(self.coeficientes, polynomb.coeficientes)]
    if len(self.coeficientes)< len(polynomb.coeficientes):
      r+= [ -v for v in polynomb.coeficientes[len(self.coeficientes):]]
    else:
      r+= self.coeficientes[len(polynomb.coeficientes):]
    return Polinomio(r)

  def multiplication(self, polynomb):
    r= [0]*(len(self.coeficientes)+len(polynomb.coeficientes)-1)
    for sgrado, scoef in enumerate(self.coeficientes):
      for ogrado, ocoef in enumerate(polynomb.coeficientes):
        r[sgrado+ogrado]+= scoef*ocoef
    return Polinomio(r)

  def evaluate(self, x):
    r= 0
    for c in reversed(self.coeficientes):
      r*= x
      r+= c
    return r

  def scalarproduct(self, c):
    return Polinomio([c*coef for coef in self.coeficientes])

  def __str__(self):
    r= ""
    for grado, coeficiente in enumerate(self.coeficientes):
      if coeficiente!= 0:
        if grado== 0:
          if coeficiente> 0 and r!= "":
            r+= "+"
          r+= str(coeficiente)
        else:
          if coeficiente<0:
            if coeficiente== -1:
              r+= "-"
            else:
              r+= str(coeficiente)+"*"
          else:
            if r!= "":
              r+= "+"
            if coeficiente!= 1:
              r+= str(coeficiente)+"*"
          r+= "x"
          if grado> 1:
            r+= "^"+str(grado)
    if r== "":
      r= "0"
    return r

a=Polinomio([1,2,3])
b=Polinomio([3,4])
suma=a.addition(b)
resta=a.substraction(b)
producto=a.multiplication(b)
escalar=a.scalarproduct(2)
evaluado=a.evaluate(2)
print('Polinomio a: ', a)
print('Polinomio b: ', b)
print('a+b: ',suma)
print('a-b: ',resta)
print('a*b: ',producto)
print('a multiplicado por 2: ',escalar)
print('a evaluado en 2:',evaluado)
