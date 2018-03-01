#Daniel Bandler
#3/1/18
#dotsDemo.py - loops with graphics

from ggame import *

red = Color("0xFF0000",1)

radius = 25

dot = CircleAsset(radius, LineStyle(1,red), red)

for i in range(12):   #putting a row of dots
    for j in range(12):
       Sprite(dot, (10+(radius*2+10)*i,10+(radius*2+10)*j)) 
       
App().run()