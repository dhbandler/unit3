#Daniel Bandler
#3/2/18
#wallpaper.py makes a wallpaper


from ggame import *


black = Color(0x000000, 1)
red = Color(0xff0000, 1)
blue = Colot(0x0000ff, 1)
white = Color(0xffffff, 1)

redRectangle = RectangleAsset(1.14, .0769, blackOutline, red)


for i in range(12):   #putting a row of dots
    for j in range(12):
       Sprite(dot, (10+(radius*2+10)*i,10+(radius*2+10)*j)) 
       
App().run()
