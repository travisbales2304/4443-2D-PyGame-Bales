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
|2|[200x200 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/200x200.png)||
|3|[300x300 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/300x300.png)||
|4|[400x400 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/300x300.png)||
|5|[500x500 screen size](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/500x500.png)||
|6|[Double Barrier](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/DoubleBarrier.png)||
|7|[Left Barrier](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/LeftBarrier.png)||
|8|[Right Barrier](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/rightBarrier.png)||
|8|[Barrier Message](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.02/barrierMessage.png)||


<br>

#### How to Run:
  - Download game.py to desktop
  - change director to that location. Ex. cd C:\Users\"your user"\Desktop
  - type "main.py" title="whatever you want" width=640 height=480 220,122,122 size=70
  - My program expects five parameters to be placed on the command line when you run the program.
  - Parameters
    - title - the title of the game window
    - width - the width of the screen resolution
    - height - the height of the screen resolution
    - background color - the RGB value of the background window
    - size of sprite - the size of the cube you will use, the number will be both length and width
 #### How To Play:
   - The game starts off by the sprite following the mouse, click on the screen to toggle this feature
     - When you click it starts/stops the sprite from following the mouse
   - If you want to use keyboard you need to disable follow mouse by clicking once
     - Controls:
       - ↑ on keyboard to move up
       - ↓ on keyboard to move down
       - ← on keyboard to move left
       - → on keyboard to move right
       - Left Mouse Button(LMB) to toggle sprite to follow mouse
  
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
  - It only uses a rectangle for the sprite at the moment because images are hard to control
    
   ##### Output Images:
   <img src="Shot1.png" width="640">
   <img src="shot2.png" width="640">
   <img src="shot3.png" width="640">

