# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
import sys
from settings import *
from SpriteHandler import *
from os import path
from MapCreator import *


class Game:
    def __init__(self,map):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #the rate at which holding down button moves the player
        pg.key.set_repeat(10, 80)
        self.load_data(map)
        self.playerSpawn = (0,0)
        self.lastmap = 1
        self.finalmap = 0
        self.keyfound = False
        self.deathcounter = 0

    def deathcounterup(self):
        self.deathcounter = self.player.deathcounter

    #this loads the map data into the list
    def load_data(self,map):
        game_folder = path.dirname(__file__)
        #holds the data from the loaded map
        self.map = Map(path.join(game_folder,map))
        self.spritesheet = Spritesheet('Kings and Pigs\\Sprites\\01-King Human\\Idle (78x58).png')
        #load player image
        #self.player_img = pg.image.load(PLAYER_IMG).convert_alpha()



    #spawn point of character
    def new(self,map):
        self.map = Map(map)
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bgs = pg.sprite.Group()
        self.objects = pg.sprite.Group()
        #spawns player at 10,10
        #self.player = Player(self, 10, 10)
        '''
        #manual wall creation
        for x in range(10, 20):
            Wall(self, x, 5)
        '''
        #row will be index value and tile is the string of characters
        for row, tiles in enumerate(self.map.data):
            #now we enumerate through the string
            for col,tile in enumerate(tiles):
                if tile == '.':
                    holder = '.'
                    Background(self,col,row,holder)
                if tile == 'V':
                    holder = 'V'
                    Background(self,col,row,holder)
                if tile =='p':
                    self.playerSpawn = (col,row)
                    Background(self,col,row,'.')
                    #self.player = Player(self,col,row)
                if tile == 'L':
                    holder = 'L'
                    Wall(self,col,row,holder)
                if tile == 'R':
                    holder = 'R'
                    Wall(self,col,row,holder)
                if tile == 'F':
                    holder = 'F'
                    Wall(self,col,row,holder)
                if tile == 'C':
                    holder = 'C'
                    Wall(self,col,row,holder)
                if tile == 'B':
                    Boxes(self,col,row)
        #spawn camera to be used
        self.camera = Camera(self.map.width,self.map.height)

                 


    def run(self):
        #pygame.mixer.music.load('Sounds\\Music.wav')
        #pygame.mixer.music.play(-1, 0.0)
        sound = pygame.mixer.Sound("Sounds\\Music.wav")
        channel = sound.play(-1,0)      # Sound plays at full volume by default
        sound.set_volume(0.9)   # Now plays at 90% of full volume.
        sound.set_volume(0.6)   # Now plays at 60% (previous value replaced).
        channel.set_volume(0.1)
        #soundObj = pygame.mixer.Sound('Sounds\\Music.wav')
        #soundObj.play()

        # game loop - set self.playing = False to end the game
        self.playing = True
        nlabel=myfont.render("Welcome Start Screen", 1, (255, 0, 0))
        self.screen.blit(nlabel,(200,200))
        starttime = 0
        while self.playing:
            self.deathcounterup()
            n1label=myfont.render(("Deaths: " + str(self.deathcounter)), 1, (255, 0, 0))
            self.screen.blit(n1label,(32,128))
            if self.finalmap == 1 and self.player.pos.y <= 40:
                print('oh yeah')
                starttime = pygame.time.get_ticks()
                holder = pygame.time.get_ticks()
                screen1.fill(black)
                self.screen.fill(black)
                nlabel=myfont.render("You WIN!!!!", 1, (0, 255, 0))
                n2abel=myfont.render("Press Space Bar to close", 1, (255, 0, 0))
                screen1.blit(nlabel,(350,200))
                screen1.blit(n2abel,(350,300))
                pygame.display.flip()
                pygame.event.clear()
                while True:
                    event = pg.event.wait()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            pygame.quit()
                            sys.exit()
            if self.deathcounter >= 15:
                starttime = pygame.time.get_ticks()
                holder = pygame.time.get_ticks()
                screen1.fill(black)
                self.screen.fill(black)
                nlabel=myfont.render("Game Over, you're bad", 1, (255, 0, 0))
                n2abel=myfont.render("Press Space Bar to close", 1, (255, 0, 0))
                screen1.blit(nlabel,(350,200))
                screen1.blit(n2abel,(350,300))
                pygame.display.flip()
                pygame.event.clear()
                while True:
                    event = pg.event.wait()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            pygame.quit()
                            sys.exit()
            if self.keyfound == False:
                nlabel=myfont.render("Key not Found", 1, (255, 0, 0))
            else:
                nlabel=myfont.render("Key Found!", 1, (255, 0, 0))
            self.screen.blit(nlabel,(32,32))
            pygame.display.flip()
            print(str(self.player.pos.x) + " " + str(self.player.pos.y))
            if self.lastmap == 2:
                if self.player.pos.x <= 1162 and self.player.pos.x >= 1111 and self.player.pos.y == 864:
                    for sprite in self.objects:
                        if self.keyfound == False:
                            sound = pygame.mixer.Sound("Sounds\\Pickup.wav")
                            channel = sound.play()
                        self.keyfound = True
                        sprite.image = pygame.image.load('BasicFrames\\M.png')
            if self.player.pos.x <= 540 and self.player.pos.y == 320 and self.lastmap == 1:
                for sprite in self.objects:
                    if self.keyfound == False:
                        sound = pygame.mixer.Sound("Sounds\\Pickup.wav")
                        channel = sound.play()
                    self.keyfound = True
                    sprite.image = pygame.image.load('BasicFrames\\M.png')
            elif self.player.pos.x >= 1980 and self.player.pos.y >= 410 and self.lastmap == 1 and self.keyfound == True:
                self.keyfound = False
                self.lastmap = 2
                g.new('Map2.txt')
                sound = pygame.mixer.Sound("Sounds\\Level.wav")
                channel = sound.play()
                self.camera.width = 64 * TILESIZE
                self.camera.height = 32 * TILESIZE
                self.camera.update(self.player)
                self.player = Player(self,self.camera.width,self.camera.height)
            elif self.player.pos.x <= 137 and self.player.pos.y == 256 and self.lastmap == 2 and self.keyfound:
                sound = pygame.mixer.Sound("Sounds\\Level.wav")
                channel = sound.play()
                g.new('Map3.txt')
                self.camera.width = 64 * TILESIZE
                self.camera.height = 32 * TILESIZE
                self.camera.update(self.player)
                self.player = Player(self,self.camera.width,self.camera.height)
                self.finalmap = 1

            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        #print(str(self.player.pos.x) + " " + str(self.player.pos.y))

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            if sprite.type == 1: 
                self.screen.blit(sprite.image,self.camera.apply(sprite))
        for sprite in self.all_sprites:
            if sprite.type != 1: 
                self.screen.blit(sprite.image,self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
    
# create the game object
screen1 = pg.display.set_mode((WIDTH, HEIGHT))

startgame = False
black=(0,0,0)
screen1.fill(black)
myfont=pygame.font.SysFont("Britannic Bold", 40)
nlabel=myfont.render("Just Reach The End", 1, (255, 255, 0))
n2abel=myfont.render("by Travis Bales", 1, (255, 255, 255))
screen1.blit(nlabel,(350,300))
screen1.blit(n2abel,(350,400))
pygame.display.flip()
while(pg.time.get_ticks() != 3000):
    pass
screen1.fill(black)
nlabel=myfont.render("Start Level 1", 1, (255, 0, 0))
screen1.blit(nlabel,(350,300))
pygame.display.flip()
g = Game("Map.txt")
g.show_start_screen()

mousepos = pygame.mouse.get_pos()
while True:
    g.new('Map.txt')
    print(str(mousepos[0]) + " " + str(mousepos[1]))
    mousepos = pygame.mouse.get_pos()
    if mousepos[0] >= 345 and mousepos[0] <= 445:
        if mousepos[1] >= 293 and mousepos[1] <= 336:
            print('true')
            screen1.fill(black)
            n2abel=myfont.render("Start Level 1", 1, (255, 255, 0))
            screen1.blit(n2abel,(350,300))
    else:
        screen1.fill(black)
        nlabel=myfont.render("Start Level 1", 1, (255, 0, 0))
        screen1.blit(nlabel,(350,300))

            
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if startgame == False:
                if mousepos[0] >= 345 and mousepos[0] <= 445:
                    if mousepos[1] >= 293 and mousepos[1] <= 336:
                        g.player = Player(g,g.playerSpawn[0],g.playerSpawn[1])
                        startgame = True
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if startgame == True:
        g.run()
    g.show_go_screen()