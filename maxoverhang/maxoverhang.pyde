holding = -1
mp = False
relX=0
relY=0
comdisplay = False
forcedisplay = False
add = False
sub = False
checkbal = False
bw=100
bh=50
bn=0


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
        stroke(0)
        fill(255)
        #if(self.touchRect(0,600,500,50) or touching[blocks.index(self)]):
            #fill(255,0,0)
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
        


blocks = []
touching = [False,False]
#block1=blocks[0]
#block2=blocks[1]
#block3=Block(400,50,200,100,0,0)
def clear():
    global blocks
    blocks=[]

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
    global sub
    global bn
    background(190)
    fill(101,67,33)
    rect(0,600,500,50)
    noStroke()
    rect(400,600,50,300)
    for b in blocks:
        b.move()
        b.display()
    if holding > -1:
        blocks[holding].setpos(mouseX-relX,blocks[holding].y)
        if not mp:
            holding = -1
    for b in blocks:
        if mp and b.inBlock(mouseX,mouseY) and holding==-1:
            holding = blocks.index(b)
            relX=mouseX-b.x
            relY=mouseY-b.y
    xcom = 0
    ycom = 0
    for b in blocks:
        xcom+=b.x+b.w/2.0
        ycom+=b.y+b.h/2.0
    if(len(blocks)>0):
        xcom/=(1.0*len(blocks))
        ycom/=(1.0*len(blocks))
    if(xcom>500):
        textSize(40)
        fill(0)
        text("total com fail",1100,100)
    for i in range(1,len(blocks)):
        b=blocks[i]
        if(b.x+b.w/2.0<blocks[i-1].x  or b.x+b.w/2.0>blocks[i-1].x+bw):
            textSize(40)
            fill(0)
            text("indiv com fail "+str(i),1100,500)
    maxx=400
    if(len(blocks)>0):
        maxx=blocks[0].x
        if(blocks[0].x+b.w/2.0>500):
            textSize(40)
            fill(0)
            text("indiv com fail 0",1100, 500)
    for b in blocks:
        if(b.x>maxx):
            maxx=b.x
    textSize(40)
    fill(0)
    text(maxx-400,1200,750)
    line(harmSum(len(blocks))*bw+500,0,harmSum(len(blocks))*bw+500,height)
    if(comdisplay):
        fill(255,0,0)
        ellipse(xcom,ycom,10,10)
    if(add):
        bn+=1
        clear()
        for i in range(bn):
            blocks.append(Block(400,600-(i+1)*bh,bw,bh,0,0))
        add = False
    if(sub):
        bn-=1
        clear()
        for i in range(bn):
            blocks.append(Block(400,600-(i+1)*bh,bw,bh,0,0))
        sub = False
    """for i in range(len(touching)):
        touching[i]=False
    for i in range(len(blocks)):
        for j in filter(lambda x: x>i,range(len(blocks))):
            bli = blocks[i]
            blj = blocks[j]
            if bli.touchRect(blj.x,blj.y,blj.w,blj.h):
                touching[i]=True
                touching[j]=True
                #if bli.x+bli.w>blj.x:
                 #   bli.x=blj.x-bli.w
                
                   # if bli.y+bli.h>blj.y:
                   # blj.y=bli.y+bli.h
                if blj.y+blj.h>bli.y:
                    blj.y=bli.y-blj.
               # if blj.x+blj.w>bli.x:
                #    blj.x=bli.x-blj.w
        """
def harmSum(n):
    sum=0.0
    for i in range(n):
        sum+=1/(2.0*(i+1))
    return sum

def keyPressed():
    global comdisplay
    global add
    global checkbal
    global sub
    if(key=='c'):
        comdisplay = True
    if(key=='a'):
        add = True
    if(key=='g'):
        checkbal = True
    if(key=='s' and len(blocks)>0):
        sub = True
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
