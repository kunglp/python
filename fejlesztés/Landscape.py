# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:18:53 2016

A class that contains the map and handles the fire activity


@author: Tapsi
"""
import numpy as np
from sets import Set


class Landscape:
    
    On_Fire_List = Set([])    
    
    def __init__(self, sizeX, sizeY):
        
        """ TODO: On the long run the map should be loaded from an image file """
        """ For the time being it is a homogeneus map """
        self.Terrain_Quality = np.ones((sizeX, sizeY))
        self.Terrain_Fuel = 10*np.ones((sizeX, sizeY))
        self.Is_On_Fire = np.zeros((sizeX, sizeY))
        self.Burnt_Down = np.zeros((sizeX, sizeY))
        
        self.sizeX = sizeX
        self.sizeY = sizeY
    
    def init_Fire(self, coordinate_list):
        
        """ Method takes a list of coordinates on the map and turns the places on fire """
        """ TODO: Add error handling """        
        while coordinate_list:
            coord = coordinate_list.pop()
            self.Is_On_Fire[coord[0], coord[1]] = 1
            self.On_Fire_List.add(coord)
            
        