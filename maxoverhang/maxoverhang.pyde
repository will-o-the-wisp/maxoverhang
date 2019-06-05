holding = -1
mp = False
relX=0
relY=0
comdisplay = False
forcedisplay = False
add = False
class Block:
    def __init__(self,x,y,w,h,ax,ay):
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
        if(self.touchRect(0,600,500,50) or touching[blocks.index(self)]):
            fill(255,0,0)
        rect(self.x,self.y,self.w,self.h)
        if(comdisplay):
            fill(0)
            ellipse(self.x+self.w/2.0,self.y+self.h/2.0,10,10)
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
    def touchRect(self,x,y,w,h):
        return (self.x+self.w>=x and self.x <= x+w and self.y + self.h >= y and self.y <= y + h)
        


blocks = [Block(50,50,200,100,0,0),Block(400,50,200,100,0,0)]
touching = [False,False]
block1=blocks[0]
#block2=blocks[1]
#block3=Block(400,50,200,100,0,0)
def setup():
    size(1400,800)
    background(190)

def draw():
    global touching
    global add
    global holding
    global relX
    global relY
    global mp
    global blocks
    global blocks2
    background(190)
    fill(101,67,33)
    rect(0,600,500,50)
    noStroke()
    rect(400,600,50,300)
    for b in blocks:
        b.move()
        b.display()
    for i in range(len(touching)):
        touching[i]=False
    for i in range(len(blocks)):
        for j in range(i+1,len(blocks)):
            blj = blocks[j]
            if blocks[i].touchRect(blj.x,blj.y,blj.w,blj.h):
                touching[i]=True
                touching[j]=True
    if holding > -1:
        blocks[holding].setpos(mouseX-relX,mouseY-relY)
        if not mp:
            holding = -1
    for b in blocks:
        if mp and b.inBlock(mouseX,mouseY) and holding==-1:
            holding = blocks.index(b)
            relX=mouseX-b.x
            relY=mouseY-b.y
    if(comdisplay):
        xcom = 0
        ycom = 0
        for b in blocks:
            xcom+=b.x+b.w/2.0
            ycom+=b.y+b.h/2.0
        xcom/=(1.0*len(blocks))
        ycom/=(1.0*len(blocks))
        fill(255,0,0)
        ellipse(xcom,ycom,10,10)
    if(add):
        blocks.append(Block(mouseX-100,mouseY-50,200,100,0,0))
        touching.append(False)
        add = False
    
def keyPressed():
    global comdisplay
    global add
    if(key=='c'):
        comdisplay = True
    if(key=='a'):
        add = True
def keyReleased():
    global comdisplay
    if(key=='c'):
        comdisplay = False

def mousePressed():
    global mp
    mp = True

def mouseReleased():
    global mp
    mp = False
