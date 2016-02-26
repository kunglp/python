# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:18:53 2016

A class that contains the map and handles the fire activity


@author: Tapsi
"""
import numpy as np


class Landscape:
    
    On_Fire_List = set([])
    Fire_Neighbours = set([])    
    Burnt_Down = set([])
    
    def __init__(self, Size_X, Size_Y):
        
        """ TODO: On the long run the map should be loaded from an image file """
        """ For the time being it is a homogeneus map """
        self.Terrain_Quality = np.ones((Size_X, Size_Y))
        self.Terrain_Fuel = 10*np.ones((Size_X, Size_Y))
        self.Is_On_Fire = np.zeros((Size_X, Size_Y))
               
        self.Size_X = Size_X
        self.Size_Y = Size_Y
    
    def init_Fire(self, coordinate_list):
        
        """ Method takes a list of coordinates on the map and turns the places on fire """
        """ TODO: Add error handling """
        """ The coordinates should have the form of a dictionary
            e.g. coord = {'X': 12, 'Y': 34} """        
        while coordinate_list:
            coord = coordinate_list.pop()
            self.Is_On_Fire[coord['X'], coord['Y']] = 1
            self.On_Fire_List.add(coord)
            
    def get_Fire_Neighbours(self):
        
        """ Refresh the tiles which are neighbours of fire and hence can potentially
        catch fire themselves. Do not include tiles which are on fire themselves or are
        brunt down. """
        self.Fire_Neighbours.clear()
        for On_Fire in self.On_Fire_List:
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    coord = {'X': On_Fire['X']+i,
                             'Y': On_Fire['Y']+j}
                    if not (coord in self.On_Fire_List or coord in self.Burnt_Down):
                        self.Fire_Neighbours.add(coord)
        
            
        