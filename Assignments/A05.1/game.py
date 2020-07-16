"""
Travis Bales
Professor Griffin

Pygame A05-005
Description:
   Moving a player with Mouse
New Code:
     event.type == pygame.MOUSEBUTTONUP
"""
# Import and initialize the pygame library
import pygame
import random
import json
import pprint
import sys
import os
import math
import time

# Tells OS where to open the window
os.environ['SDL_VIDEO_WINDOW_POS'] = str(1000) + "," + str(100)
#helper modules courtesy of Professor Griffin
from helper_module import load_colors
from helper_module import mykwargs
from helper_module import straightDistance
from PIL import Image


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


#config that holds the screen size and the name of the window
#will not be used in this program
config = {
    'title' :'006 Pygame Lesson',
    'window_size' : {
        'width' : 600,
        'height' : 480
    }
}
#loads the colors that we will use to draw items
colors = load_colors('colors.json')

#creates the object that will hold the sprite and it's properties
#will also hold the functions to move and update it's position
class Player(pygame.sprite.Sprite):
    def __init__(self,screen,color,x,y,r):
        pygame.sprite.Sprite.__init__(self)
        #create a sprite rectangle of width and height selected by user input
        x = argv[4].split('=')
        self.image = pygame.Surface([int(x[1]),int(x[1])])
        #fill the sprite with the color input
        self.image.fill(color)
        #self.image2 = pygame.image.load("Images//BillStanding.png").convert()
        self.rect = self.image.get_rect()
        #set the center of the sprite
        x = argv[1].split('=')
        y = argv[2].split('=')
        self.rect.center = (int(x[1]) / 2, int(y[1]) / 2)
        #initialize values
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = r
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        self.speed = 15
        self.last_direction = None
        self.target_location = None
        self.moving = False

    def update(self):
        self.rect.x += 5
        if self.rect.left > 640:
            self.rect.right = 0

    def Draw(self):
        pass
        #screen.blit(self.image2, self.rect)
        #pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    #moves the object to the location
    def BouncyMove(self):
        w, h = pygame.display.get_surface().get_size()
        self.rect.x += (self.speed * self.dx)
        self.rect.y += (self.speed * self.dy)
        if self.rect.x <= 0 or self.rect.x >= w:
            self.dx *= -1
        if self.rect.y <= 0 or self.rect.y >= h:
            self.dy *= -1
    #returns true if the object is on the viewable world
    #false if it is not
    def OnWorld(self):
        w, h = pygame.display.get_surface().get_size()
        return self.rect.center[0] > 0 + (self.radius//2) and self.rect.center[0] + (self.radius//2) < w and self.rect.center[1] > 0 + (self.radius//2) and self.rect.center[1] + (self.radius//2) < h
    def GetDirection(self,keys):
        if keys[K_UP]:
            return K_UP
        elif keys[K_DOWN]:
            return K_DOWN
        elif keys[K_LEFT]:
            return K_LEFT
        elif keys[K_RIGHT]:
            return K_RIGHT
        return None
    def Move(self):
        if self.moving:
            self.MoveWithMouse()
    #moves sprite to mouse location on clicj
    def MouseClicked(self,loc):
        self.target_location = loc
        self.moving = True
        self.MoveWithMouse()
    #moves sprite to mouse location logic
    def MoveWithMouse(self):
        if not self.moving:
            return
        x = self.target_location[0]
        y = self.target_location[1]
        dx = x - self.rect.x
        dy = y - self.rect.y 
        angle = math.atan2(dy, dx)
        if straightDistance(self.rect.x,self.rect.y,x,y) > 10:
            self.rect.x += int(self.speed * math.cos(angle))
            self.rect.y += int(self.speed * math.sin(angle))
            if not self.OnWorld():
                self.rect.x -= int(self.speed * math.cos(angle))
                self.rect.y -= int(self.speed * math.sin(angle))
    #moves the sprite with keys, has logic to not pass world borders
    def MoveWithKeys(self,keys):
        w, h = pygame.display.get_surface().get_size()
        self.moving = False
        if keys[K_UP]:
            self.rect.y -= self.speed
            if not self.OnWorld():
                self.rect.y += self.speed
            self.last_direction = K_UP
        elif keys[K_DOWN]:
            self.rect.y += self.speed
            if not self.OnWorld():
                self.rect.y -= self.speed
            self.last_direction = K_DOWN
        elif keys[K_LEFT]:
            self.rect.x -= self.speed
            if not self.OnWorld():
                self.rect.x += self.speed
            self.last_direction = K_LEFT
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
            if not self.OnWorld():
                self.rect.x -= self.speed
            self.last_direction = K_RIGHT
#easy way to break down args. Did not use 
def mykwargs(argv):
    '''
    Processes argv list into plain args and kwargs.
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}
        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs
    print(args + " " + kargs)
        
def usage():
    # Params in square brackets are optional
    # The kwargs function script needs key=value to NOT have spaces
    print("Usage: python basic.py title=string width=int height=int color = int size=int[jsonfile=string]")
    print("Example:\n\n\t python basic.py title='Game 1' width=640 height=480 122,122,122 size=90 \n")
    sys.exit()


def main(**kwargs):
    pygame.init()
    

    # sets the window title
    #pygame.display.set_caption(config['title'])
    x = argv[0].split('=')
    pygame.display.set_caption(x[1])

    # set screen size location
    x = argv[1].split('=')
    y = argv[2].split('=')
    width = int(x[1])
    height = int(y[1])

    # Set up the drawing window
    screen = pygame.display.set_mode((width,height))
    x = argv[4].split('=')
    # construct the sprite
    p1 = Player(screen,colors['rebeccapurple']['rgb'],width//2,height//2,int(x[1]))

    # Run until the user asks to quit
    # game loop
    running = True
    followmouse = True
    lastchange = False
    #the sprite collection to add to screen
    all_sprites = pygame.sprite.Group()
    all_sprites.add(p1)
    while running:
        
        #print(followmouse)
        #let's slow down the loop so we can use a reasonable speed
        time.sleep(.01)
        if followmouse == True:
            p1.MouseClicked(pygame.mouse.get_pos())
        #Fill the background with white
        x,y,z = argv[3].split(',')
        screen.fill((int(x),int(y),int(z)))
        #screen.fill(colors['white']['rgb'])
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lastchange == False:
                lastchange = True
                followmouse = not followmouse
        if event.type != pygame.MOUSEBUTTONDOWN:
            lastchange = False
        if pygame.key.get_pressed():
            p1.MoveWithKeys(pygame.key.get_pressed())
        # handle MOUSEBUTTONUP

        #p1.Move()
        #p1.Draw()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.blit(p1.image, p1.rect)


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    argv = sys.argv[1:]
    #if len(argv) < 6 or len(argv) > 6:
    #    print(len(argv))
    #    usage()
    #colors = fix_colors("colors.json")
    #pprint.pprint(colors)
    main()
