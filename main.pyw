import random, time, pygame, math, sys, os

def updateBoard(board, direction):
    global points
    stacked=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if direction=="up":
        changed=1
        while changed:
            changed=0
            for y in range(1,4,1):
                
                for x in range(0,4,1):
                    #pygame.draw.rect(screen,(0,0,0,255),(x*100+3,y*100+53,10,10))
                    #pygame.display.flip()
                    #time.sleep(0.1)
                    if (board[y-1][x]==board[y][x]!=0 and stacked[y][x]==0) or (board[y-1][x]==0 and board[y][x]!=0):
                        changed=1
                        if board[y-1][x]==board[y][x]!=0:
                            points=board[y-1][x]+points
                            stacked[y-1][x]=1
                        board[y-1][x]=board[y-1][x]+board[y][x]
                        
                        board[y][x]=0

    
    elif direction=="down":
        changed=1
        while changed:
            changed=0
            for y in range(2,-1,-1):
                for x in range(0,4,1):
                    if (board[y+1][x]==board[y][x]!=0 and stacked[y][x]==0)  or (board[y+1][x]==0 and board[y][x]!=0):
                        changed=1
                        if board[y+1][x]==board[y][x]!=0:
                            points=board[y+1][x]+points
                            stacked[y+1][x]=1
                        board[y+1][x]=board[y+1][x]+board[y][x]
                        board[y][x]=0
                        
    elif direction=="left":
        changed=1
        while changed:
            changed=0
            for y in range(3,-1,-1):
                for x in range(1,4,1):
                    if (board[y][x-1]==board[y][x]!=0 and stacked[y][x]==0)  or (board[y][x-1]==0 and board[y][x]!=0):
                        changed=1
                        if board[y][x-1]==board[y][x]!=0:
                            points=board[y][x-1]+points
                            stacked[y][x-1]=1
                        board[y][x-1]=board[y][x-1]+board[y][x]
                        board[y][x]=0
                        
    elif direction=="right":
        changed=1
        while changed:
            changed=0
            for y in range(3,-1,-1):
                for x in range(2,-1,-1):
                    if (board[y][x+1]==board[y][x]!=0 and stacked[y][x]==0)  or (board[y][x+1]==0 and board[y][x]!=0):
                        changed=1
                        if board[y][x+1]==board[y][x]!=0:
                            points=board[y][x+1]+points
                            stacked[y][x+1]=1
                        board[y][x+1]=board[y][x+1]+board[y][x]
                        board[y][x]=0
    return board
def addTile(board):
    changed=0
    if 0 not in board[0]+board[1]+board[2]+board[3]:
        changed=1
    while not changed:
        rand=random.randrange(0,4),random.randrange(0,4)
        if board[rand[0]][rand[1]]==0:
            board[rand[0]][rand[1]]=random.randrange(2,3)
            changed=1
    return board
def draw(board):
    screen.fill((220,220,220,255))
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 30, 1)
    for y in range(0,4):
        for x in range(0,4):
            text = font.render(str(board[y][x]), True, (255,255,255,255))
            point = font.render(str(points), True, (120,120,120,255))
            if board[y][x]==0:
                pygame.draw.rect(screen,(200,200,200,255),(x*100+3,y*100+53,97,97))
            else:
                pygame.draw.rect(screen,(250, 240-7*math.log(board[y][x]+1,2)%240,180-(10*math.log(board[y][x]+1,2)/4)%180,255),(x*100+3,y*100+53,97,97))
            if board[y][x]!=0:
                screen.blit(text,(x*100+51-text.get_size()[0]/2,y*100+90))
            screen.blit(point,(20,15))
            
    pygame.display.flip()
def handleKeys():
    key=0
    #print(1)
    while key==0:
        event = pygame.event.wait()
        if event.type==pygame.KEYDOWN:
            #print(event.key)
            if event.key in [97, 276]:
                key="a"
            elif event.key in [100, 275]:
                key="d"
            elif event.key in (119, 273):
                key="w"
            elif event.key in [115, 274]:
                key="s"
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    return key

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path('icon.png')
board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

addTile(board)
#print(board)
displaysize = (403,453)
pygame.display.init()
pygame.display.set_caption('2048')
a = pygame.image.load(Logo)
pygame.display.set_icon(a)
screen = pygame.display.set_mode(displaysize)
screen.fill((200,200,200,255))
pygame.event.set_blocked(pygame.MOUSEMOTION)
points=0
while 1:
    draw(board)

    direction=handleKeys()
    if direction=="w":direction="up"
    if direction=="s":direction="down"
    if direction=="a":direction="left"
    if direction=="d":direction="right"
    oldboard=str(board)
    updateBoard(board,direction)
    #print(board)
    #print(oldboard)
    if oldboard!=str(board):
        #print(1000)
        addTile(board)
    
    
