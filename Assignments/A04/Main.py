#travis Bales
#assignment 4

import tkinter as tk
import json
import sys


class HelloWorldFramePlayerInfo(tk.Frame):
    def __init__(self,master,name):
        f = open(name)
        x = json.load(f)
        tk.Frame.__init__(self,master)
        self.grid()
        counter = 0
        for key in x:
            value = x[key]
            hello = tk.Label(self,text = "{} : {}".format(key,value),anchor="w",width=60)
            hello.grid(row=counter, column=0)
            counter += 1
            print("{} {}".format(key, value))
        f.close()

# Spawn window
if __name__ == "__main__":
    #check if there are too many arguments
    if(len(sys.argv)>2):
        sys.exit('Incorrect Parameters')
    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("Player Stats")
    # Instantiate HelloWorldFramePlayerInfo object with command line arg
    hello_frame = HelloWorldFramePlayerInfo(root,sys.argv[1])
    # Start GUI
    hello_frame.mainloop()
