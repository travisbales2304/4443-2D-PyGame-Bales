# Movable sprite with Edge Detection with more animations,shooting,and enemies(Project 1.04)
Travis Bales

## Description:
Using command line parameters set the screen size, title, color of the background, and size of sprite used in window.
The sprite is allowed to move around within the map boundaries and upon hitting the edge, a map boundary will appear and a message will appear
When hitting the barrier an explosion sprite will activate, can shoot projectiles,plays sound on shooting and when hitting a mob, There is also mobs now! Many upgrades to
the entire system (Completely recoded everything)
<br>
- **Using python 3.8.3**

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|1| [game_pt4.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/game_pt4.py) |The main driver that launches the gui to produces the game window|
|2|[Helper_Module.py]()|Helper module provided |
|3|[Background Image](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/Background.jpg)|Imagine used for the background|
|4|[Enemies](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/BardoFull.png)|Sprite used for the enemies|
|5|[Bullet Sprite](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/Bullet.png)|Sprite used for the bullet|
|6|[Player Sprite for wall](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/LinkWall.png)|sprite that shows when player hits a wall|
|7|[Right and Left bounds](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/RightLeftBarrier.png)|Visual barries that is used for left and right bounds of map|
|8|[Top and Bot Bounds](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/TopBotBarrier.png)|visual Barriers that is used for the top and bottom of the map|
|9|[Rocket sound](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/RockShot.wav)|Sound that plays when rocket is shot|
|10|[explosion sound](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/Splosion.wav)|sound that plays when an enemy is hit with rocket|
|11|||
<br>

# HOW TO TRIGGER DEATH SPRITE (New 7/29/20)
  - run into a wall and click of for the death message and the death sprite will start animating until you move away from the wall
<br>

#### How to Run:
  - Download game_pt2.py to desktop
  - change director to that location. Ex. cd C:\Users\"your user"\Desktop
  - Download character spritesheet that to desktop
  - type "game_pt2.py 500 500 400 400 packman bg.png pacmanchar.png"
  - My program expects seven parameters to be placed on the command line when you run the program.
  - Parameters
    - game width - width of the game window
    - game height - height of the game window
    - player location on map x value(negative value means random) - cannot be outside of game boundaries
    - player location on map y value(negative value means random) - cannot be outside of game boundaries
    - title - title of the game window
    - background - this is the directory to the background image to scroll, should be in same dir as main driver
    - character spritesheet - this is the directory to the spritesheet you are using for your character, same as background for location
 #### How To Play:
     - Controls:
       - ↑ on keyboard to move up
       - ↓ on keyboard to move down
       - ← on keyboard to move left
       - → on keyboard to move right
       - Space Bar - shoot projectile in direction you are moving
  
##### Notes:
  - Make sure you import
    - pygame
    - random
    - json
    - pprint
    - sys
    - os
    - math
    - time
    - helper_module.py
    
   #### Output Images:
   <img src="deathbarrier2.png" width="500">
   <img src="deathbarrier1.png" width="500">
 



