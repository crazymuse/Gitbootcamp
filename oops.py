#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:52:32 2018

@author: jaley
"""
 
class Dog(object):
    # 2 Underscores 
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print (sam.breed)

class Animal(object):
    def __init__(self,name):
        self.name = name
        print (self.name + " created")

    def whoAmI(self): print ("Animal")

    def eat(self): print ("Eating")

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        #Animal.__init__(self,name)
        print (self.name + " object created")
        self.name = "Lab"

    def whoAmI(self): print (self.name)

    def bark(self): print ("Woof!")
tommyObject = Dog("tommy") # Creating the class instancce
germanShepherdObject = Dog("gs") # Creating the class instancce

