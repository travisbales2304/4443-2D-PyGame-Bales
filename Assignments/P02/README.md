# Platformer with scrolling background, pickup keys, and 3 levels
Travis Bales

## Description:
This is a platformer game that uses jumping to get to the end of the level. You must also collect the key for the first two levels.
If you die 15 times in one level, the game ends. IF you beat the third level you win the game!
<br>
- **Using python 3.8.3**

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|1| [TiledGame.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/TiledGame.py) |The main driver that launches the gui to produces the game window and handles game logic|
|2|[pygame_functions.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/pygame_functions.py)|Helper module provided by StevePaget |
|3|[Settings.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/settings.py)|Settings File used for variables|
|4|[SpriteHandler.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/SpriteHandler.py)|File that handles all sprites in game|
|5|[MapCreator.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/MapCreator.py)|Python file that reads and generates a map|
|6|[Map3.txt](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/Map3.txt)|Third map used in the game|
|7|[Map2.txt](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/Map2.txt)|Second map used in the game|
|8|[Map.txt](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P02/Map.txt)|first Map used in the game|
|9|[Sounds](https://github.com/travisbales2304/4443-2D-PyGame-Bales/tree/master/Assignments/P02/Sounds)|All Sound files Used in game|
|10|[Kings and Pigs](https://github.com/travisbales2304/4443-2D-PyGame-Bales/tree/master/Assignments/P02/Kings%20and%20Pigs/Sprites)|Sprites for boxes and player|
|11|[Basic Frames](https://github.com/travisbales2304/4443-2D-PyGame-Bales/tree/master/Assignments/P02/BasicFrames)|Sprites for building the environment|
|12|[Screeshot1](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/shot1.png)|Shooting to the right |
|13|[Screenshot2](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/shot2.png)|Shooting down|
|14|[Screenshot3](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/shot3.png)|Shooting to the left|
|15|[Screenshot4](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/P1.04/shot4.png)|Shooting up|
<br>


#### How to Run:
  - Download all python files to desktop
  - Download all other files to Desktop
  - change directory to that location. Ex. cd C:\Users\"your user"\Desktop
  - type "TiledGame.py" in the commandline
  - My program takes zero parameters
 #### How To Play:
     - Controls:
       - ↑ on keyboard to jump
       - ← on keyboard to move left
       - → on keyboard to move right
       - Space Bar - to end game on screen popup
  
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
   |#|#|
   |:--:|---|
   |<img src="shot1.png" width="400">|<img src="shot2.png" width="400">|
   |<img src="shot3.png" width="400">|<img src="shot4.png" width="400">|
 

