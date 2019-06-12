holding = -1
mp = False
relX=0
relY=0
comdisplay = False
forcedisplay = False
add = False
checkbal = False
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
        cx=self.x+self.w/2.0
        cy=self.y+self.h/2.0
            
    def display(self):
        fill(255)
        if(self.touchRect(0,600,500,50) or touching[blocks.index(self)]):
            fill(255,0,0)
        rect(self.x,self.y,self.w,self.h)
        cx=self.x+self.w/2.0
        cy=self.y+self.h/2.0
        if(comdisplay):
            fill(0)
            ellipse(cx,cy,10,10)
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

blocks = [Block(50,50,200,100,0.00,-.00),Block(400,50,80,50,-0.00,0)]
touching = [False,False]
block1=blocks[0]
#block2=blocks[1]
block3=Block(400,50,200,100,0,0)

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
    xcom/=(1.0*len(blocks))
    ycom/=(1.0*len(blocks))
    
    if(xcom>500):
        textSize(40)
        text("fail",500,500)
    if(comdisplay):
        xcom = 0
        ycom = 0        
        for b in blocks:
            xcom+=b.x+b.w/2.0
            ycom+=b.y+b.h/2.0
            arrow = createShape(GROUP)
            head = createShape(TRIANGLE, xcom-10, ycom-20, xcom+10, ycom-20, xcom, ycom-30)
            head.setFill(color(0))
            body = createShape(RECT, xcom-5, ycom, 7, 20)
            body.setFill(color(0))
            arrow.addChild(body)
            arrow.addChild(head)
            shape(arrow)
        xcom/=(1.0*len(blocks))
        ycom/=(1.0*len(blocks))
        fill(255,0,0)
        ellipse(xcom,ycom,10,10)
    if(add):
        blocks.append(Block(mouseX-100,mouseY-50,200,100,0,0))
        touching.append(False)
        add = False
    for i in range(len(touching)):
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
                """if bli.y+bli.h>blj.y:
                    blj.y=bli.y+bli.h
                if blj.y+blj.h>bli.y:
                    blj.y=bli.y-blj.h"""
               # if blj.x+blj.w>bli.x:
                #    blj.x=bli.x-blj.w
                

def keyPressed():
    global comdisplay
    global add
    global checkbal
    if(key=='c'):
        comdisplay = True
    if(key=='a'):
        add = True

    if(key=='g'):
        checkbal = True

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
