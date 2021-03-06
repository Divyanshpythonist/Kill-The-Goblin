import pygame
pygame.init()

screenwidth=480

win= pygame.display.set_mode((screenwidth,screenwidth))
caption=pygame.display.set_caption("Character Animation & Projectiles")

walkRight=[pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png'),]
bg=pygame.image.load('bg.jpg')

clock=pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing=True

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if character.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))

class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
        self.x=x
        self.y=y
        self.vel=10*facing
        self.radius=radius
        self.colour=colour
        self.facing=facing

    def draw(self,win):
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.radius)

def redrawGameWindow():
    win.blit(bg,(0,0))
    character.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run=True
character=player(200,415,64,64)
bullets=[]
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for bullet in bullets:
        if bullet.x < screenwidth and bullet.x>0 :
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if character.left:
            facing=-1
        else:
            facing=1
        if len(bullets) < 5:
            bullets.append(projectile(round(character.x+character.width//2),round(character.y+character.height//2),4,(255,0,0),facing) )

    if keys[pygame.K_LEFT] and character.x>character.vel:
        character.x-=character.vel
        character.left=True
        character.right=False
        character.standing=False
    elif keys[pygame.K_RIGHT] and character.x<screenwidth-character.width-character.vel:
        character.x+=character.vel
        character.left=False
        character.right=True
        character.standing=False
    else:
        character.standing=False
        character.walkCount=0
    if not(character.isJump):
        if keys[pygame.K_UP]:
            character.isJump=True
            character.right=False
            character.left=False
            character.walkCount=0
    else:
        if character.jumpCount >= -10:
            neg = 1
            if character.jumpCount < 0:
                neg = -1
            character.y -= (character.jumpCount ** 2) * 0.5 * neg
            character.jumpCount-=1
        else:
            character.isJump = False
            character.jumpCount = 10

    redrawGameWindow()

pygame.quit()