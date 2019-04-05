import pygame #This imports pygame into the code
pygame.init() #intitiates pygame

screenheight = 480 #sets the screen height
screenwidth = 500 #sets the screen width

clock = pygame.time.Clock() 
score = 0

win = pygame.display.set_mode((500,480)) #displays the screen height and width

walkRight = [pygame.image.load('resources/character/R1.png'), #all of this is the character's images 
    pygame.image.load('resources/character/R2.png'),
    pygame.image.load('resources/character/R3.png'),
    pygame.image.load('resources/character/R4.png'),
    pygame.image.load('resources/character/R5.png'),
    pygame.image.load('resources/character/R6.png'),
    pygame.image.load('resources/character/R7.png'),
    pygame.image.load('resources/character/R8.png'),
    pygame.image.load('resources/character/R9.png')]
walkLeft = [pygame.image.load('resources/character/L1.png'),
       pygame.image.load('resources/character/L2.png'),
       pygame.image.load('resources/character/L3.png'),
       pygame.image.load('resources/character/L4.png'),
       pygame.image.load('resources/character/L5.png'),
       pygame.image.load('resources/character/L6.png'),
       pygame.image.load('resources/character/L7.png'),
       pygame.image.load('resources/character/L8.png'),
       pygame.image.load('resources/character/L9.png')]
bg = pygame.image.load('resources/bg.jpg') #this is the background
char = pygame.image.load('resources/character/standing.png') #the character standing

class player(object): #this is makikng the player class
     def __init__(self, x, y, width, height): #this initiates the class player
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
         self.standing = True
         self.hitbox = (self.x + 17, self.y + 11, 29, 52)

     def draw(self,win): #defines the characters walking pattern
          if self.walkCount + 1 >=27:
               self.walkCount = 0

          if not(self.standing):
               if self.left:
                    win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1
               elif self.right:
                    win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                    self.walkCount +=1
          else:
               if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
               else:
                    win.blit(walkLeft[0], (self.x, self.y))
                    self.hitbox = (self.x + 17, self.y + 11, 29, 52)
       
               
class enemy(object): #makes the class enemy
    i = 0 #defines i
    numberOfImages = 11 
    walkLeft = []
    walkRight = []
    directoryName = 'enemy'

    
    while(i < numberOfImages):
         i += 1
         walkLeftElement = "resources/" + directoryName + "/L" + str(i) +  ".png"
         walkRightElement = "resources/" + directoryName + "/R" + str(i) +  ".png"
         walkLeft.append(pygame.image.load(walkLeftElement))
         walkRight.append(pygame.image.load(walkRightElement))
               
        
  
    def __init__(self, x, y, width, height, end, numberOfImages, directoryName): #intitiiates the class player
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.end = end
         self.path = [self.x, self.end]
         self.walkCount =  0
         self.vel = 3
         self.hitbox = (self.x + 17, self.y + 2, 31, 57)
         self.health = 10
         self.visible = True
         self.numberOfImages = numberOfImages

    def draw(self,win): #definies the enemy's walk pattern
        self.move()
        if self.visible:
            if self.walkCount + 1 >= numberOfImages * 3:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win,(255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #all of this makes the hitbox for the enemy
            pygame.draw.rect(win,(0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
              

    def move(self): #defining the way the enemy moves
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            self.hitbox = (self.x + 0, self.y + 0, 0, 0)

class enemy2(object):
  
    def __init__(self, x, y, width, height, end, numberOfImages, directoryName):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.end = end
         self.path = [self.x, self.end]
         self.walkCount =  0
         self.vel = 3
         i = 0
         numberOfImages = 11
         self.walkLeft = []
         self.walkRight = []
         directoryName = 'enemy2'
         while(i < numberOfImages):
              i += 1
              walkLeftElement = "resources/" + directoryName + "/L" + str(i) + ".png"
              walkRightElement = "resources/" + directoryName + "/R" + str(i) +  ".png"
              walkLeft.append(pygame.image.load(walkLeftElement))
              walkRight.append(pygame.image.load(walkRightElement))
         

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win,(255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win,(0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
              

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            self.hitbox = (self.x + 0, self.y + 0, 0, 0)

class projectile(object): #this initiates the projectile class
   def __init__(self,x,y,radius,color,facing):
     self.x = x
     self.y = y
     self.radius = radius
     
     self.facing = facing
     self.color = color
     self.vel = 8 * facing
     
   def draw(self,win):
     pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#print("hello game")
def redrawGameWindow(): #this defines the game window
    #global walkCount
    win.blit(bg,(0,0))
    man.draw(win)
    mike.draw(win)
    goblin.draw(win)
    for bullet in bullets:
       bullet.draw(win)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))

    win.blit(text, (390,10))

    pygame.display.update()

#Main Loop
font = pygame.font.SysFont("comicsans", 30, True)
man = player(300, 410, 64, 64)
mike = enemy2(100, 410, 64, 64, 450, 11, 'enemy')
goblin = enemy(100, 410, 64, 64, 450, 11, 'enemy')
shootLoop = 0
run = True
bullets = []
while run:
    clock.tick(27)
    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:       
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets)< 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2),6,(0,0,0),facing))

        shootLoop = 1
    
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < (screenwidth - (man.width - man.vel)):
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        #man.left = False
        #man.right = False
        man.walkCount = 0
        man.standing = True
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount>=-10:
            neg = 1
            if man.jumpCount< 0:
                neg = -1
            man.y-=(man.jumpCount**2)*0.5*neg
            man.jumpCount-=1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()
     
pygame.quit()
 
     

