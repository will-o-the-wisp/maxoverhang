holding = -1
mp = False
relX=0
relY=0
comdisplay = False
forcedisplay = False
counter=0
add = False #adding blocks
sub = False #subtracting blocks
checkbal = False #checking com
bw=100 #block width
bh=50 #block height
bn=0 #block number
add = False
sub = False
checkbal = False
showfn = False
showfg = False
bw=100
bh=50
bn=0
fail = False

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
        stroke(0)
        fill(255)
        #if(self.touchRect(0,600,500,50) or touching[blocks.index(self)]):
            #fill(255,0,0)
        rect(self.x,self.y,self.w,self.h)
        cx=self.x+self.w/2.0
        cy=self.y+self.h/2.0
        if(comdisplay):
            #ellipse(cx,cy,10,10)
            drawcom(cx,cy,0)
            #textSize(18)
        #    text("x", cx-5, cy+5)
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
block3=Block(400,50,200,100,0,0)

#block3=Block(400,50,200,100,0,0)

def clear():
    global blocks
    blocks=[]


def setup():
    size(1400,800)
    background(190)

def draw():
    global showfn
    global showfg
    global touching
    global add
    global holding
    global relX
    global relY
    global mp
    global blocks
    global sub
    global bn
    global fail
    global checkbal
    background(190)
    fill(101,67,33)
    noStroke()
    rect(0,600,500,50)
    noStroke()
    rect(400,600,50,300)
    for b in blocks:
        b.move()
        b.display()
        if(showfg):
            stroke(0,255,0)
            arrow(-1,50,b.x+b.w/2.0,b.y+b.h/2.0)
    if(showfn):
        stroke(255,0,0)
        for i in range(maxstack()):
            bl=blocks[i]
            if(i==0):
                if(bl.x+bl.w<=500):
                    arrow(1,50*maxstack(),bl.x+bl.w/2.0,bl.y+b.h)
                else:
                    arrow(1,50*maxstack(),(bl.x+500)/2.0,bl.y+b.h)
            else:
                d=blocks[i-1]
                #if(b.x>=d.x):
                arrow(1,50*maxstack()-50*(i),(bl.x+d.x+bw)/2.0,bl.y+b.h)
                #else:
                   # arrow(1,50*maxstack()-50*(i),,b.y+b.h)
            
    if holding > -1:
        blocks[holding].setpos(mouseX-relX,blocks[holding].y)
        if not mp:
            holding = -1
    for b in blocks:
        if mp and b.inBlock(mouseX,mouseY) and holding==-1:
            checkbal = False
            holding = blocks.index(b)
            relX=mouseX-b.x
            relY=mouseY-b.y
    xcom = 0
    ycom = 0
    for b in blocks:
        counter = b.x - 400
    for b in blocks:
        xcom+=b.x+b.w/2.0
        ycom+=b.y+b.h/2.0
    if(len(blocks)>0):
        xcom/=(1.0*len(blocks))
        ycom/=(1.0*len(blocks))
    #if(xcom>500):
    #    if(len(blocks)==3):
    #        print(calcxcom(0,len(blocks)),blocks[0].x+100,blocks[1].x+100,blocks[2].x+100)
    if(calcxcom(0,len(blocks))>500):
        fail = True
        if(comdisplay):
            textSize(40)
            fill(0)
            text("total com fail",1100,100)
    for i in range(1,len(blocks)):
        b=blocks[i]
        if(calcxcom(i,len(blocks))<blocks[i-1].x  or calcxcom(i,len(blocks))>blocks[i-1].x+bw):
            fail = True
            if(comdisplay):
                textSize(40)
                fill(0)
                text("substack com fail",1000,500)
    maxx=400
    for b in blocks:
        if(b.x>maxx):
            maxx=b.x
    fill(255,0,0)
    #line(maxx,0,maxx,height)
    textSize(40)
    fill(0)
    if(len(blocks)>0):
        text(str(maxx-400)+"/"+str(int(harmSum(len(blocks))*bw)),1200,750)
    stroke(0);
    line(harmSum(len(blocks))*bw+500,0,harmSum(len(blocks))*bw+500,height)
    if(len(blocks)>0):
        #maxx=blocks[0].x
        if(blocks[0].x+b.w/2.0>500):
            fail = True
            if(comdisplay):
                textSize(40)
                fill(0)
                text("substack com fail",1000, 500)
    #print(fail,checkbal,maxx-400,int(harmSum(len(blocks))*bw)*0.95)
    if(len(blocks)>0 and checkbal==True):
        if(fail == False):
            if(maxx-400>=int(harmSum(len(blocks))*bw)*0.95):
                textSize(40)
                fill(0)
                text("You win!",800,750)
            else:
                text("You aren't close enough!",600,750)
        else:
            text("The stack is unstable!", 600, 750)
    fail = False
    if(comdisplay):
        xcom = 0
        ycom = 0        
        for b in blocks:
            xcom+=b.x+b.w/2.0
            ycom+=b.y+b.h/2.0
        xcom/=(1.0*len(blocks))
        ycom/=(1.0*len(blocks))
        fill(255,0,0)
        drawcom(xcom,ycom,120)
       # textSize(18)
       # fill(255)
        #text("x", xcom-5, ycom+5)
        #ellipse(calcxcom(0,len(blocks)),calcycom(0,len(blocks)),10,10)
        #fill(0,255,0)
        #for i in range(1,len(blocks)):
        #    ellipse(calcxcom(i,len(blocks)),calcycom(i,len(blocks)),15,15)
    if(add):
        checkbal = False
        bn+=1
        clear()
        for i in range(bn):
            blocks.append(Block(400,600-(i+1)*bh,bw,bh,0,0))
        add = False
    if(sub):
        checkbal = False
        bn-=1
        clear()
        for i in range(bn):
            blocks.append(Block(400,600-(i+1)*bh,bw,bh,0,0))
        sub = False
    textSize(40)
    fill(0)

def harmSum(n):
    sum=0.0
    for i in range(n):
        sum+=1/(2.0*(i+1))
    return sum

def arrow(o,l,x,y):
    line(x,y,x,y-l*o)
    line(x,y-l*o,x+10,(y-l*o)+o*20)
    line(x,y-l*o,x-10,(y-l*o)+o*20)
def calcxcom(m,n):
    xcom = 0
    for i in range(m,n):
        xcom+=blocks[i].x+blocks[i].w/2.0
    if(n-m>0):
        xcom/=(1.0*(n-m))
    return xcom
def calcycom(m,n):
    ycom = 0
    for i in range(m,n):
        ycom+=blocks[i].y+blocks[i].h/2.0
    if(n-m>0):
        ycom/=(1.0*(n-m))
    return ycom

def drawcom(x,y,c):
    fill(255)
    arc(x, y, 14, 14, 0, PI/2.0, PIE)
    fill(c)
    arc(x, y, 14, 14, PI/2.0, PI, PIE)
    fill(255)
    arc(x, y, 14, 14, PI, PI*1.5, PIE)
    fill(c)
    arc(x, y, 14, 14, PI*1.5, 2*PI, PIE)

def maxstack():
    ans = 1
    if(len(blocks)==0 or blocks[0].x > 500):
        return 0
    for i in range(1,len(blocks)):
        if((blocks[i].x>=blocks[i-1].x and blocks[i].x<=blocks[i-1].x+bw) or (blocks[i].x+bw>=blocks[i-1].x and blocks[i].x+bw<=blocks[i-1].x+bw)):
            ans+=1
        else:
            return ans
    return ans
def keyPressed():
    global comdisplay
    global add
    global checkbal
    global sub
    global showfg
    global showfn
    if(key=='c' and comdisplay == False):
        comdisplay = True
    if(key=='v' and comdisplay == True):
        comdisplay = False
    if(key=='a' and len(blocks)<12):
        add = True
    if(key == 'l' and comdisplay == False):
        checkbal = True
    if(key=='s' and len(blocks)>0):
        sub = True
    if(key=='g' and showfg == False):
        showfg = True
    if(key=='h' and showfg == True):
        showfg = False
    if(key=='n' and showfn == False):
        showfn = True
    if(key=='m' and showfn == True):
        showfn = False
        
def keyReleased():
    pass
def mousePressed():
    global mp
    mp = True
def mouseReleased():
    global mp
    mp = False
