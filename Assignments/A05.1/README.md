# Printing Stat Cards(Assignment 4)
Travis Bales

## Description:
Using command line parameters set the screen size, title, color of the background, and size of sprite used in window.
The sprite is allowed to follow the mouse and be moved with the keyboard. The sprite is not allowed to go outside of view
<br>
- **Using python 3.8.3**

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|1| [game.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A05.1/game.py) |The main driver that launches the gui to produces the game window|
|2|[shot1.png](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A05.1/Shot1.png)| screenshot showing how it looks with sprite rendered|
|3|[shot2.png](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A05.1/shot2.png)|Screenshot of game screen with different color in different location|
|4|[shot3.png](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A05.1/shot3.png)|third screenshot of screen, notice the sprite is at the lowest point it can go

<br>

#### How to Run:
  - Download game.py to desktop
  - change director to that location. Ex. cd C:\Users\"your user"\Desktop
  - type "main.py" title="whatever you want" width=640 height=480 220,122,122 size=70
  
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
  - My program expects five parameters to be placed on the command line when you run the program.
  - Parameters
    - title - the title of the game window
    - width - the width of the screen resolution
    - height - the height of the screen resolution
    - background color - the RGB value of the background window
    - size of sprite - the size of the cube you will use, the number will be both length and width
    
   ##### Output Images:
   <img src="Shot1.png" width="640">
   <img src="shot2.png" width="640">
   <img src="shot3.png" width="640">
