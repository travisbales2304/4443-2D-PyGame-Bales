'''
Travis Bales
Project 1.04
Goal: Create a pygame that scolls the background (except when close to the edge)
and have animations for movement and shooting as well as sounds.
'''


#Import helper functions, source cited in the helper function file
from pygame_functions_clean import *
import math, random, time

#initialize the screen size, background color, and background image
#(image overlaps the color) and sets our tracking variables to 0 for 
#scrolling around the scrool
screenSize(int(sys.argv[1]),int(sys.argv[2]))
setBackgroundColour("pink")
setBackgroundImage('bg.png')
Trackerx = 0
Trackery = 0




#sets the window title
setWindowTitle(sys.argv[3])


#Set's the sprite that presents when the player is close to the wall
player2 = makeSprite('linkWall.png',8)
#displays the sprite to be written
showSprite(player2)
#moves the sprite and then refreshes the display
moveSprite(player2,int(sys.argv[1]) // 2,int(sys.argv[2]) // 2,1)


#Entities created for our game
#boundary[1-4] are the boundaries around the map
#shotsound is the sound when you shoot
#splosion is the sound when you hit an enemy
#bullet is the sprite of the bullet
player = makeSprite(sys.argv[4],32)
bullet = makeSprite('Bullet.png',5)
bullet2 = makeSprite('Bullet2.png',5)
Boundary = makeSprite('TopBotBarrier.png')
Boundary2 = makeSprite('RightLeftBarrier.png')
Boundary3 = makeSprite('RightLeftBarrier.png')
Boundary4 = makeSprite('TopBotBarrier.png')
shotsound = makeSound('RockShot.wav')
splosion = makeSound('Splosion.wav')
#walk = makeSound('Walk2.wav')
#initialize the bullet coords
bullet.x = 200
bullet.y = 200

#initialize the boundary coords
Boundary.x = -500
Boundary.y = 0
Boundary2.x = 3189
Boundary2.y = 79
Boundary3.x = -500
Boundary3.y = 50
Boundary4.x = -500
Boundary4.y = 3789
#move all entities to their location and show them
moveSprite(Boundary,Boundary.x,Boundary.y)
moveSprite(Boundary2,Boundary2.x,Boundary2.y)
moveSprite(Boundary3,Boundary3.x,Boundary3.y)
moveSprite(Boundary4,Boundary4.x,Boundary4.y)
showSprite(Boundary)
showSprite(Boundary2)
showSprite(Boundary3)
showSprite(Boundary4)
#check if the amount of entities is an even number or odd
#if not even then add one to it(neccessary for logic)
number = 6
enemies = []
if int(sys.argv[5]) % 2 != 0:
    number = int(sys.argv[5]) + 1
else:
    number = int(sys.argv[5])
#creates enemies and adds them to the list
for x in range(number):
    thisEnemy = makeSprite("BardoFull.png",14)
    #addSpriteImage(thisEnemy, "enemy1.png")
    thisEnemy.x = random.randint(0,1000)
    thisEnemy.y = random.randint(0,750)
    thisEnemy.alive = True
    thisEnemy.counter = 0
    moveSprite(thisEnemy, thisEnemy.x, thisEnemy.y)
    thisEnemy.xspeed = 1
    thisEnemy.yspeed = 1
    showSprite(thisEnemy)
    enemies.append(thisEnemy)

changeSpriteImage(bullet,2)
#showSprite(bullet)

#sets up the player sprite location and adds the labels for approaching a wall
showSprite(player)
moveSprite(player,int(sys.argv[1]) // 2,int(sys.argv[2]) // 2,1)
textlabel1 = makeLabel("Close to Right Wall", 22,200,220,"red", font="impact")
textlabel2 = makeLabel("Close to Top Wall", 22,200,200,"red", font="impact")
textlabel3 = makeLabel("Close to Left Wall", 22,200,180,"red", font="impact")
textlabel4 = makeLabel("Close to Bottom Wall", 22,200,160,"red", font="impact")






def main(**kwargs):
    spritecount = 0
    global Trackerx    #global tracker vaiable used throughout
    global Trackery    #global Tracker variable
    barrier = False    #bool that represents if the player has hit a barrier
    StopScrolling = False #bool that tells us if we can scroll the background, true = we can, false = we can't
    lockshooting = False #bool to lock the shoot button, if true you cannot shoot
    ShotDirection = "None" #last shoot direction to find out where the missile should go
    flipper = 0            #flip flop used in logic
    nextFrame = clock()    #keeps the frame timing
    frame=0                 #frame number
    tempx = 300             #temporary location for when you stop scrolling on the x coord
    tempy = 300             #temporary locatin for when you stop scrolling on the Y coord
    while True:
        if clock() > nextFrame:                         # We only animate our character every 80ms.
            frame = (frame+1)%8                         # There are 8 frames of animation in each direction
            nextFrame += 80                             # so the modulus 8 allows it to loop
            print(str(Trackerx)+ " " + str(Trackery) + " Tempx: " + str(tempx) + " tempy: "  + str(tempy) + " " + str(number)) #Testing Purposes
        barrier = False
        StopScrolling = False
        #checks to see if we need to print a barrier message
        if tempx >= 480:
            showLabel(textlabel1)
            barrier = True
            StopScrolling = True
        else:
            hideLabel(textlabel1)
        if tempy == 135:
            barrier = True
            StopScrolling = True
            showLabel(textlabel2)
        else: hideLabel(textlabel2)
        if tempy == 500:
            barrier = True
            StopScrolling = True
            showLabel(textlabel4)
        else:hideLabel(textlabel4)
        if tempx == 75:
            barrier = True
            StopScrolling = True
            showLabel(textlabel3)
        else:hideLabel(textlabel3)
        if not barrier:
            hideSprite(player2)
            showSprite(player)
        else:
            hideSprite(player)
            showSprite(player2)

        
        #All key events handle the following:
            #for each key pressed it flip flops the lockshooting bool
            #then sets the bullet coords to theplayer location and moves the bullet there
            #if it's not locked for shooting it plays the shoot sound and sets the direction to be sent off.
            #tracks the logic for when close to barriers to stop scrolling and then start moving the character
        if keyPressed("right"):
            if keyPressed('space'):
                lockshooting = not lockshooting
                bullet.x = tempx - 50
                bullet.y = tempy - 50
                moveSprite(bullet,bullet.x,bullet.y)
                rotateSprite(bullet,90)
                hideSprite(bullet2)
                showSprite(bullet)
            if not lockshooting:
                #playSound(shotsound)
                lockshooting = True
                ShotDirection = "right"
            if Trackerx < 2675 and tempx == 300:
                Boundary.x -= 5
                Boundary2.x -= 5
                Boundary3.x -= 5
                Boundary4.x -= 5
                moveSprite(Boundary,Boundary.x,Boundary.y)
                moveSprite(Boundary2,Boundary2.x,Boundary2.y)
                moveSprite(Boundary3,Boundary3.x,Boundary3.y)
                moveSprite(Boundary4,Boundary4.x,Boundary4.y)
                Trackerx += 5
                scrollBackground(-5,0)  
                for thisEnemy in enemies:
                    thisEnemy.x -= 5
                changeSpriteImage(player, 0*8+frame)
            if Trackerx >= 2675 and tempx <= 480:
                tempx += 5
                changeSpriteImage(player, 0*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)
            elif Trackerx <= -80 and tempx < 300:
                tempx += 5
                changeSpriteImage(player, 0*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)

                

        elif keyPressed("down"):
            if keyPressed('space'):
                lockshooting = not lockshooting
                bullet.x = tempx - 50
                bullet.y = tempy - 50
                moveSprite(bullet,bullet.x,bullet.y)
                rotateSprite(bullet,180)
                hideSprite(bullet2)
                showSprite(bullet)
            if not lockshooting:
                lockshooting = True
                ShotDirection = "down"
            if Trackery < 3240 and tempy == 300:
                Boundary.y -= 5
                Boundary2.y -= 5
                Boundary3.y -= 5
                Boundary4.y -= 5
                moveSprite(Boundary,Boundary.x,Boundary.y)
                moveSprite(Boundary2,Boundary2.x,Boundary2.y)
                moveSprite(Boundary3,Boundary3.x,Boundary3.y)
                moveSprite(Boundary4,Boundary4.x,Boundary4.y)
                Trackery += 5
                scrollBackground(0, -5)
                for thisEnemy in enemies:
                    thisEnemy.y -= 5
                changeSpriteImage(player, 1*8+frame)
            if Trackery >= 3240 and tempy >=300 and tempy < 500:
                tempy += 5
                changeSpriteImage(player, 1*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)
            elif Trackery <= 0 and tempy < 300:
                tempy += 5
                changeSpriteImage(player, 1*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)


            

        elif keyPressed("left"):
            if keyPressed('space'):
                lockshooting = not lockshooting
                bullet.x = tempx - 50
                bullet.y = tempy - 50
                moveSprite(bullet,bullet.x,bullet.y)
                rotateSprite(bullet,-90)
                hideSprite(bullet2)
                showSprite(bullet)
            if not lockshooting:
                lockshooting = True
                ShotDirection = "left"
            if Trackerx > -435 and tempx == 300:
                Boundary.x += 5
                Boundary2.x += 5
                Boundary3.x += 5
                Boundary4.x += 5
                moveSprite(Boundary,Boundary.x,Boundary.y)
                moveSprite(Boundary2,Boundary2.x,Boundary2.y)
                moveSprite(Boundary3,Boundary3.x,Boundary3.y)
                moveSprite(Boundary4,Boundary4.x,Boundary4.y)
                Trackerx -= 5
                scrollBackground(5,0)
                for thisEnemy in enemies:
                    thisEnemy.x += 5
                changeSpriteImage(player, 2*8+frame)
            if Trackerx >= 2675 and tempx > 300:
                tempx -= 5
                changeSpriteImage(player, 2*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)
            elif Trackerx == -435 and tempx >= 80:
                tempx -= 5
                changeSpriteImage(player, 2*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)

            


            

        elif keyPressed("up"):
            if keyPressed('space'):
                lockshooting = not lockshooting
                bullet.x = tempx - 50
                bullet.y = tempy - 50
                moveSprite(bullet2,bullet.x,bullet.y)
                hideSprite(bullet)
                showSprite(bullet2)
            if not lockshooting:
                lockshooting = True
                ShotDirection = "up"
            if Trackery > 0 and tempy == 300:
                Boundary.y += 5
                Boundary2.y += 5
                Boundary3.y += 5
                Boundary4.y += 5
                moveSprite(Boundary,Boundary.x,Boundary.y)
                moveSprite(Boundary2,Boundary2.x,Boundary2.y)
                moveSprite(Boundary3,Boundary3.x,Boundary3.y)
                moveSprite(Boundary4,Boundary4.x,Boundary4.y)
                Trackery -= 5
                scrollBackground(0,5)
                for thisEnemy in enemies:
                    thisEnemy.y += 5
                changeSpriteImage(player,3*8+frame)
            if Trackery >= 3240 and tempy >= 300:
                tempy -=5
                changeSpriteImage(player,3*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)
            elif Trackery <= 0 and tempy >= 140:
                tempy -=5
                changeSpriteImage(player,3*8+frame)
                moveSprite(player,tempx,tempy,1)
                moveSprite(player2,tempx,tempy,1)


            

        
        #if we are doing nothing we update the player with idle frames
        else:
            #stopSound(walk)
            changeSpriteImage(player, 1 * 8 + 5)
            changeSpriteImage(player2,frame%5)

        #updates the bullet location for each frame and sets it in the right direction
        if bullet.x == 250 and bullet.y == 250:
            playSound(shotsound)
            time.sleep(.05)
        if ShotDirection == "right":
            bullet.x += 5
        elif ShotDirection == "left":
            bullet.x -= 5
        elif ShotDirection == "up":
            bullet.y -= 5
        elif ShotDirection == "down":
            bullet.y += 5
        #chets to see if the enemy is alive and checks to see if a projectile hit an enemy.
        #if an enemy has been hit it plays the death animation and hides the sprite after a short while
        #plays the exlosion sound upon impact 
        for thisEnemy in enemies:
            if thisEnemy.alive == False:
                thisEnemy.counter += 1
                if thisEnemy.counter >= 200:
                    hideSprite(thisEnemy)
            if flipper == 0 and thisEnemy.alive == True:
                thisEnemy.x += thisEnemy.xspeed
                if thisEnemy.x > 1000:
                    thisEnemy.x = 0
                elif thisEnemy.x < 0:
                    thisEnemy.x = 1000
                changeSpriteImage(thisEnemy,(frame%4))
                moveSprite(thisEnemy, thisEnemy.x, thisEnemy.y)
            if flipper == 1 and thisEnemy.alive == True:
                thisEnemy.y += thisEnemy.yspeed
                if thisEnemy.y > 750:
                    thisEnemy.y = 0
                elif thisEnemy.y < 0:
                    thisEnemy.y = 750
                changeSpriteImage(thisEnemy,frame%4)
                moveSprite(thisEnemy, thisEnemy.x, thisEnemy.y)
            if flipper == 0: flipper = 1
            else: flipper = 0
            if abs(thisEnemy.x - bullet.x) <= 30 and abs(thisEnemy.y - bullet.y) <= 30:
                thisEnemy.alive = False
                changeSpriteImage(thisEnemy,13)
                stopSound(shotsound)
                playSound(splosion)
                #hideSprite(thisEnemy)
                hideSprite(bullet)
                hideSprite(bullet2)
            moveSprite(thisEnemy, thisEnemy.x, thisEnemy.y)
                
        changeSpriteImage(bullet,frame%5)
        moveSprite(bullet,bullet.x,bullet.y)
        moveSprite(bullet2,bullet.x,bullet.y)
        updateDisplay()
        spritecount+=1
        tick(120)

    endWait()

if __name__=='__main__':
    if(len(sys.argv)>7):
        pass
        #sys.exit('Too many Params')

    main()
