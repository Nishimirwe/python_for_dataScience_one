# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:42:48 2021

@author: Jean Paul Nishimirwe
"""
class Color:
    def __init__(self, r,g,b):
        self.r=r
        self.g=g
        self.b=b
        
    def getRColor(self):
        return self.r
    
    def getGColor(self):
        return self.g
    
    def getBColor(self):
        return self.b
    
    def setBColor(self,c):
        self.r=c
    
    def setGColor(self,c):
        return self.g
    
    def setGColor(self,c):
        self.g=c
        
    def getWholeColor(self):
        return (self.r,self.g,self.b)
    
    def __str__(self):
        return f"I am a color having {self.getWholeColor()} color combination"
def main():
    color=Color(255,0,0)
    color.setGColor(100)
    print(color.getRColor(), color.getWholeColor())
    
if __name__ == '__main__':
    main()
