"""
CITATION FOR CUBE SOLVING ALGORITHIM:

Used very heavily -
Website 1: https://www.youtube.com/watch?v=1t1OL2zN0LQ
Website 2: https://www.youtube.com/watch?v=1t1OL2zN0LQ

Not really used -
Website 3: http://ozcubegirl.com/rubikscubesolution.html
"""
from moves import *

def whiteDaisy(data):
    # ONE MOVE DAISY FIT
    if(data.cube[1][0][1] == "WHITE" and data.cube[2][0][1] != "WHITE"):
        print("Top prime")
        topPrime(data)
    elif(data.cube[3][0][1] == "WHITE" and data.cube[2][0][1] != "WHITE"):
        print("Top")
        top(data)
    elif(data.cube[1][2][1] == "WHITE" and data.cube[2][2][1] != "WHITE"):
        print("Down")
        down(data)
    elif(data.cube[3][2][1] == "WHITE" and data.cube[2][2][1] != "WHITE"):
        print("Down prime")
        downPrime(data)
    elif(data.cube[4][0][1] == "WHITE" and data.cube[2][1][0] != "WHITE"):
        print("Right")
        right(data)
    elif(data.cube[5][2][1] == "WHITE" and data.cube[2][1][0] != "WHITE"):
        print("Right prime")
        rightPrime(data)
    elif(data.cube[4][2][1] == "WHITE" and data.cube[2][1][2] != "WHITE"):
        print("Left prime")
        leftPrime(data)
    elif(data.cube[5][0][1] == "WHITE" and data.cube[2][1][2] != "WHITE"):
        print("Left")
        left(data)
    # TWO MOVE DAISY FIT
    elif(data.cube[0][0][1] == "WHITE" and data.cube[2][0][1] != "WHITE"):
        print("Top x2")
        top(data)
        top(data)
    elif(data.cube[0][2][1] == "WHITE" and data.cube[2][2][1] != "WHITE"):
        print("Down x2")
        down(data)
        down(data)
    elif(data.cube[0][1][2] == "WHITE" and data.cube[2][1][0] != "WHITE"):
        print("Right x2")
        right(data)
        right(data)
    elif(data.cube[0][1][0] == "WHITE" and data.cube[2][1][2] != "WHITE"):
        print("Left x2")
        left(data)
        left(data)
    # FACE ROTATION TO ONE/TWO MOVE DAISY FIT
    elif((data.cube[5][0][1] == "WHITE" or data.cube[4][2][1] == "WHITE" or data.cube[0][1][0] == "WHITE") and data.cube[2][2][1] != "WHITE"):
        print("Back prime")
        backPrime(data)
    elif((data.cube[4][0][1] == "WHITE" or data.cube[5][2][1] == "WHITE" or data.cube[0][1][2] == "WHITE") and data.cube[2][2][1] != "WHITE"):
        print("Back")
        back(data)
    elif((data.cube[1][0][1] == "WHITE" or data.cube[3][0][1] == "WHITE" or data.cube[0][0][1] == "WHITE") and data.cube[2][2][1] != "WHITE"):
        print("Back x2")
        back(data)
        back(data)
        
    elif((data.cube[1][0][1] == "WHITE" or data.cube[3][0][1] == "WHITE" or data.cube[0][0][1] == "WHITE") and data.cube[2][1][0] != "WHITE"):
        print("Back")
        back(data)
    elif((data.cube[1][2][1] == "WHITE" or data.cube[3][2][1] == "WHITE" or data.cube[0][2][1] == "WHITE") and data.cube[2][1][0] != "WHITE"):
        print("Back prime")
        backPrime(data)
    elif((data.cube[5][0][1] == "WHITE" or data.cube[4][2][1] == "WHITE" or data.cube[0][1][0] == "WHITE") and data.cube[2][1][0] != "WHITE"):
        print("Back x2")
        back(data)
        back(data)
    
    elif((data.cube[4][0][1] == "WHITE" or data.cube[5][2][1] == "WHITE" or data.cube[0][1][2] == "WHITE") and data.cube[2][0][1] != "WHITE"):
        print("Back prime")
        backPrime(data)
    elif((data.cube[5][0][1] == "WHITE" or data.cube[4][2][1] == "WHITE" or data.cube[0][1][0] == "WHITE") and data.cube[2][0][1] != "WHITE"):
        print("Back")
        back(data)
    elif((data.cube[1][2][1] == "WHITE" or data.cube[3][2][1] == "WHITE" or data.cube[0][2][1] == "WHITE") and data.cube[2][0][1] != "WHITE"):
        print("Back x2")
        back(data)
        back(data)
    
    elif((data.cube[1][0][1] == "WHITE" or data.cube[3][0][1] == "WHITE" or data.cube[0][0][1] == "WHITE") and data.cube[2][1][2] != "WHITE"):
        print("Back prime")
        backPrime(data)
    elif((data.cube[1][2][1] == "WHITE" or data.cube[3][2][1] == "WHITE" or data.cube[0][2][1] == "WHITE") and data.cube[2][1][2] != "WHITE"):
        print("Back")
        back(data)
    elif((data.cube[4][0][1] == "WHITE" or data.cube[5][2][1] == "WHITE" or data.cube[0][1][2] == "WHITE") and data.cube[2][1][2] != "WHITE"):
        print("Back x2")
        back(data)
        back(data)
    # NOT IN THE ROW I NEED, BUT ALSO NOT TOUCHING THE YELLOW SIDE
    elif(data.cube[1][1][0] == "WHITE" and data.cube[2][1][0] != "WHITE"):
        print("Face prime")
        print("Top prime")
        print("Right")
        print("Top")
        facePrime(data)
        topPrime(data)
        right(data)
        top(data)
    elif(data.cube[3][1][2] == "WHITE" and data.cube[2][1][2] != "WHITE"):
        print("Face")
        print("Top")
        print("Left prime")
        print("Top prime")
        face(data)
        top(data)
        leftPrime(data)
        topPrime(data)
    elif(data.cube[4][1][2] == "WHITE" and data.cube[2][0][1] != "WHITE"):
        print("Face prime")
        print("Left prime")
        print("Top")
        print("Left")
        facePrime(data)
        leftPrime(data)
        top(data)
        left(data)
    elif(data.cube[5][1][2] == "WHITE" and data.cube[2][2][1] != "WHITE"):
        print("Face prime")
        print("Right prime")
        print("Down")
        print("Right")
        facePrime(data)
        rightPrime(data)
        down(data)
        right(data)
    elif(data.cube[1][1][2] == "WHITE" and data.cube[2][1][0] != "WHITE"):
        print("Right")
        right(data)
    elif(data.cube[3][1][0] == "WHITE" and data.cube[2][1][2] != "WHITE"):
        print("Left")
        left(data)
    elif(data.cube[4][1][0] == "WHITE" and data.cube[2][0][1] != "WHITE"):
        print("Top")
        top(data)
    elif(data.cube[5][1][0] == "WHITE" and data.cube[2][2][1] != "WHITE"):
        print("Down")
        down(data)
    else:
        print("Back")
        back(data)

def whiteT(data):
    if(data.cube[4][1][0] == data.cube[4][1][1] and data.cube[0][0][1] != "WHITE"):
        print("Top x2")
        top(data)
        top(data)
    elif(data.cube[1][1][2] == data.cube[1][1][1] and data.cube[0][1][2] != "WHITE"):
        print("Right x2")
        right(data)
        right(data)
    elif(data.cube[5][1][0] == data.cube[5][1][1] and data.cube[0][2][1] != "WHITE"):
        print("Down x2")
        down(data)
        down(data)
    elif(data.cube[3][1][0] == data.cube[3][1][1] and data.cube[0][1][0] != "WHITE"):
        print("Left x2")
        left(data)
        left(data)
    if(data.cube[0][0][1] == "WHITE" and data.cube[0][1][2] == "WHITE" and data.cube[0][2][1] == "WHITE" and data.cube[0][1][0] == "WHITE" and data.cube[1][1][0] != data.cube[1][1][1]):
        print("Front")
        front(data)
    else:
        print("Back")
        back(data)

def whiteFace(data):
    # In the spots we want
    # All good
    if(data.cube[3][0][0] == "WHITE" and data.cube[4][2][0] == data.cube[4][1][1]):
        print("Back")
        print("Top")
        print("Back prime")
        print("Top prime")
        back(data)
        top(data)
        backPrime(data)
        topPrime(data)
    # All good
    elif(data.cube[1][2][2] == "WHITE" and data.cube[5][2][0] == data.cube[5][1][1]):
        print("Back")
        print("Down")
        print("Back prime")
        print("Down prime")
        back(data)
        down(data)
        backPrime(data)
        downPrime(data)
    # All good
    elif(data.cube[4][2][0] == "WHITE" and data.cube[3][0][0] == data.cube[3][1][1]):
        print("Back prime")
        print("Left prime")
        print("Back")
        print("Left")
        backPrime(data)
        leftPrime(data)
        back(data)
        left(data)
    # All good
    elif(data.cube[3][2][0] == "WHITE" and data.cube[5][0][0] == data.cube[5][1][1]):
        print("Back prime")
        print("Down prime")
        print("Back")
        print("Down")
        backPrime(data)
        downPrime(data)
        back(data)
        down(data)
    # All good
    elif(data.cube[1][0][2] == "WHITE" and data.cube[4][0][0] == data.cube[4][1][1]):
        print("Back prime")
        print("Top prime")
        print("Back")
        print("Top")
        backPrime(data)
        topPrime(data)
        back(data)
        top(data)
    # All good
    elif(data.cube[4][0][0] == "WHITE" and data.cube[1][0][2] == data.cube[1][1][1]):
        print("Back")
        print("Right")
        print("Back prime")
        print("Right prime")
        back(data)
        right(data)
        backPrime(data)
        rightPrime(data)
    # All good
    elif(data.cube[5][2][0] == "WHITE" and data.cube[1][2][2] == data.cube[1][1][1]):
        print("Back prime")
        print("Right prime")
        print("Back")
        print("Right")
        backPrime(data)
        rightPrime(data)
        back(data)
        right(data)
    # All good
    elif(data.cube[5][0][0] == "WHITE" and data.cube[3][2][0] == data.cube[3][1][1]):
        print("Back")
        print("Left")
        print("Back prime")
        print("Left prime")
        back(data)
        left(data)
        backPrime(data)
        leftPrime(data)
    # If the white is touching the face it should end on
    elif(data.cube[5][2][2] == "WHITE"):
        print("Down")
        print("Back")
        print("Down prime")
        down(data)
        back(data)
        downPrime(data)
    elif(data.cube[1][2][0] == "WHITE"):
        print("Right prime")
        print("Back")
        print("Right")
        rightPrime(data)
        back(data)
        right(data)
    elif(data.cube[1][0][0] == "WHITE"):
        print("Right")
        print("Back")
        print("Right prime")
        right(data)
        back(data)
        rightPrime(data)
    elif(data.cube[4][0][2] == "WHITE"):
        print("Top prime")
        print("Back")
        print("Top")
        topPrime(data)
        back(data)
        top(data)
    elif(data.cube[4][2][2] == "WHITE"):
        print("Top")
        print("Back")
        print("Top prime")
        top(data)
        back(data)
        topPrime(data)
    elif(data.cube[3][0][2] == "WHITE"):
        print("Left prime")
        print("Back prime")
        print("Left")
        leftPrime(data)
        backPrime(data)
        left(data)
    elif(data.cube[3][2][2] == "WHITE"):
        print("Left")
        print("Back prime")
        print("Left prime")
        left(data)
        backPrime(data)
        leftPrime(data)
    elif(data.cube[5][0][2] == "WHITE"):
        print("Down prime")
        print("Back prime")
        print("Down")
        downPrime(data)
        backPrime(data)
        down(data)
    # If the white is on the face opposite of what it should be
    elif(data.cube[2][2][0] == "WHITE" and data.cube[0][2][2] != "WHITE" and data.cube[1][0][2] != "WHITE"):
        print("Down")
        print("Back x2")
        print("Down prime")
        down(data)
        back(data)
        back(data)
        downPrime(data)
    elif(data.cube[2][0][0] == "WHITE" and data.cube[0][0][2] != "WHITE" and data.cube[4][2][0] != "WHITE"):
        print("Right")
        print("Back x2")
        print("Right prime")
        right(data)
        back(data)
        back(data)
        rightPrime(data)
    elif(data.cube[2][0][2] == "WHITE" and data.cube[0][0][0] != "WHITE" and data.cube[4][0][0] != "WHITE"):
        print("Left prime")
        print("Back back x2")
        print("Left")
        leftPrime(data)
        back(data)
        back(data)
        left(data)
    elif(data.cube[2][2][2] == "WHITE" and data.cube[0][2][0] != "WHITE" and data.cube[3][0][0] != "WHITE"):
        print("Down prime")
        print("Back x2")
        print("Down")
        downPrime(data)
        back(data)
        back(data)
        down(data)
    elif(data.cube[0][0][0] == data.cube[0][0][1] == data.cube[0][0][2] == data.cube[0][1][0] == data.cube[0][1][1] == data.cube[0][1][2] == data.cube[0][2][0] == data.cube[0][2][1] == data.cube[0][2][2]):
        redCorrect = data.cube[1][0][0] == data.cube[1][2][0] == data.cube[1][1][1]
        blueCorrect = data.cube[4][2][2] == data.cube[4][0][2] == data.cube[4][1][1]
        greenCorrect = data.cube[5][2][2] == data.cube[5][0][2] == data.cube[5][1][1]
        orangeCorrect = data.cube[3][0][2] == data.cube[3][2][2] == data.cube[3][1][1]
    
        if(not redCorrect):
            if(data.cube[1][0][0] != data.cube[1][1][1]):    
                print("Top prime")
                print("Back prime")
                print("Top")
                topPrime(data)
                backPrime(data)
                top(data)
            else:
                print("Down")
                print("Back")
                print("Down prime")
                down(data)
                back(data)
                downPrime(data)
        elif(not blueCorrect):
            if(data.cube[4][2][2] != data.cube[4][1][1]):
                print("Left prime")
                print("Back prime")
                print("Left")
                leftPrime(data)
                backPrime(data)
                left(data)
            else:
                print("Right")
                print("Back")
                print("Right prime")
                right(data)
                back(data)
                rightPrime(data)
        elif(not greenCorrect):
            if(data.cube[5][2][2] != data.cube[5][1][1]):
                print("Right prime")
                print("Back prime")
                print("Right")
                rightPrime(data)
                backPrime(data)
                right(data)
            else:
                print("Left")
                print("Back")
                print("Left prime")
                left(data)
                back(data)
                leftPrime(data)
        elif(not orangeCorrect):
            if(data.cube[3][0][2] != data.cube[3][1][1]):
                print("Down prime")
                print("Back prime")
                print("Down")
                downPrime(data)
                backPrime(data)
                down(data)
            else:
                print("Top")
                print("Back")
                print("Top prime")
                top(data)
                down(data)
                topPrime(data)
    else:
        print("Back")
        back(data)

def middleLayer(data):
    #print("MIDDLE LAYER")
    # --------------------RED LAYER PRIME CASE----------------------------------
    if(data.cube[1][1][2] == data.cube[1][1][1] and data.cube[2][1][0] != "YELLOW"):
        if(data.cube[2][1][0] == data.cube[5][1][1]):
            print("Back")
            
            print("Down")
            print("Back")
            print("Down prime")
            print("Back prime")
            
            print("Right prime")
            print("Back prime")
            print("Right")
            
            back(data)
            down(data)
            back(data)
            downPrime(data)
            backPrime(data)
            rightPrime(data)
            backPrime(data)
            right(data)
        else:
            print("Back prime")
            
            print("Top prime")
            print("Back prime")
            print("Top")
            print("Back")
            
            print("Right")
            print("Back")
            print("Right prime")
            
            backPrime(data)
            topPrime(data)
            backPrime(data)
            top(data)
            back(data)
            right(data)
            back(data)
            rightPrime(data)
    # --------------------ORANGE LAYER PRIME CASE-------------------------------
    elif(data.cube[3][1][0] == data.cube[3][1][1] and data.cube[2][1][2] != "YELLOW"):
        if(data.cube[2][1][2] == data.cube[4][1][1]):
            print("Back")
            
            print("Top")
            print("Back")
            print("Top prime")
            print("Back prime")
            
            print("Left prime")
            print("Back prime")
            print("Left")
            
            back(data)
            top(data)
            back(data)
            topPrime(data)
            backPrime(data)
            leftPrime(data)
            backPrime(data)
            left(data)
            
        else:
            print("Back prime")
            
            print("Down prime")
            print("Back prime")
            print("Down")
            print("Back")
            
            print("Left")
            print("Back")
            print("Left prime")
            
            backPrime(data)
            downPrime(data)
            backPrime(data)
            down(data)
            back(data)
            left(data)
            back(data)
            leftPrime(data)
    # --------------------GREEN LAYER PRIME CASE--------------------------------
    elif(data.cube[5][1][0] == data.cube[5][1][1] and data.cube[2][2][1] != "YELLOW"):
        if(data.cube[2][2][1] == data.cube[1][1][1]):
            print("Back prime")
            
            print("Right prime")
            print("Back prime")
            print("Right")
            print("Back")
            
            print("Down")
            print("Back")
            print("Down prime")
            
            backPrime(data)
            rightPrime(data)
            backPrime(data)
            right(data)
            back(data)
            down(data)
            back(data)
            downPrime(data)
        else:
            print("Back")
            
            print("Left")
            print("Back")
            print("Left prime")
            print("Back prime")
            
            print("Down prime")
            print("Back prime")
            print("Down")
            
            back(data)
            left(data)
            back(data)
            leftPrime(data)
            backPrime(data)
            downPrime(data)
            backPrime(data)
            down(data)
    
    # --------------------BLUE LAYER PRIME CASE---------------------------------
    elif(data.cube[4][1][0] == data.cube[4][1][1] and data.cube[2][0][1] != "YELLOW"):
        if(data.cube[2][0][1] == data.cube[3][1][1]):
            print("Back prime")
            
            print("Left prime")
            print("Back prime")
            print("Left")
            print("Back")
            
            print("Top")
            print("Back")
            print("Top prime")
            
            backPrime(data)
            leftPrime(data)
            backPrime(data)
            left(data)
            back(data)
            top(data)
            back(data)
            topPrime(data)
        else:
            print("Back")
            
            print("Right")
            print("Back")
            print("Right prime")
            print("Back prime")
            
            print("Top prime")
            print("Back prime")
            print("Top")
            back(data)
            right(data)
            back(data)
            rightPrime(data)
            backPrime(data)
            topPrime(data)
            backPrime(data)
            top(data)
    # --------------------NOW DEAL WITH YELLOWS---------------------------------
    # RED IS IN THE RIGHT PLACE BUT TOUCHING YELLOW
    elif(data.cube[1][1][2] == data.cube[1][1][1]):
        if(data.cube[1][0][1] != data.cube[1][1][1] or data.cube[1][2][1] != data.cube[1][1][1]):
            if(data.cube[1][0][1] == data.cube[1][1][1] and data.cube[4][0][1] == data.cube[4][1][1]):
                print("Back")
                
                print("Down")
                print("Back")
                print("Down prime")
                print("Back prime")
                
                print("Right prime")
                print("Back prime")
                print("Right")
                
                back(data)
                down(data)
                back(data)
                downPrime(data)
                backPrime(data)
                rightPrime(data)
                backPrime(data)
                right(data)
            else:
                print("Back prime")
                
                print("Top prime")
                print("Back prime")
                print("Top")
                print("Back")
                
                print("Right")
                print("Back")
                print("Right prime")
                
                backPrime(data)
                topPrime(data)
                backPrime(data)
                top(data)
                back(data)
                right(data)
                back(data)
                rightPrime(data)
        else:
            print("Back")
            back(data)
    # BLUE IS IN THE RIGHT PLACE BUT TOUCHING YELLOW
    elif(data.cube[4][1][0] == data.cube[4][1][1]):
        if(data.cube[4][2][1] != data.cube[4][1][1] or data.cube[4][0][1] != data.cube[4][1][1]):
            if(data.cube[4][2][1] == data.cube[4][1][1] and data.cube[3][0][1] == data.cube[3][1][1]):
                print("Back")
                
                print("Right")
                print("Back")
                print("Right prime")
                print("Back prime")
                
                print("Top prime")
                print("Back prime")
                print("Top")
                back(data)
                right(data)
                back(data)
                rightPrime(data)
                backPrime(data)
                topPrime(data)
                backPrime(data)
                top(data)
            else:
                print("Back prime")
                
                print("Left prime")
                print("Back prime")
                print("Left")
                print("Back")
                
                print("Top")
                print("Back")
                print("Top prime")
                
                backPrime(data)
                leftPrime(data)
                backPrime(data)
                left(data)
                back(data)
                top(data)
                back(data)
                topPrime(data)
        else:
            print("Back")
            back(data)
    # ORANGE IS IN THE RIGHT PLACE BUT TOUCHING YELLOW
    elif(data.cube[3][1][0] == data.cube[3][1][1]):
        if(data.cube[3][0][1] != data.cube[3][1][1] or data.cube[3][2][1] != data.cube[3][1][1]):
            if(data.cube[4][2][1] == data.cube[4][1][1] and data.cube[3][0][1] == data.cube[3][1][1]):
                print("Back prime")
                
                print("Down prime")
                print("Back prime")
                print("Down")
                print("Back")
                
                print("Left")
                print("Back")
                print("Left prime")
                
                backPrime(data)
                downPrime(data)
                backPrime(data)
                down(data)
                back(data)
                left(data)
                back(data)
                leftPrime(data)
            else:
                print("Back")
                
                print("Top")
                print("Back")
                print("Top prime")
                print("Back prime")
                
                print("Left prime")
                print("Back prime")
                print("Left")
                
                back(data)
                top(data)
                back(data)
                topPrime(data)
                backPrime(data)
                leftPrime(data)
                backPrime(data)
                left(data)
        else:
            print("Back")
            back(data)
    # GREEN IS IN THE RIGHT PLACE BUT TOUCHING YELLOW
    elif(data.cube[5][1][0] == data.cube[5][1][1]):
        if(data.cube[5][2][1] != data.cube[5][1][1] or data.cube[5][0][1] != data.cube[5][1][1]):
            if(data.cube[3][2][1] == data.cube[3][1][1] and data.cube[5][2][1] == data.cube[5][1][1]):
                print("Back prime")
                
                print("Right prime")
                print("Back prime")
                print("Right")
                print("Back")
                
                print("Down")
                print("Back")
                print("Down prime")
                
                backPrime(data)
                rightPrime(data)
                backPrime(data)
                right(data)
                back(data)
                down(data)
                back(data)
                downPrime(data)
            else:
                print("Back")
                
                print("Left")
                print("Back")
                print("Left prime")
                print("Back prime")
                
                print("Down prime")
                print("Back prime")
                print("Down")
                
                back(data)
                left(data)
                back(data)
                leftPrime(data)
                backPrime(data)
                downPrime(data)
                backPrime(data)
                down(data)
        # elif(data.cube[1][0][1] == data.cube[4][1][1]):
        #     # DO A THING
        # elif(data.cube)
        else:
            print("Back")
            back(data)
    # elif(data.cube[0][0][0] == data.cube[0][0][1] == data.cube[0][0][2] == data.cube[0][1][0] == data.cube[0][1][1] == data.cube[0][1][2] == data.cube[0][2][0] == data.cube[0][2][1] == data.cube[0][2][2]):
    #     redCorrect = data.cube[1][0][0] == data.cube[1][2][0] == data.cube[1][1][1]
    #     blueCorrect = data.cube[4][2][2] == data.cube[4][1][2] == data.cube[4][1][1]
    #     greenCorrect = data.cube[5][2][2] == data.cube[5][1][2] == data.cube[5][1][1]
    #     orangeCorrect = data.cube[3][0][2] == data.cube[3][2][2] == data.cube[3][1][1]
    # 
    #     if(not redCorrect):
    #         if(data.cube[1][0][0] != data.cube[1][1][1]):
    
    else:
        print("Back")
        back(data)
            
        
        
def yellowT(data):
    if(data.cube[2][0][1] == data.cube[2][1][1] and data.cube[2][2][1] == data.cube[2][1][1]):
        print("Back")
        back(data)
    elif(data.cube[2][1][0] == data.cube[2][1][1] and data.cube[2][1][2] == data.cube[2][1][1]):
        # Do the bar algorithim
        barAlg(data)
    elif(data.cube[2][0][1] == data.cube[2][1][1] and data.cube[2][1][0] == data.cube[2][1][1]):
        print("Back x2")
        back(data)
        back(data)
    elif(data.cube[2][0][1] == data.cube[2][1][1] and data.cube[2][1][2] == data.cube[2][1][1]):
        print("Back")
        back(data)
    elif(data.cube[2][1][0] == data.cube[2][1][1] and data.cube[2][2][1] == data.cube[2][1][1]):
        print("Back prime")
        backPrime(data)
    elif(data.cube[2][2][1] == data.cube[2][1][1] and data.cube[2][1][2] == data.cube[2][1][1]):
        angleAlg(data)
        # Do angle algorithim
    else:
        # Do the bar alogorithim
        barAlg(data)
        
def barAlg(data):
    print("Down")
    
    print("Left")
    print("Back")
    print("Left prime")
    print("Back prime")
    
    print("Down prime")
    down(data)
    left(data)
    back(data)
    leftPrime(data)
    backPrime(data)
    downPrime(data)
    
def angleAlg(data):
    print("Top")
    
    print("Back")
    print("Right")
    print("Back prime")
    print("Right prime")
    
    print("Top prime")
    
    top(data)
    back(data)
    right(data)
    backPrime(data)
    rightPrime(data)
    topPrime(data)
    
def yellowFace(data):
    # -------------PURE CROSS-------------
    if(data.cube[2][0][0] != "YELLOW" and data.cube[2][0][2] != "YELLOW" and data.cube[2][2][2] != "YELLOW" and data.cube[2][2][0] != "YELLOW"):
        while(data.cube[1][0][2] != "YELLOW" and data.cube[1][2][2] != "YELLOW"):
            print("Back")
            back(data)
        # DO HOWTOWEEKLY ALG AT 11:50
        print("Right")
        print("Back")
        print("Right prime")
        print("Back")
        print("Right")
        print("Back x2")
        print("Right prime")
        
        right(data)
        back(data)
        rightPrime(data)
        back(data)
        right(data)
        back(data)
        back(data)
        rightPrime(data)
    # ----------------FISH PATTERN---------------
    elif(data.cube[2][0][0] == "YELLOW" and data.cube[2][0][2] != "YELLOW" and data.cube[2][2][2] != "YELLOW" and data.cube[2][2][0] != "YELLOW"):
        # SPIN TO CORRECT FISH STATE
        print("Back")
        back(data)
    elif(data.cube[2][0][0] != "YELLOW" and data.cube[2][0][2] == "YELLOW" and data.cube[2][2][2] != "YELLOW" and data.cube[2][2][0] != "YELLOW"):
        # DO FISH ALG
        print("Right")
        print("Back")
        print("Right prime")
        print("Back")
        print("Right")
        print("Back x2")
        print("Right prime")
        
        right(data)
        back(data)
        rightPrime(data)
        back(data)
        right(data)
        back(data)
        back(data)
        rightPrime(data)
    elif(data.cube[2][0][0] != "YELLOW" and data.cube[2][0][2] != "YELLOW" and data.cube[2][2][2] == "YELLOW" and data.cube[2][2][0] != "YELLOW"):
        # SPIN TO CORRECT FISH STATE
        print("Back prime")
        backPrime(data)
    elif(data.cube[2][0][0] != "YELLOW" and data.cube[2][0][2] != "YELLOW" and data.cube[2][2][2] != "YELLOW" and data.cube[2][2][0] == "YELLOW"):
        # SPIN TO CORRECT FISH STATE
        print("Back x2")
        back(data)
        back(data)
    # ----------------FAT T PATTERN------------------
    elif(data.cube[2][0][2] == "YELLOW" and data.cube[2][2][2] == "YELLOW" and data.cube[2][0][0] != "YELLOW" and data.cube[2][2][0] != "YELLOW"):
        # DO THE FAT T ALG
        print("Down")
        print("Back")
        print("Down prime")
        print("Back")
        print("Down")
        print("Back x2")
        print("Down prime")
        down(data)
        back(data)
        downPrime(data)
        back(data)
        down(data)
        back(data)
        back(data)
        downPrime(data)
    elif(data.cube[2][0][2] != "YELLOW" and data.cube[2][2][2] == "YELLOW" and data.cube[2][0][0] != "YELLOW" and data.cube[2][2][0] == "YELLOW"):
        # SPIN TO CORRECT FAT T STATE
        print("Back prime")
        backPrime(data)
    elif(data.cube[2][0][2] != "YELLOW" and data.cube[2][2][2] != "YELLOW" and data.cube[2][0][0] == "YELLOW" and data.cube[2][2][0] == "YELLOW"):
        # SPIN TO CORRECT FAT T STATE
        print("Back x2")
        back(data)
        back(data)
    elif(data.cube[2][0][2] == "YELLOW" and data.cube[2][2][2] != "YELLOW" and data.cube[2][0][0] == "YELLOW" and data.cube[2][2][0] != "YELLOW"):
        # SPIN TO CORRECT FAT T STATE
        print("Back")
        back(data)
    # --------------BLOB PATTERN------------------
    elif(data.cube[2][0][2] != "YELLOW" and data.cube[2][2][0] != "YELLOW" and data.cube[2][0][0] == "YELLOW" and data.cube[2][2][2] == "YELLOW"):
        # DO THE BLOB ALG
        print("Top")
        print("Back")
        print("Top prime")
        print("Back")
        print("Top")
        print("Back x2")
        print("Top prime")
        top(data)
        back(data)
        topPrime(data)
        back(data)
        top(data)
        back(data)
        back(data)
        topPrime(data)
    elif(data.cube[2][0][2] == "YELLOW" and data.cube[2][2][0] == "YELLOW" and data.cube[2][0][0] != "YELLOW" and data.cube[2][2][2] != "YELLOW"):
       # SPIN TO CORRECT BLOB STATE
       print("Back")
       back(data)
    
def finalLayer(data):
    redMatch = False
    greenMatch = False
    orangeMatch = False
    blueMatch = False
    
    if(data.cube[1][0][2] == data.cube[1][2][2] == "RED" or data.cube[5][2][0] == data.cube[5][0][0] == "RED" or data.cube[3][0][0] == data.cube[3][2][0] == "RED" or data.cube[4][2][0] == data.cube[4][0][0] == "RED"):
        redMatch = True
    
    if(data.cube[1][0][2] == data.cube[1][2][2] == "GREEN" or data.cube[5][2][0] == data.cube[5][0][0] == "GREEN" or data.cube[3][0][0] == data.cube[3][2][0] == "GREEN" or data.cube[4][2][0] == data.cube[4][0][0] == "GREEN"):
        greenMatch = True
    
    if(data.cube[1][0][2] == data.cube[1][2][2] == "ORANGE" or data.cube[5][2][0] == data.cube[5][0][0] == "ORANGE" or data.cube[3][0][0] == data.cube[3][2][0] == "ORANGE" or data.cube[4][2][0] == data.cube[4][0][0] == "ORANGE"):
        orangeMatch = True
    
    if(data.cube[1][0][2] == data.cube[1][2][2] == "BLUE" or data.cube[5][2][0] == data.cube[5][0][0] == "BLUE" or data.cube[3][0][0] == data.cube[3][2][0] == "BLUE" or data.cube[4][2][0] == data.cube[4][0][0] == "BLUE"):
        blueMatch = True
    
    
    # No matching edges
    if(not(redMatch or greenMatch or orangeMatch or blueMatch)):
        print("Down prime")
        print("Right")
        print("Down prime")
        print("Left x2")
        print("Down")
        print("Right prime")
        print("Down prime")
        print("Left x2")
        print("Down x2")
        downPrime(data)
        right(data)
        downPrime(data)
        left(data)
        left(data)
        down(data)
        rightPrime(data)
        downPrime(data)
        left(data)
        left(data)
        down(data)
        down(data)
    # Only have matching red edges
    elif(redMatch and not greenMatch and not orangeMatch and not blueMatch):
        while(data.cube[1][0][2] != data.cube[1][1][1]):
            print("Back")
            back(data)
        print("Top prime")
        print("Left")
        print("Top prime")
        print("Right x2")
        print("Top")
        print("Left prime")
        print("Top prime")
        print("Right x2")
        print("Top x2")
        
        topPrime(data)
        left(data)
        topPrime(data)
        right(data)
        right(data)
        top(data)
        leftPrime(data)
        topPrime(data)
        right(data)
        right(data)
        top(data)
        top(data)
    # Only have matching green edges
    elif(not redMatch and greenMatch and not orangeMatch and not blueMatch):
        while(data.cube[5][2][0] != data.cube[5][1][1]):
            print("Back")
            back(data)
        print("Right prime")
        print("Top")
        print("Right prime")
        print("Down x2")
        print("Right")
        print("Top prime")
        print("Right prime")
        print("Down x2")
        print("Right x2")
        
        rightPrime(data)
        top(data)
        rightPrime(data)
        down(data)
        down(data)
        right(data)
        topPrime(data)
        rightPrime(data)
        down(data)
        down(data)
        right(data)
        right(data)
        
    # Only have matching orange edges
    elif(not redMatch and not greenMatch and orangeMatch and not blueMatch):
        while(data.cube[3][0][0] != data.cube[3][1][1]):
            print("Back")
            back(data)
            
        print("Down prime")
        print("Right")
        print("Down prime")
        print("Left x2")
        print("Down")
        print("Right prime")
        print("Down prime")
        print("Left x2")
        print("Down x2")
        
        downPrime(data)
        right(data)
        downPrime(data)
        left(data)
        left(data)
        down(data)
        rightPrime(data)
        downPrime(data)
        left(data)
        left(data)
        down(data)
        down(data)
    # Only have matching blue edges    
    elif(not redMatch and not greenMatch and not orangeMatch and blueMatch):
        while(data.cube[4][2][0] != data.cube[4][1][1]):
            print("Back")
            back(data)
        
        print("Left prime")
        print("Down")
        print("Left prime")
        print("Top x2")
        print("Left")
        print("Down prime")
        print("Left prime")
        print("Top x2")
        print("Left x2")
        
        leftPrime(data)
        down(data)
        leftPrime(data)
        top(data)
        top(data)
        left(data)
        downPrime(data)
        leftPrime(data)
        top(data)
        top(data)
        left(data)
        left(data)
    else:
        redBar = False
        greenBar = False
        blueBar = False
        orangeBar = False
        
        if(data.cube[1][0][2] == data.cube[1][1][2] == data.cube[1][2][2] == "RED" or data.cube[5][2][0] == data.cube[5][1][0] == data.cube[5][0][0] == "RED" or data.cube[3][0][0] == data.cube[3][1][0] == data.cube[3][2][0] == "RED" or data.cube[4][2][0] == data.cube[4][1][0] == data.cube[4][0][0] == "RED"):
            redBar = True
        
        if(data.cube[1][0][2] == data.cube[1][1][2] == data.cube[1][2][2] == "GREEN" or data.cube[5][2][0] == data.cube[5][1][0] == data.cube[5][0][0] == "GREEN" or data.cube[3][0][0] == data.cube[3][1][0] == data.cube[3][2][0] == "GREEN" or data.cube[4][2][0] == data.cube[4][1][0] == data.cube[4][0][0] == "GREEN"):
            greenBar = True
            
        if(data.cube[1][0][2] == data.cube[1][1][2] == data.cube[1][2][2] == "BLUE" or data.cube[5][2][0] == data.cube[5][1][0] == data.cube[5][0][0] == "BLUE" or data.cube[3][0][0] == data.cube[3][1][0] == data.cube[3][2][0] == "BLUE" or data.cube[4][2][0] == data.cube[4][1][0] == data.cube[4][0][0] == "BLUE"):
            blueBar = True
        
        if(data.cube[1][0][2] == data.cube[1][1][2] == data.cube[1][2][2] == "ORANGE" or data.cube[5][2][0] == data.cube[5][1][0] == data.cube[5][0][0] == "ORANGE" or data.cube[3][0][0] == data.cube[3][1][0] == data.cube[3][2][0] == "ORANGE" or data.cube[4][2][0] == data.cube[4][1][0] == data.cube[4][0][0] == "ORANGE"):
            orangeBar = True
            
        if(not redBar and not greenBar and not blueBar and not orangeBar):
            print("Down x2")
            print("Back")
            print("Down")
            print("Back")
            print("Down prime")
            print("Back prime")
            print("Down prime")
            print("Back prime")
            print("Down prime")
            print("Back")
            print("Down prime")
            
            down(data)
            down(data)
            back(data)
            down(data)
            back(data)
            downPrime(data)
            backPrime(data)
            downPrime(data)
            backPrime(data)
            downPrime(data)
            back(data)
            downPrime(data)
            
        # Just red bar
        elif(redBar and not greenBar and not blueBar and not orangeBar):
            while(data.cube[1][0][2] != data.cube[1][1][1]):
                print("Back")
                back(data)
            if(data.cube[3][1][0] == data.cube[5][1][0]):
                print("Top x2")
                print("Back")
                print("Top")
                print("Back")
                print("Top prime")
                print("Back prime")
                print("Top prime")
                print("Back prime")
                print("Top prime")
                print("Back")
                print("Top prime")
                top(data)
                top(data)
                back(data)
                top(data)
                back(data)
                topPrime(data)
                backPrime(data)
                topPrime(data)
                backPrime(data)
                topPrime(data)
                back(data)
                topPrime(data)
            else:
                # TODO: FIX
                '''
                R = top
                U = back
                '''
                print("Top")
                print("Back prime")
                print("Top")
                print("Back")
                print("Top")
                print("Back")
                print("Top")
                print("Back prime")
                print("Top prime")
                print("Back prime")
                print("Top x2")
                top(data)
                backPrime(data)
                top(data)
                back(data)
                top(data)
                back(data)
                top(data)
                backPrime(data)
                topPrime(data)
                backPrime(data)
                top(data)
                top(data)
                
            
        # Just green bar - I THINK DONE
        elif(not redBar and greenBar and not blueBar and not orangeBar):
            while(data.cube[5][2][2] != data.cube[5][1][1]):
                print("Back")
                back(data)
            if(data.cube[4][1][0] == data.cube[3][1][0]):
                '''
                R = Right
                U = Back
                '''
                print("Right x2")
                print("Back")
                print("Right")
                print("Back")
                print("Right prime")
                print("Back prime")
                print("Right prime")
                print("Back prime")
                print("Right prime")
                print("Back")
                print("Right prime")
                right(data)
                right(data)
                back(data)
                right(data)
                rightPrime(data)
                backPrime(data)
                rightPrime(data)
                backPrime(data)
                rightPrime(data)
                back(data)
                rightPrime(data)
            # MAYBE WRONG
            else:
                print("Right")
                print("Back prime")
                print("Right")
                print("Back")
                print("Right")
                print("Back")
                print("Right")
                print("Back prime")
                print("Right prime")
                print("Back prime")
                print("Right x2")
                right(data)
                backPrime(data)
                right(data)
                back(data)
                right(data)
                back(data)
                right(data)
                backPrime(data)
                rightPrime(data)
                backPrime(data)
                right(data)
                right(data)
        # Just blue bar
        elif(not redBar and not greenBar and blueBar and not orangeBar):
            # TODO: FIX THIS
            while(data.cube[4][2][0] != data.cube[4][1][1]):
                print("Back")
                back(data)
            '''
            R = Left
            U = Back
            '''
            if(data.cube[5][1][0] == data.cube[1][1][1]):
                print("Left x2")
                print("Back")
                print("Left")
                print("Back")
                print("Left prime")
                print("Back prime")
                print("Left prime")
                print("Back prime")
                print("Left prime")
                print("Back")
                print("Left prime")
                left(data)
                left(data)
                back(data)
                left(data)
                back(data)
                leftPrime(data)
                backPrime(data)
                leftPrime(data)
                backPrime(data)
                leftPrime(data)
                back(data)
                leftPrime(data)
                if(data.cube[0][1][1] == data.cube[2][1][0]):
                    print("Right x2")
                    print("Left x2")
                    right(data)
                    right(data)
                    left(data)
                    left(data)
            else:
                print("Left")
                print("Back prime")
                print("Left")
                print("Back")
                print("Left")
                print("Back")
                print("Left")
                print("Back prime")
                print("Left prime")
                print("Back prime")
                print("Right x2")
                left(data)
                backPrime(data)
                left(data)
                back(data)
                left(data)
                back(data)
                left(data)
                backPrime(data)
                leftPrime(data)
                backPrime(data)
                right(data)
                right(data)
                if(data.cube[0][1][1] == data.cube[2][1][0]):
                    print("Right x2")
                    print("Left x2")
                    right(data)
                    right(data)
                    left(data)
                    left(data)
        # Just orange bar
        elif(not redBar and not greenBar and not blueBar and orangeBar):
            # print(data.cube[3][0][0])
            # print(data.cube[3][1][1])
            while(data.cube[3][0][0] != data.cube[3][1][1]):
                print("Back")
                back(data)
            if(data.cube[1][1][2] == data.cube[4][1][1]):
                print("Down x2")
                print("Back")
                print("Down")
                print("Back")
                print("Down prime")
                print("Back prime")
                print("Down prime")
                print("Back prime")
                print("Down prime")
                print("Back")
                print("Down prime")
                
                down(data)
                down(data)
                back(data)
                down(data)
                back(data)
                downPrime(data)
                backPrime(data)
                downPrime(data)
                backPrime(data)
                downPrime(data)
                back(data)
                downPrime(data)
            else:
                '''
                R = Down
                U = Back
                '''
                print("Down")
                print("Back prime")
                print("Down")
                print("Back")
                print("Down")
                print("Back")
                print("Down")
                print("Back prime")
                print("Down prime")
                print("Back prime")
                print("Down x2")
                down(data)
                backPrime(data)
                down(data)
                back(data)
                down(data)
                back(data)
                down(data)
                backPrime(data)
                downPrime(data)
                backPrime(data)
                down(data)
                down(data)
            # TODO: Add counterclockwise rotation

        if(greenBar and redBar and blueBar and orangeBar):
            while(data.cube[1][0][2] != data.cube[1][1][1]):
                print("Back")
                back(data)

        
        
        