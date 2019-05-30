holding = False
mp = False
relX=0
relY=0
class Block:
    def __init__(self,x,y,h,w):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.vx=0
        self.vy=0
        self.ax=0
        self.ay=0
    def display(self):
        rect(self.x,self.y,self.w,self.h)
    def inBlock(self,x,y):
        return (x>=self.x and x<=self.x+self.w and y>=self.y and y<=self.y+self.h)
    def setpos(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        
    
block1 = Block(50,50,100,50)
def setup():
    size(1000,800)
    size(1000,700)


def draw():
    global holding
    global relX
    global relY
    global mp
    background(255)
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
