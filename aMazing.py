import pygame, sys, random

Runner_image = ["Blocky (2).jpg"]
Fireball_image = ["FireBall.png"]
boss_image = ["WizardFace.png"]
bossHat_image = ["WizardHat.png"]
pygame.mixer.init()
pygame.mixer.music.load("thomas.wav")
global room
global bosslife
global weard
#Class for Runner Sprite
class blockClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Blocky (2).jpg")
        self.rect = self.image.get_rect()
        self.rect.center = [100,425]
        
    def moveLeft(self):
        self.rect.centerx = self.rect.centerx - 3

    def moveRight(self):
        self.rect.centerx = self.rect.centerx + 3
        
    def moveUp(self,vel):
        self.rect.centery = self.rect.centery - vel/50

    def getUnder(self,screen):
        return screen.get_at((self.rect.centerx, self.rect.centery+22))

    def getLeft(self,screen):
        return screen.get_at((self.rect.centerx-27, self.rect.centery))

    def getUp(self,screen):
        if weard == block:
            return screen.get_at((self.rect.centerx, self.rect.centery-50))
        return screen.get_at((self.rect.centerx, self.rect.centery-25))

    def getRight(self,screen):
        return screen.get_at((self.rect.centerx+27, self.rect.centery))

    def getX(self):
        return self.rect.centerx

    def getY(self):
        return self.rect.centery

    def teleport(self,newX,newY):
        self.rect.center = [newX,newY]

    def hatter(self):
        return [self.rect.centerx,self.rect.centery-30]
    
#Class for Fireball Sprite
class fireballClass(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("FireBall.png")
        self.rect = self.image.get_rect()
        self.rect.center = location

    def update(self):
        self.rect.centery = self.rect.centery + 1
        if self.rect.centery > 430:
            self.kill()

class bossMan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("WizardFace.png")
        self.rect = self.image.get_rect()
        self.rect.center = [600,300]
    def hatter(self):
        return [self.rect.centerx,self.rect.centery-35]

class bossManHat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("WizardHat.png")
        self.rect = self.image.get_rect()
        self.rect.center = [200,265]
    def update(self,wearer):
        self.rect.center = wearer.hatter()

def fireWall(height):
    locations = []
    jkl = []
    for i in range(7):
        row = random.randint(0,6)
        duh = row in jkl
        while duh:
            row = row + 1
            if row >= 8:
                row = 0
            duh = row in jkl
        jkl.append(row)
        location = [row * 100 + 50, height]
        locations.append(location)
        fer = fireballClass(location)
        firewally.add(fer)

def fonters(font,size):
    return pygame.font.Font(font,size)
        
def animate(passed):
    pygame.display.flip()
    if room == 1:
        screen.fill([170,178,200])
        pygame.draw.rect(screen, [150,157,178], [0,460,798,40], 0)
        pygame.draw.rect(screen, [150,157,178], [0,0,40,500], 0)
        pygame.draw.rect(screen, [150,157,178], [0,0,798,7], 0)
        pygame.draw.rect(screen, [150,157,178], [400,200,90,90],0)
        pygame.draw.rect(screen, [150,157,179], [797,0,3,500],0)
        screen.blit(block.image, block.rect)
        if weard == block:
            screen.blit(bossHat.image, bossHat.rect)
    elif room == 2:
        screen.fill([178,200,170])
        pygame.draw.rect(screen, [150,157,178], [2,460,798,40], 0)
        pygame.draw.rect(screen, [150,157,177], [0,0,3,500],0)
        pygame.draw.rect(screen, [150,157,179], [797,0,3,500],0)
        if not passed:
            pygame.draw.rect(screen, [150,157,178], [0,0,15,500], 0)
            pygame.draw.rect(screen, [150,157,178], [785,0,15,500], 0)
        screen.blit(block.image, block.rect)
        firewally.draw(screen)
        if weard == block:
            screen.blit(bossHat.image, bossHat.rect)
    elif room == 3:
        screen.fill([200,170,178])
        pygame.draw.rect(screen, [150,157,178], [3,460,347,40], 0)
        pygame.draw.rect(screen, [150,157,178], [450,460,347,40], 0)
        pygame.draw.rect(screen, [150,157,177], [0,0,3,500],0)
        pygame.draw.rect(screen, [150,157,179], [797,0,3,500],0)
        pygame.draw.rect(screen, [249,92,34], [350,480,100,20], 0)
        screen.blit(block.image,block.rect)
        if weard == block:
            screen.blit(bossHat.image, bossHat.rect)
    elif room == 4:
        screen.fill([200,170,178])
        pygame.draw.rect(screen, [150,157,178], [3,460,147,40], 0)
        pygame.draw.rect(screen, [150,157,178], [700,460,97,40], 0)
        pygame.draw.rect(screen, [150,157,177], [0,0,3,500],0)
        pygame.draw.rect(screen, [150,157,179], [797,0,3,500],0)
        pygame.draw.rect(screen, [249,92,34], [150,480,550,20], 0)
        screen.blit(block.image,block.rect)
        if weard == block:
            screen.blit(bossHat.image, bossHat.rect)
    elif room == 5:
        screen.fill([255, 123, 37])
        pygame.draw.rect(screen, [150,157,178], [2,460,798,40], 0)
        pygame.draw.rect(screen, [150,157,177], [0,0,3,500],0)
        pygame.draw.rect(screen, [150,157,179], [797,0,3,500],0)
        screen.blit(block.image, block.rect)
        bosser.draw(screen)
        screen.blit(bossHat.image, bossHat.rect)
    elif room == -5:
        screen.fill([255,0,0])
    elif room == 0:
        screen.fill([0,0,0])
        pygame.draw.rect(screen, [255,255,255], [312,250,175,50], 0)
        pygame.draw.rect(screen, [125,125,125], [300,237,200,75],12)
        screen.blit(fonters(None, 60).render('Play', 1, (0,0,0)), [355,255])
        screen.blit(fonters(None, 120).render('Escape From', 1, (255,255,255)), [140,50])
        screen.blit(fonters(None, 120).render('the Dungeon', 1, (255,255,255)), [140,145])

#Initialize and Run Code
pygame.init()
screen = pygame.display.set_mode([800,500])
tock = pygame.time.Clock()
block = blockClass()
bosser = pygame.sprite.GroupSingle()
firewally = pygame.sprite.Group()
pygame.mixer.music.load("thomas.wav")
pygame.mixer.music.play(-1)
timer = 0
coins_collected = 0
leftMoving = False
rightMoving = False
room = 0
Running = True
upwards = 0
rest = False
lives = 3
passed_firewall = False
first_time_room_1 = True
first_time_room_2 = True
first_time_room_5 = True
bosslife = True
can_move = True
seconds = 0
room_2_start_sec = 0
weard = None


while room == 0:
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if (event.type == pygame.MOUSEBUTTONDOWN) and (Mouse_x > 311) and (Mouse_x < 489) and (Mouse_y > 249) and (Mouse_y < 301):
            room = 1
    animate(passed_firewall)
while Running:
    tock.tick(120)
    if timer < 120:
        timer = timer + 1
    if timer >= 120:
        timer = 0
        seconds = seconds + 1
    if seconds-room_2_start_sec > 31:
        passed_firewall = True
    if  (first_time_room_2) and (room == 2):
        room_2_start_sec = seconds
        first_time_room_2 = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                upwards = 357
                rest = False
    if block.getUp(screen) == (150,157,178,255):
        upwards = -50
    if upwards > 0:
        upwards = (upwards/1.03)-3
    else:
        upwards = (upwards*1.03)-3
    if not block.getUnder(screen) == (150,157,178,255):
        rest = False
    if not rest:
        block.moveUp(upwards)
    if block.getUnder(screen) == (150,157,178,255):
        upwards = 0
        rest = True
    animate(passed_firewall)
    if can_move:
        if(pygame.key.get_pressed()[pygame.K_LEFT]) & (block.getLeft(screen) != (150,157,178,255)):
            leftMoving = True
        if leftMoving:
            block.moveLeft()
            leftMoving = False
        if(pygame.key.get_pressed()[pygame.K_RIGHT]) & (block.getRight(screen) != (150,157,178,255)):
            rightMoving = True
        if rightMoving:
            block.moveRight()
            rightMoving = False
        if block.getRight(screen) == (150,157,179,255):
            room = room + 1
            #animate(passed_firewall)
            block.teleport(40,block.getY())
            if first_time_room_2 and room == 2:
                for i in range(9):
                    fireWall(i * (-350) - 300)
            print(room)
        if block.getLeft(screen) == (150,157,177,255):
            room = room - 1
            #animate(passed_firewall)
            block.teleport(760,block.getY())
        elif block.getUnder(screen) == (249,92,34,255):
            room = -5
        if (room == 5) and (first_time_room_5):
            Firet = bossMan()
            bosser.add(Firet)
            bossHat = bossManHat()
            weard = Firet
            bossHat.update(weard)
            first_time_room_5 = False
        if room == 2:
            hitFire =  pygame.sprite.spritecollide(block, firewally, False)
            if hitFire:
                room = -5
                animate(passed_firewall)
        if room == 5:
            hitBossMan =  pygame.sprite.spritecollide(block, bosser, False)
            hitHat =  pygame.sprite.collide_rect(block, bossHat)
            if hitBossMan:
                room = -5
                animate(passed_firewall)
            if hitHat:
                Firet.kill()
                weard = block
                bosslife = False
        if not bosslife:
            bossHat.update(weard)
        firewally.update()
        animate(passed_firewall)
    
