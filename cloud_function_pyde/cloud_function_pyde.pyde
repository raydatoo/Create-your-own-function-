#-------------------------------
#Name: cloudFunction.py
#Purpose: Show basic processing stuffs like animation, text, and shapes
#Author: Datoo.R
#Created: 19/11/2018
#-------------------------------

#set animation variables
a = 0
b = 135
c = 206
d = 235


def setup():
    size(1366, 768)


def draw():
    global a
    global b
    global c
    global d
    
    #sky blue background
    background(b, c, d)
    
    #draw three clouds
    drawCloud(100 + a, 500)
    drawCloud(800 + a, 300)
    drawCloud(700 + a, 600)
    
    #animate
    a += 10
    if a>= width:
        a = 0
        b -= 20
        c -= 20
        d -= 20
    if b <= 0:
        b = 135
        c = 206
        d = 235
    
    
    
def drawCloud(x, y):
    
    #draw the cloud
    noStroke()
    fill(255)
    ellipse(x, y, 200, 50)
    ellipse(x - 25, y - 25, 100, 100)
    ellipse(x + 50, y - 25, 50, 80)
    ellipse(x + 50, y - 60, 100, 100)
    ellipse(x + 50, y, 200, 40)
    ellipse(x + 75, y - 25, 100, 80)
    
