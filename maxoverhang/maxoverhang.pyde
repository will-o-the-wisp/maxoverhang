holding = -1
mp = False
relX=0
relY=0
comdisplay = False
forcedisplay = False
add = False
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
        cx=self.x+self.w/2.0
        cy=self.y+self.h/2.0
    def createArrow(self,cx,cy):
        arrow = createShape(GROUP)
        head = createShape(TRIANGLE, cx-10, cy-20, cx+10, cy-20, cx, cy-30)
        head.setFill(color(0))
        body = createShape(RECT, cx-5, cy, 7, 20)
        body.setFill(color(0))
        arrow.addChild(body)
        arrow.addChild(head)
            
    def display(self):
        fill(255)
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

blocks = [Block(50,50,100,200,0,0),Block(200,50,100,200,0,0)]
block1=blocks[0]
#block2=blocks[1]
block3=Block(400,50,200,100,0,0)


def setup():
    size(1000,800)
    background(190)

def draw():
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
        
        xcom/=(1.0*len(blocks))
        ycom/=(1.0*len(blocks))
        fill(255,0,0)
        ellipse(xcom,ycom,10,10)
    for b in blocks:
            xcom+=b.x+b.w/2.0
            ycom+=b.y+b.h/2.0
            b.createArrow(xcom, ycom)    
    if(add):
        blocks.append(Block(mouseX-100,mouseY-50,100,200,0,0))
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
