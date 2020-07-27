"""
Travis Bales
Pygame scroller with bounds detection
Description:
   Background Images and Scrolling Background
New Code:
"""
# Import and initialize the pygame library
import pygame
import random
import json
import pprint
import sys
import os
import math
from tkinter import *
from tkinter import messagebox


# Tells OS where to open the window
# Delete later or change to your own values
os.environ['SDL_VIDEO_WINDOW_POS'] = str(1000) + "," + str(100)

from helper_module import rgb_colors
from helper_module import mykwargs
from helper_module import straightDistance
from helper_module import getCardinalDirection


#key dictionary to keep track of all the key's that are being pressed and held down
keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0}
screen = ""

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
config = {
    'title' :'009 Pygame Sprite Movement',
    'window_size' : {
        'width' : 500,
        'height' : 500
    },
    'sprite_sheet':'pacman_ghosts_40x.png',
    'background':'tile_1000x1000_40_light.png'
}
colors = rgb_colors('colors.json')

#creates the pacman sprite and has the functions to animate it
class PacmanSprite(pygame.sprite.Sprite):
    # This code gets executed as soon as we create a new instance
    def __init__(self, **kwargs):
        # Initiate this sprite
        pygame.sprite.Sprite.__init__(self)
        self.screen = kwargs.get('screen',None)
        if not self.screen:
            print("Error: PacmanSprite needs a copy of the screen!!")
            sys.exit()
        # Mandatory Params
        self.gameWidth = int(sys.argv[1])
        self.gameHeight = int(sys.argv[2])
        #self.gameWidth = config['window_size']['width']
        #self.gameHeight = config['window_size']['height']
        if not self.gameWidth or not self.gameHeight:
            print("Error: No gameWidth or gameHeight!")
            sys.exit(0)
        self.frame_nums = [0,1,2]
        # possible pacman colors
        colors = ['red','purple','orange','blue']
        # color choice
        color = kwargs.get('color','purple')
        colors.index(color)
        self.sprite = sys.argv[7]
        self.resizex = kwargs.get('sizefactor',2)
        self.tilesize = kwargs.get('tilesize',40) * self.resizex
        # offsets x coord to beginning column of a color
        self.color_offset = colors.index(color) * len(self.frame_nums) * self.tilesize
        # pacmans position
        self.x = self.gameWidth // 2
        self.y = self.gameHeight // 2
        self.image = pygame.image.load(self.sprite)
        # get original image size
        self.image_size = self.image.get_rect().size
        # resize the sprite sheet
        self.image = pygame.transform.scale(self.image, (self.image_size[0]*self.resizex, self.image_size[1]*self.resizex))
        # preserve alpha channel (I think)
        self.image = self.image.convert_alpha()
        # A bounding rectangle not necessary
        # self.rect = self.image.get_rect()
        # self.rect.center = (self.x, self.y)
        # slow down the rate of frame change
        self.delay = 2
        self.callCounter = 0
        self.frameCounter = 0
    def GetRect(self):
        pass
    #moves the frame on the sprite sheet
    def Move(self,events):
        yoffset = 0
        # Picks the proper frame depending on keys(s) pressed.
        if sum(events['all_pressed']) > 1:
            if events['all_pressed'][K_UP]:
                if events['all_pressed'][K_LEFT]:
                    yoffset = self.tilesize * 6
                if events['all_pressed'][K_RIGHT]:
                    yoffset = self.tilesize * 5
            if events['all_pressed'][K_DOWN]:
                if events['all_pressed'][K_LEFT]:
                    yoffset = self.tilesize * 7
                if events['all_pressed'][K_RIGHT]:
                    yoffset = self.tilesize * 8
        else:
            if events['all_pressed'][K_UP]:
                yoffset = self.tilesize * 3
            if events['all_pressed'][K_DOWN]:
                yoffset = self.tilesize * 4
            if events['all_pressed'][K_LEFT]:
                yoffset = self.tilesize * 2
            if events['all_pressed'][K_RIGHT]:
                yoffset = self.tilesize * 1
        # call counter is how many times move is called.
        # we will use it to determine how often to switch between frames in the sprite.
        self.callCounter += 1
        # increment frame counter based on the delay we set
        if self.callCounter % self.delay == 0:
            self.frameCounter+= 1
        # midpoint of a frame so it prints centered
        mid = self.tilesize // 2
        # xoffset picks the color of the ghost
        xoffset = self.color_offset
        frame = xoffset + self.frame_nums[self.frameCounter%len(self.frame_nums)]*self.tilesize
        self.screen.blit(self.image, (self.x-mid, self.y-mid),(frame,yoffset,self.tilesize,self.tilesize))

#contains all the events to use for other classes
class EventContainer:
    """ Dictionary of events all kept in one place for use in other classes
    """
    def __init__(self):
        self.events = {
            'keydown':None,
            'keyup':None,
            'mouse_motion':None,
            'mouse_button_up':None,
            'all_pressed':None
        }

    def reset(self):
        """ Set all to None
        """
        for k,v in self.events.items():
            self.events[k] = None

    def __str__(self):
        """Dump instance to screen or wherever
        """
        s = ''
        for k,v in self.events.items():
            if k == 'all_pressed':
                continue
            s += f"{k} : {v}\n"

        return s

#keeps treack of the background, it's location
#keeps track of pacman location
#keeps track of barrier location
#draws barrier bounds and produces alert when approaching the edge of the map
class BackgroundScroller:
    def __init__(self,screen,floor,tile_size):
        # assumes squares for now
        self.screen = screen                            # pygame screen handle
        self.bgimg = pygame.image.load(floor)            # background img handle
        self.bgimg_size = self.bgimg.get_rect().size    # size of bg image: tuple (w,h)
        self.tile_size = tile_size
        self.gw = int(sys.argv[1])
        self.gh = int(sys.argv[2])
        self.floorw = self.bgimg_size[0]
        self.floorh = self.bgimg_size[1]
        self.cx = self.gw // 2                          # center x (of game window)
        self.cy = self.gh // 2                          # center y
        self.step = 2                                   # move size in any direction
        self.target_location = None                     # tuple (x,y) of where to move to
        self.cardinal_direction = None                  # direction to move to go toward goal
        self.distance_to_target = 0
        self.scroll_x = 0
        self.scroll_y = 0
        self.w_buffer = (self.floorw-self.gw) // 2
        self.h_buffer = (self.floorh-self.gh) // 2
        self.boundx = 0
        self.boundy = 0
        self.showmessage = True

    #get the direction to scroll to in cardinal directions
    def setScrollDirection(self,loc=None):
        """If keys are pressed or mouse is clicked, set a goal location to scroll toward.
        """
        self.target_location = loc
        self.cardinal_direction = getCardinalDirection((self.cx,self.cy), self.target_location)
        self.distance_to_target = straightDistance((self.cx,self.cy),self.target_location)

        print(self.target_location)
        print(self.cardinal_direction)
        print(self.distance_to_target)

    #creates a white background
    def drawBackground(self):
        self.screen.fill(colors['white'])
        self.scrollBackground()

    #returns a number corresponding to what bound pacman is at
    #1 = outside of x bound positive
    #2 = outside of x bound positive and y bound negative
    #3 outside of x bound positive and y bound positive
    #4 outside of x bound negative
    #5 outside of x bound negative and y bound negative
    #6 outside of x bound negative and y bound positive
    #7 outside of y bound positive
    #8 outside of y bound negative
    #9 not outside of bounds
    def IsAtBoundsEdge(self,x,y):
        if x + 5 >= self.boundx: 
            if y <= -self.boundy:return 2
            elif y >= self.boundy:return 3
            else:return 1
        elif x <= -self.boundx: 
            if y <= -self.boundy:return 5
            elif y >= self.boundy:return 6
            else: return 4
        elif y >= self.boundy: return 7
        elif y <= -self.boundy: return 8
        else: return 9
    #updates the boundary for the map
    def UpdateBounds(self,x,y):
        self.boundx = x
        self.boundy = y
    #sets the location of the character in the map
    def setlocation(self,x,y):
        if x > self.gw:
            self.cx = x - 50
        elif x < 0:
            self.cx = self.gw % 5
        else: self.cx = int(sys.argv[3])
        if y > self.gh:
            self.cy = y - 50
        elif y < 0:
            self.cy = self.gh % 5
        else: self.cy = int(sys.argv[4])
        
        self.cx = x
        self.cy = y
    #updates location of the character
    def UpdateLoc(self,x,y):
        self.cx += x
        self.cy += y
        print(str(self.IsAtBoundsEdge(self.cx,self.cy)))
        print(str(self.cx) + " " + str(self.cy))
    #draws a barrier to be used on map edges
    def drawthebarrier(self):
        drawRect(self.screensizex // 2 + 50,self.screensizey // 12,500,500,pygame.Color("red"))
    #scrolls the background in certain directions and draws barriers and produces edge hit message
    def scrollBackground(self):
        if self.target_location != None:
            if 'N' in self.cardinal_direction :
                if self.cy >= self.target_location[1]:
                    if self.cy + -self.step >= -self.boundy:
                        self.scroll_y -= self.step
                        self.UpdateLoc(0,-self.step)
                        self.showmessage = True
                        #self.cy -= self.step
                    else:
                        pygame.draw.rect(self.screen,pygame.Color("red"),[0, 200, 500, 10])
                        if self.showmessage == True:
                            self.showmessage = False
                            Tk().wm_withdraw() #to hide the main window
                            messagebox.showinfo('Boundary Hit','OK')
                        
            if 'S' in self.cardinal_direction :
                if self.cy <= self.target_location[1]:
                    if self.cy + self.step <= self.boundy:
                        self.scroll_y += self.step
                        self.UpdateLoc(0,self.step)
                        self.showmessage = True
                        #self.cy += self.step
                    else:
                        pygame.draw.rect(self.screen,pygame.Color("red"),[0, 300, 500, 10])
                        if self.showmessage == True:
                            self.showmessage = False
                            Tk().wm_withdraw() #to hide the main window
                            messagebox.showinfo('Boundary Hit','OK')
            if 'E' in self.cardinal_direction :
                if self.cx <= self.target_location[0]:
                    if self.cx + self.step <= self.boundx:
                        self.scroll_x += self.step
                        self.UpdateLoc(self.step,0)
                        self.showmessage = True
                        #self.cx += self.step
                    else:
                        pygame.draw.rect(self.screen,pygame.Color("red"),[300, 0, 10, 500])
                        if self.showmessage == True:
                            self.showmessage = False
                            Tk().wm_withdraw() #to hide the main window
                            messagebox.showinfo('Boundary Hit','OK')
                        if self.cy >= .95*self.boundy:
                            pygame.draw.rect(self.screen,pygame.Color("red"),[0, 300, 500, 10])
                            if self.showmessage == True:
                                self.showmessage = False
                                Tk().wm_withdraw() #to hide the main window
                                messagebox.showinfo('Boundary Hit','OK')
                        elif self.cy <= 50:
                            pygame.draw.rect(self.screen,pygame.Color("red"),[0, 200, 500, 10])
                            if self.showmessage == True:
                                self.showmessage = False
                                Tk().wm_withdraw() #to hide the main window
                                messagebox.showinfo('Boundary Hit','OK')
            if 'W' in self.cardinal_direction :
                if self.cx >= self.target_location[0]:
                    if self.cx + -self.step >= -self.boundx:
                        self.scroll_x -= self.step
                        self.UpdateLoc(-self.step,0)
                        self.showmessage = True
                        #self.cx -= self.step
                    else:
                        pygame.draw.rect(self.screen,pygame.Color("red"),[200, 0, 10, 500])
                        if self.showmessage == True:
                            self.showmessage = False
                            Tk().wm_withdraw() #to hide the main window
                            messagebox.showinfo('Boundary Hit','OK')
                        if self.cy >= .95*self.boundy:
                            pygame.draw.rect(self.screen,pygame.Color("red"),[0, 300, 500, 10])
                            if self.showmessage == True:
                                self.showmessage = False
                                Tk().wm_withdraw() #to hide the main window
                                messagebox.showinfo('Boundary Hit','OK')
                        elif self.cy <= 50:
                            pygame.draw.rect(self.screen,pygame.Color("red"),[0, 200, 500, 10])
                            if self.showmessage == True:
                                self.showmessage = False
                                Tk().wm_withdraw() #to hide the main window
                                messagebox.showinfo('Boundary Hit','OK')

        self.scroll_x = self.scroll_x % self.tile_size
        self.scroll_y = self.scroll_y % self.tile_size
        basex = self.w_buffer + (self.scroll_x)
        basey = self.h_buffer + (self.scroll_y)
        self.screen.blit(self.bgimg, (0,0), (basex,basey,self.gw,self.gh))

#get what key is pressed out of the dictionary we created
def keyPressed(keyCheck=""):
    global keydict
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False



def main(**kwargs):
    pygame.init()

    eventHelper = EventContainer()

    # sets the window title
    pygame.display.set_caption(sys.argv[5])

    # set circle location
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    # Set up the drawing window
    screen = pygame.display.set_mode((width,height))

    pman = PacmanSprite(screen = screen,color='blue')
    background = BackgroundScroller(screen,sys.argv[6],40)
    background.setlocation(int(sys.argv[3]),int(sys.argv[4]))

    
    # Run until the user asks to quit
    # game loop
    running = True

    background.UpdateBounds(1000,1000)




        

    while running:

        # Did the user click the window close button?
        eventHelper.reset()

        background.drawBackground()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                eventHelper.events['keydown'] = event.key
                if keyPressed("right"):
                    background.setScrollDirection((background.cx + 20000,background.cy))
                    background.scrollBackground()
                elif keyPressed("down"):
                    background.setScrollDirection((background.cx,background.cy + 2000))
                    background.scrollBackground()
                elif keyPressed("left"):
                    background.setScrollDirection((background.cx - 2000,background.cy))
                    background.scrollBackground()
                elif keyPressed("up"):
                    background.setScrollDirection((background.cx,background.cy - 2000))
                    background.scrollBackground()
                else:
                    pass
                

            if event.type == pygame.KEYUP:
                eventHelper.events['keyup'] = event.key
                background.target_location = (background.cx,background.cy)

            if event.type == pygame.MOUSEMOTION:
                eventHelper.events['mouse_motion'] = pygame.mouse.get_pos()
                

            if event.type == pygame.MOUSEBUTTONUP:
                eventHelper.events['mouse_button_up'] = pygame.mouse.get_pos()
                background.setScrollDirection(pygame.mouse.get_pos())

        eventHelper.events['all_pressed'] = pygame.key.get_pressed()

        pman.Move(eventHelper.events)
        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    if(len(sys.argv)>7):
        pass
        #sys.exit('Too many Params')

    main()
