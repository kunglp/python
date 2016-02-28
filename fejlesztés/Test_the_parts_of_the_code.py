# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:04:40 2016

Test the tiles of the code

@author: Tapsi
"""

import Landscape

L = Landscape.Landscape(10,10)

print L.Is_On_Fire
L.init_Fire([(2,2)])
print L.Is_On_Fire
for i in range(20):
    L.One_step()
    print L.Is_On_Fire
    raw_input('Next Step?')

print "The fuel in the terrain:"
print L.Terrain_Fuel