# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:07:09 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True :
    x,y,z = mc.player.getTilePos()
    mc.postToChat("you are located on X:"+str(x)+" Y:"+str(y)+" Z:"+str(z) )