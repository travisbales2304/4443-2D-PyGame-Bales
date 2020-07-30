# Movable sprite with Edge Detection(Project 1.02)
Travis Bales

## Description:
Using command line parameters set the screen size, title, color of the background, and size of sprite used in window.
The sprite is allowed to move around within the map boundaries and upon hitting the edge, a map boundary will appear and a message will appear
<br>
- **Using python 3.8.3**

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|1| [game_pt2.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/game_pt2.py) |The main driver that launches the gui to produces the game window|
|2|[Helper_Module.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/helper_module.py)|Helper module provided by Dr. Griffin|
|3|[200x200 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/200x200.png)|game with 200x200 screen size|
|4|[300x300 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/300x300.png)|game with 300x300 screen size|
|5|[400x400 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/300x300.png)|game with 400x400 screen size|
|6|[500x500 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/500x500.png)|game with 500x500 screen size|
|7|[Double Barrier](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/DoubleBarrier.png)|double barrier example|
|8|[Left Barrier](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/LeftBarrier.png)|left map barrier example|
|9|[Right Barrier](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/rightBarrier.png)|right map barrier example|
|10|[Barrier Message](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/barrierMessage.png)|barrier message example|


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
    
   ##### Output Images:
   <img src="200x200.png" width="200">
   <img src="300x300.png" width="300">
   <img src="400x400.png" width="400">
   <img src="500x500.png" width="400">
   <img src="LeftBarrier.png" width="400">
   <img src="rightBarrier.png" width="400">
   <img src="DoubleBarrier.png" width="400">
   <img src="barrierMessage.png" width="400">


