# Printing Stat Cards(Assignment 4)
Travis Bales

## Description:
Using command line parameters open a json file to load data about a character. Print that data to the screen using a label
Also use dictionaries with key value pairs to parse the json object.
<br>
- **Using python 3.8.3**

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|1| [main.py](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A04/Main.py) |The main driver that launches the gui to produce hello world|
|2|[playerInfo.Json](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A04/playerInfo.json)| The json file that holds the character information|
|3|[A04.png](https://github.com/travisbales2304/4443-2D-PyGame-Bales/blob/master/Assignments/A04/A04.png)|Screenshot of expected output|

<br>

#### How to Run:
  - Download main.py to desktop
  - Download playerinfo.json to desktop
  - change director to that location. Ex. cd C:\Users\"your user"\Desktop
  - type "main.py" playerinfo.json
  
##### Notes:
  - Make sure you import
    - tkinter as tk
    - json
    - sys
  - My program expects one parameter to be placed on the command line when you run the program.
  - Parameters `<input file>` this is a json file
  - The input file should be in the same directory as main.py
  - you can use your own json file if it follows the same structur
  - just use main.py "yourJsonFileName.json"
