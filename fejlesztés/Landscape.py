# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:18:53 2016

A class that contains the map and handles the fire activity


@author: Tapsi
"""
import numpy as np


class Landscape(object):
    
    On_Fire_List = set([])
    Fire_Neighbours = set([])    
    Burnt_Down = set([])
    alpha = .4 # A factor to adjust the burning probability
    
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
        """ The coordinates should have the form of a tuple
               e.g. coord = (1,1), the x-coord is coord[0]
               and the y-coord is coord[1]"""        
        while coordinate_list:
            coord = coordinate_list.pop()
            self.Is_On_Fire[coord[0], coord[1]] = 1
            self.On_Fire_List.add(coord)
            
    def get_Fire_Neighbours(self):
        
        """ Refresh the tiles which are neighbours of fire and hence can potentially
        catch fire themselves. Do not include tiles which are on fire themselves or are
        brunt down. """
        self.Fire_Neighbours.clear()
        for On_Fire in self.On_Fire_List:
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    coord = (On_Fire[0]+i,
                             On_Fire[1]+j)
                    if (coord[0]>-1 and coord[0]<self.Size_X):
                        if (coord[1]>-1 and coord[1]<self.Size_Y):
                            if not (coord in self.On_Fire_List or coord in self.Burnt_Down):
                                self.Fire_Neighbours.add(coord)
                                
    def P_catch_fire(self, tile_coord):
        
        """ The function calculates the probability rate of a tile to catch fire in
        a time step.
        TODO: For the time being the formula is very ad-hoc. There should be a better found
        """
        
        N_burning_neighbours = 0.
        for i in [ -1, 0, 1]:
            for j in [ -1, 0, 1]:
                coord = (tile_coord[0]+i,
                         tile_coord[1]+j)
                if coord in self.On_Fire_List:
                    N_burning_neighbours +=1
        return 1. - np.exp(-self.alpha*N_burning_neighbours)
        
    def One_step(self):
        
        """ The method carries out one step of the burning landscape.
            The steps are:
                1. Neighbours of the fire can catch fire
                2. Burning tiles consume one unit of fuel
                3. Tiles, which consumed their fules cease to burn """
        
        """ Catching fire """
        self.get_Fire_Neighbours()
        for coord in self.Fire_Neighbours:
            prob = self.P_catch_fire(coord)
            p_gen = np.random.rand()
            if p_gen < prob:
                self.On_Fire_List.add(coord)
                self.Is_On_Fire[coord[0],coord[1]] = 1
        
        """ Consume fuel and mark tiles to be brunt down"""
        to_burn_down = set()
        for coord in self.On_Fire_List:
            self.Terrain_Fuel[coord[0], coord[1]] -= 1
            if self.Terrain_Fuel[coord[0], coord[1]] < 1:
                to_burn_down.add(coord)
                self.Burnt_Down.add(coord)
        
        """ Burn down """
        for coord in to_burn_down:
            self.On_Fire_List.remove(coord)
            self.Is_On_Fire[coord[0],coord[1]] = 0.
            
                    
        
        
        
    
    """ DEBUG functions """
    
    def report_On_Fire(self):
        print "The tile on fire are:"
        for coord in self.On_Fire_List:
            print coord
        print "####################"

    def report_Burnt_down(self):
        print "The brunt down tiles are:"
        for coord in self.Burnt_Down:
            print coord
        print "####################"
            
        
