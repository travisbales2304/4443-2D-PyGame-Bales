import pygame as pg
from settings import *
from pygame_functions import *
vec = pg.math.Vector2
Player_Speed = 1000



class Spritesheet:
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert_alpha()

    def get_image(self,x,y,width,height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet,(0,0),(x,y,width,height))
        #image = pg.transform.scale(image,(width // 2, height // 2))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.type = 0
        self.game = game
        self.jumping = False
        self.counter = 0
        self.framecounter = 0
        self.lorr = 0
        self.deathcounter = 0
        print("Generated char")
        ##
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.image = pg.image.load(PLAYER_IMG).convert_alpha()
        self.image = self.game.spritesheet.get_image(10,15,32,32)
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image,(32,32))
        #self.image.fill(YELLOW)
        ##
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE

    def get_keys(self):
        #print(self.pos)
        if self.game.lastmap == 1:
            if self.pos.y > 416:
                self.pos.y = 416
        if self.game.lastmap == 2:
            if self.pos.y >= 992:
                    self.pos = (64,960)
                    sound = pygame.mixer.Sound("Sounds\\Death.wav")
                    channel = sound.play()
                    self.deathcounter +=1
                    print('ded')
        self.vel = vec(0,self.vel.y+100)
        #print(self.counter)
        #if self.pos.y < 416 and not self.jumping:
        #    self.pos.y = 416
        if self.vel ==  (0,100):
            self.counter +=1
        if self.vel == (0,100) and self.counter >= 10:
            self.jumping = False
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vel.x = -Player_Speed
            self.lorr = 1
            self.image = self.game.spritesheet.get_image((self.framecounter % 11) * 78,15,58,32)
            self.image.set_colorkey(BLACK)
            self.image = pygame.transform.flip(self.image,True,False)
        elif keys[pg.K_RIGHT]:
            self.vel.x = Player_Speed
            self.lorr = 0
            self.image = self.game.spritesheet.get_image((self.framecounter % 11) * 78,15,58,32)
            self.image.set_colorkey(BLACK)
        if keys[pg.K_UP]:
            if self.jumping == False:
                self.jumping = True
                self.counter = 0
                self.vel.y = -Player_Speed
        elif keys[pg.K_DOWN]:
            self.vel.y = Player_Speed
        else:
            self.framecounter+= 1
            if self.framecounter % 20 == 0:
                if self.lorr == 0:
                    self.image = self.game.spritesheet.get_image((self.framecounter % 11) * 78,15,58,32)
                    self.image.set_colorkey(BLACK)
                else:
                    self.image = self.game.spritesheet.get_image((self.framecounter % 11) * 78,15,58,32)
                    self.image.set_colorkey(BLACK)
                    self.image = pygame.transform.flip(self.image,True,False)

    
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy
    

    #checks if next player move is going to collide with a wall
    def collide_with_walls(self,dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
                return True
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
                return True
           


    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y,which):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.type = 1
        self.game = game
        if which == 'V':
            self.image = pygame.image.load('BasicFrames\\0.png')
        elif which == 'L':
            self.image = pygame.image.load('BasicFrames\\L.png')
        elif which == 'R':
            self.image = pygame.image.load('BasicFrames\\R.png')
        elif which == 'F':
            self.image = pygame.image.load('BasicFrames\\F.png')
        elif which == 'C':
            self.image = pygame.image.load('BasicFrames\\C.png')

        self.image = pygame.transform.scale(self.image,(32,32))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Background(pg.sprite.Sprite):
    def __init__(self, game, x, y,which):
        self.groups = game.all_sprites, game.bgs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.type = 1
        self.game = game
        if which == '.':
            self.image = pygame.image.load('BasicFrames\\M.png')
        elif which == 'V':
            self.image = pygame.image.load('BasicFrames\\0.png')

        self.image = pygame.transform.scale(self.image,(32,32))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Boxes(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.objects
        pg.sprite.Sprite.__init__(self, self.groups)
        self.type = 1
        self.game = game
        self.image = pygame.image.load('Kings and Pigs\\Sprites\\08-Box\\Idle.png')
        self.image = pygame.transform.scale(self.image,(32,32))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE