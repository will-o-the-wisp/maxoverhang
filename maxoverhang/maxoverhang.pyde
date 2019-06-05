holding = False #holding block
mp = False #mousepressed, might change later
relX=0
relY=0
class Block:
    def __init__(self,x,y,h,w,ax,ay):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.vx=0
        self.vy=0
        self.ax=ax
        self.ay=ay
    def display(self):
        fill(255)
        rect(self.x,self.y,self.w,self.h)
    def inBlock(self,x,y):
        return (x>=self.x and x<=self.x+self.w and y>=self.y and y<=self.y+self.h)
    def setpos(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        self.vx+=self.ax
        self.vy+=self.ay
        self.x+=self.vx
        self.y+=self.vy
    
block1 = Block(50,50,50,100,0,0)

class Tab:
    def __init__(self, c, xpos, ypos):
        self.c = color (101,67,33)
        self.xpos = width/2
        self.ypos = height/2
    def display(self):
        fill(self.c)
        rect(xpos, ypos, 50, 100)
    
def setup():
    size(1000,800)
    background(190)

def draw():
    global holding
    global relX
    global relY
    global mp
    background (190)
    fill(101,67,33)
    rect(0,600,500,50)
    noStroke()
    rect(400,600,50,300)
    block1.move()
    block1.display()
    if holding == True:
        print(mp)
        block1.setpos(mouseX-relX,mouseY-relY)
        if mp == False:
            holding = False
    if mp and block1.inBlock(mouseX,mouseY) and not holding:
        holding = True
        relX = mouseX-block1.x
        relY=mouseY-block1.y
        #block1.setpos(mouseX,mouseY)
    print(mp,holding)

    
def mousePressed():
    global mp
    mp = True

def mouseReleased():
    global mp
    mp = False
