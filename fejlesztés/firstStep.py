# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import time
import random
import pygame.locals as lcl
 
 
class Fire(object):
    x = 150
    y = 150
    spread = 30
    
    def moveRight(self):
        self.x = self.x + self.spread
        
    def moveLeft(self):
        self.x = self.x - self.spread
        
    def moveUp(self):
        self.y = self.y - self.spread
        
    def moveDown(self):
        self.y = self.y + self.spread
         
             
  
 
class App(object):

    
        
    
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.Fire = Fire()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._image_surf = pygame.image.load("fire.png").convert()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.blit(self._image_surf,(self.Fire.x,self.Fire.y))
        pygame.display.flip()
        
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            keys = pygame.key.get_pressed() 
            if (keys[lcl.K_ESCAPE]):
                self._running = False
            time.sleep(0.1)
            rand = random.randint(0,3)
            if(rand==0):
                self.Fire.moveDown()
            if(rand==1):
                self.Fire.moveUp()
            if(rand==2):
                self.Fire.moveRight()
            if(rand==3):
                self.Fire.moveLeft()
            
            
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
        
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
