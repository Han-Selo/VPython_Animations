from vpython import *
import time

mRadius=1
wallThickness=.5
roomWidth=15
roomDepth=10
roomHeight=10

roomFloor=box(pos=vector(0, -roomHeight/2, 0), color=color.white, size=vector(roomWidth,wallThickness,roomDepth))

ceiling=box(pos=vector(0, roomHeight/2, 0), color=color.white, size=vector(roomWidth,wallThickness,roomDepth))

sidewallLeft=box(pos=vector(-roomWidth/2, 0, 0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))

sidewallRight=box(pos=vector(roomWidth/2, 0, 0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))

backwall=box(pos=vector(0, 0, -roomDepth/2), color=color.white, size=vector(roomWidth,roomHeight,wallThickness))

marble=sphere(pos=vector(0,0,0), color=color.blue, radius=mRadius)
deltaX = .1
deltaY = .1
deltaZ = .1
xPos=0
yPos=0
zPos=0

while True:
    rate(25)
    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ
    Xrme = xPos + mRadius
    Xlme = xPos - mRadius
    Ytme = yPos + mRadius
    Ybme = yPos - mRadius
    Zbme = zPos - mRadius
    Zfme = zPos + mRadius

    Rwe = roomWidth/2-wallThickness/2
    Lwe = -roomWidth/2+wallThickness/2
    Ce=roomHeight/2-wallThickness/2
    Flwe=-roomHeight/2+wallThickness/2
    Fwe=roomDepth/2-wallThickness/2
    Bwe=-roomDepth/2+wallThickness/2

    if (Xrme >= Rwe or Xlme <= Lwe):
        deltaX = deltaX*(-1)




    if (Ytme >= Ce or Ybme <= Flwe):
        deltaY = deltaY*(-1)



    if (Zfme >= Fwe or Zbme <= Bwe):

        deltaZ = deltaZ*(-1)


    
    marble.pos=vector(xPos, yPos, zPos)
