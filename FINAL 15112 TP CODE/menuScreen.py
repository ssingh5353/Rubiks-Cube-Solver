# Updated Animation Starter Code

import numpy as np
import cv2
import copy

from tkinter import *
import random
import webbrowser
from DrawCube import *


##
def colorCalibration(data):
    calibrationStep = True
    cap = cv2.VideoCapture(0)
    cameraRunning = True
    cubeSide = [ [" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "] ]
    faceCount = 1
    calibrationNum = 1
    
    while(cameraRunning):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # get dimensions of image
        dimensions = frame.shape
        # height, width, number of channels in image
        height = dimensions[0]
        width = dimensions[1]
        # Cube size 
        sideLength = height // 5
        # Flip the grame to the correct orientation
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        if(calibrationStep):
            
            
            
            x0 = (9*width//20)
            y0 = (2*height//5)
            x1 = x0 + sideLength
            y1 = y0 + sideLength
            
            
            cv2.rectangle(frame,(x0,y0),(x1,y1),(0,0,0),3)
            
            checkX1 = x0 + (2*sideLength//5)
            checkX2 = x0 + (3*sideLength//5)
            checkY1 = y0 + (2*sideLength//5)
            checkY2 = y0 + (3*sideLength//5)
            
            #cv2.rectangle(frame,(checkX1,checkY1),(checkX2,checkY2),(255,255,255),3)
            
            firstCheck = frame[checkY1,checkX1]
            secondCheck = frame[checkY1,checkX2]
            thirdCheck = frame[checkY2,checkX1]
            fourthCheck = frame[checkY2,checkX2]
            
            bTot = (int(firstCheck[0]) + int(secondCheck[0]) + int(thirdCheck[0]) + int(fourthCheck[0]))//4
            gTot = (int(firstCheck[1]) + int(secondCheck[1]) + int(thirdCheck[1]) + int(fourthCheck[1]))//4
            rTot = (int(firstCheck[2]) + int(secondCheck[2]) + int(thirdCheck[2]) + int(fourthCheck[2]))//4
            
            cv2.rectangle(frame,(50,height//10),(width-50,height//5+5),(255,255,255),-1)
            cv2.rectangle(frame,(50,height//10),(width-50,height//5+5),(0,0,0),1)
            
            if(calibrationNum == 1):
                cv2.rectangle(frame,(x0,y0),(x1,y1),(255,255,255),3)
                cv2.putText(frame,"Please calibrate the white color",(height//3-100,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    data.whiteColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 2):
                cv2.rectangle(frame,(x0,y0),(x1,y1),(255,0,0),3)
                cv2.putText(frame,"Please calibrate the blue color",(height//3-75,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    data.blueColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 3):
                cv2.rectangle(frame,(x0,y0),(x1,y1),(0,255,255),3)
                cv2.putText(frame,"Please calibrate the yellow color",(height//3-115,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    data.yellowColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 4):
                cv2.rectangle(frame,(x0,y0),(x1,y1),(0,255,0),3)
                cv2.putText(frame,"Please calibrate the green color",(height//3-110,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    data.greenColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 5):
                cv2.rectangle(frame,(x0,y0),(x1,y1),(0,165,255),3)
                cv2.putText(frame,"Please calibrate the orange color",(height//3-115,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    data.orangeColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 6):
                cv2.rectangle(frame,(x0,y0),(x1,y1),(0,0,255),3)
                cv2.putText(frame,"Please calibrate the red color",(height//3-60,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    data.redColor = [bTot,gTot,rTot]
                    cameraRunning = False
                    calibrationStep = False
                    
        cv2.rectangle(frame,(50,height//10+500),(width-50,height//5+505),(255,255,255),-1)
        cv2.rectangle(frame,(50,height//10+500),(width-50,height//5+505),(0,0,0),1)
        cv2.putText(frame,"Press 'r' when color is in position!",(height//3-145,width//10+500), font, 2,(0,0,0),2,cv2.LINE_AA)
            
 
            
        
        
        # Display the resulting frame
        cv2.imshow("Rubik's Cube Scanner!",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #print(cv2.waitKey(1))
            cameraRunning = False
            
        
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def colorReader(data):
    calibrationStep = True
    cap = cv2.VideoCapture(0)
    cameraRunning = True
    cubeSide = [ [" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "] ]
    faceCount = 1
    calibrationNum = 1
    while(cameraRunning):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # get dimensions of image
        dimensions = frame.shape
        # height, width, number of channels in image
        height = dimensions[0]
        width = dimensions[1]
        # Cube size 
        sideLength = height // 5
        # Flip the grame to the correct orientation
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.rectangle(frame,(50,height//10-50),(width-50,height//5-5),(0,0,0),2)
        cv2.rectangle(frame,(50,height//10-50),(width-50,height//5-5),(255,255,255),-1)
        
        
        if(faceCount == 1):
            cv2.putText(frame,"Please show the white side",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        elif(faceCount == 2):
            cv2.putText(frame,"Please turn clockwise once",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        elif(faceCount == 3):
            cv2.putText(frame,"Please turn clockwise once",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        elif(faceCount == 4):
            cv2.putText(frame,"Please turn clockwise once",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        elif(faceCount == 5):
            cv2.putText(frame,"Please turn towards screen once",(height//5,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        elif(faceCount == 6):
            cv2.putText(frame,"Please turn away from screen twice",(height//10,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        else:
            cap.release()
            cv2.destroyAllWindows()
            
        
        
        cv2.putText(frame,"Face " + str(faceCount),(35*width//80-5,height//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        
        
        cv2.rectangle(frame,(30,9*height//10-55),(width-30,9*height//10+20),(255,255,255),-1)
        cv2.rectangle(frame,(30,9*height//10-55),(width-30,9*height//10+20),(0,0,0),1)
        cv2.putText(frame,"Press space when face is in position!",(width//35,9*height//10), font, 2,(0,0,0),2,cv2.LINE_AA)
        
        
        
        
        
        # Makes grid
        for rows in range(3):
            for cols in range (3):
                x0 = (3*width//5) + (rows * sideLength)
                y0 = (height//5) + (cols * sideLength)
                x1 = x0 + sideLength
                y1 = y0 + sideLength
                
                checkX1 = x0 + (2*sideLength//5)
                checkX2 = x0 + (3*sideLength//5)
                checkY1 = y0 + (2*sideLength//5)
                checkY2 = y0 + (3*sideLength//5)
                
                #cv2.rectangle(frame,(checkX1,checkY1),(checkX2,checkY2),(255,255,255),3)
                
                firstCheck = frame[checkY1,checkX1]
                secondCheck = frame[checkY1,checkX2]
                thirdCheck = frame[checkY2,checkX1]
                fourthCheck = frame[checkY2,checkX2]
                
                # Averages -> bTot with middlePoint[0], gTot with middlePoint[1], rTot with middlePoint[2]
                bTot = (int(firstCheck[0]) + int(secondCheck[0]) + int(thirdCheck[0]) + int(fourthCheck[0]))//4
                gTot = (int(firstCheck[1]) + int(secondCheck[1]) + int(thirdCheck[1]) + int(fourthCheck[1]))//4
                rTot = (int(firstCheck[2]) + int(secondCheck[2]) + int(thirdCheck[2]) + int(fourthCheck[2]))//4
                
                
                cv2.rectangle(frame,(x0,y0),(x1,y1),(255,255,255),3)
                
                
                middlePoint = frame[y0+sideLength//2, x0+sideLength//2]
                
                animationX0 = (width//10) + (rows * sideLength)
                animationY0 = y0
                animationX1 = animationX0 + sideLength
                animationY0 = y1
                
                whiteBDiff = abs(data.whiteColor[0] - bTot)
                whiteGDiff = abs(data.whiteColor[1] - gTot)
                whiteRDiff = abs(data.whiteColor[2] - rTot)
                
                yellowBDiff = abs(data.yellowColor[0] - bTot)
                yellowGDiff = abs(data.yellowColor[1] - gTot)
                yellowRDiff = abs(data.yellowColor[2] - rTot)
                
                blueBDiff = abs(data.blueColor[0] - bTot)
                blueGDiff = abs(data.blueColor[1] - gTot)
                blueRDiff = abs(data.blueColor[2] - rTot)
                
                redBDiff = abs(data.redColor[0] - bTot)
                redGDiff = abs(data.redColor[1] - gTot)
                redRDiff = abs(data.redColor[2] - rTot)
                
                orangeBDiff = abs(data.orangeColor[0] - bTot)
                orangeGDiff = abs(data.orangeColor[1] - gTot)
                orangeRDiff = abs(data.orangeColor[2] - rTot)
                
                greenBDiff = abs(data.greenColor[0] - bTot)
                greenGDiff = abs(data.greenColor[1] - gTot)
                greenRDiff = abs(data.greenColor[2] - rTot)
                
                
                
                
                # Text for which colors are in the shown cube
                if(whiteBDiff < 90 and whiteGDiff < 90 and whiteRDiff < 90):
                    #cv2.putText(frame,str([whiteBDiff,whiteGDiff,whiteRDiff]),(x0+sideLength//10,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cv2.putText(frame,"WHITE",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][2-rows] = "WHITE"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(255,255,255),-1)
                elif(yellowBDiff < 50 and yellowGDiff < 50 and yellowRDiff < 50):
                    cv2.putText(frame,"YELLOW",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][2-rows] = "YELLOW"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,255,255),-1)
                elif(redBDiff < 60 and redGDiff < 60 and redRDiff < 60):
                    cv2.putText(frame,"RED",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][2-rows] = "RED"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,0,255),-1)
                elif(orangeBDiff < 60 and orangeGDiff < 60 and orangeRDiff < 60):
                    cv2.putText(frame,"ORANGE",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][2-rows] = "ORANGE"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,165,255),-1)
                elif(greenBDiff < 70 and greenGDiff < 70 and greenRDiff < 70):
                    cv2.putText(frame,"GREEN",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][2-rows] = "GREEN"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,255,0),-1)
                elif(blueBDiff < 90 and blueGDiff < 90 and blueRDiff < 90):
                    cv2.putText(frame,"BLUE",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][2-rows] = "BLUE"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(255,0,0),-1)
                else:
                    #cv2.putText(frame,str([blueDiff,greenDiff,redDiff]),(x0+sideLength//10,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cv2.putText(frame,"NO COLOR",(x0+sideLength//10,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                    cubeSide[cols][rows] = " "
                    
                if(faceCount == 1 and rows == 1 and cols == 1):
                    cubeSide[cols][2-rows] = "WHITE"
                    cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(255,255,255),-1)
                    cv2.rectangle(frame,(x0,y0),(x1,y1),(255,255,255),-1)
                
                cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,0,0),2)
                
            
        
        
        if cv2.waitKey(1) == ord(' '):
    
            hasAllColors = True
            for row in cubeSide:
                for col in row:
                    if col == " ":
                        hasAllColors = False
                        
            if(hasAllColors):
                #print("Not here")
                if faceCount == 1:
                    side1 = copy.deepcopy(cubeSide)
                if faceCount == 2:
                    side2 = copy.deepcopy(cubeSide)
                if faceCount == 3:
                    side3 = copy.deepcopy(cubeSide)
                if faceCount == 4:
                    side4 = copy.deepcopy(cubeSide)
                if faceCount == 5:
                    side5 = copy.deepcopy(cubeSide)
                if faceCount == 6:
                    side6 = copy.deepcopy(cubeSide)
                faceCount += 1
            # else:
            #     print("Found it")
            
            if(faceCount == 7):
                cube = [side1,side2,side3,side4,side5,side6]
                cap.release()
                cv2.destroyAllWindows()
                return cube
            
        
        
        # Display the resulting frame
        cv2.imshow("Rubik's Cube Scanner!",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #print(cv2.waitKey(1))
            cameraRunning = False
            
        
    
    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()

##






####################################
# customize these functions
####################################
#def start():
def init(data):
    data.colorConfig = False
    data.solver = False
    data.solveScreen = False
    data.menu = True
    data.instructions = False
    data.cube = []
    
    data.buttonWidth = 5*data.width//7
    data.buttonHeight = data.height//5
    
    data.buttonX0 = data.width//7
    data.buttonX1 = data.buttonX0 + data.buttonWidth
    
    data.box1Y0 = data.height//5
    data.box1Y1 = data.box1Y0 + data.buttonHeight
    
    data.box2Y0 = data.box1Y1 + data.height//15
    data.box2Y1 = data.box2Y0 + data.buttonHeight
    
    data.box3Y0 = data.box2Y1 + data.height//15
    data.box3Y1 = data.box3Y0 + data.buttonHeight
    
    data.whiteColor = [255,255,255]
    data.blueColor = [255,0,0]
    data.greenColor = [0,255,0]
    data.yellowColor = [255,255,0]
    data.redColor = [0,0,255]
    data.orangeColor = [0,165,255]
    # load data.xyz as appropriate
    pass

def mousePressed(event, data):
    
    
    if(data.menu):
        if(event.x >= data.buttonX0 and event.x <= data.buttonX0 + data.buttonWidth):
            if(event.y >= data.box1Y0 and event.y <= data.box1Y1):
                #print("Top")
                data.menu = False
                data.colorConfig = True
            # if(event.y >= data.box2Y0 and event.y <= data.box2Y1):
            #     data.solveScreen = True
            #     data.menu = False
            #     #print("")
                
            if(event.y >= data.box3Y0 and event.y <= data.box3Y1):
                #print("Bottom")
                return webbrowser.open('http://ozcubegirl.com/rubikscubesolution.html')
            # TODO: JHSBDF
            if(event.y >= data.box2Y0 and event.y <= data.box2Y1):
                cube = colorReader(data)
                data.menu = False
                data.instructions = True
                data.cube = cube
                #solve(cube)
    
    if(data.colorConfig):
        xLeft = data.width//20
        xRight = data.width//5
        yTop = data.height//20
        yBottom = 5*data.height//40
        if(event.x >= xLeft and event.x <= xRight and event.y >= yTop and event.y <= yBottom):
            data.menu = True
            data.colorConfig = False
        index = 0    
        boxWidth = data.width//5
        for row in range(2):
            for col in range(3):
                colors = ["Red","Blue","Green","Yellow","Orange","White"]
                x0 = data.width//5 + boxWidth * col
                x1 = x0 + boxWidth
                y0 = data.height//3 + boxWidth * row
                y1 = y0 + boxWidth
                # if(event.x >= x0 and event.x <= x1 and event.y >= y0 and event.y <= y1):
                #     print(colors[index])
                index += 1
                
        if(event.x >= data.width//3 and event.x <= 2*data.width//3 and event.y >= 8*data.height//10 and event.y <= 9*data.height//10):
            colorCalibration(data)
        
    

def keyPressed(event, data):
    if(data.instructions and event.keysym == "s"):
        data.menu = True
        data.instructions = False
        solve(data.cube)
    
    if(event.keysym == "b"):
        (data.whiteColor)
    pass

def timerFired(data):
    
    pass

def redrawAll(canvas, data):
    if(data.instructions):
        canvas.create_text(data.width//2,data.height//10,text = "Instructions",font = "Arial 70 bold")
        canvas.create_text(data.width//2,data.height//5,text = "Here are a few things to keep in mind:",font = "Arial 25")
        canvas.create_text(data.width//2,data.height//5+65,text = "- Please point the WHITE face at you",font = "Arial 25")
        canvas.create_text(data.width//2,data.height//5+130,text = "- Please point the " + str(data.cube[1][1][1]) + " face to your right",font = "Arial 25")
        canvas.create_text(data.width//2,data.height//5+195,text = "- Always spin the cube respective to the face instructed",font = "Arial 25")
        canvas.create_text(data.width//2,data.height//5+260,text = "- Always spin clock wise other indicated otherwise by the word 'prime'",font = "Arial 25")
        canvas.create_text(data.width//2,data.height//5+325,text = "Press 's' to see the solution to your cube!",font = "Arial 25")
        
        
        
        
    if(data.solveScreen):
        xLeft = data.width//20
        xRight = data.width//5
        yTop = data.height//20
        yBottom = 5*data.height//40
        xMid = (xLeft + xRight)//2
        yMid = (yTop + yBottom)//2
        canvas.create_text(xMid,yMid,text = "Menu",font = "Arial 25 bold",fill="White")
        canvas.create_rectangle(data.width//3,8*data.height//10,2*data.width//3,9*data.height//10,fill="Black")
    if(data.colorConfig):
        canvas.create_text(data.width//2, data.height//5,text="Please calibrate the following colors!",font = "Arial 40 bold",fill="Black")
        boxWidth = data.width//5
        index = 0
        for row in range(2):
            for col in range(3):
                colors = ["Red","Blue","Green","Yellow2","Orange","White"]
                x0 = data.width//5 + boxWidth * col
                x1 = x0 + boxWidth
                y0 = data.height//3 + boxWidth * row
                y1 = y0 + boxWidth
                canvas.create_rectangle(x0,y0,x1,y1,fill=colors[index])
                index += 1
        xLeft = data.width//20
        xRight = data.width//5
        yTop = data.height//20
        yBottom = 5*data.height//40
        canvas.create_rectangle(xLeft,yTop,xRight,yBottom,fill="Black")
        xMid = (xLeft + xRight)//2
        yMid = (yTop + yBottom)//2
        canvas.create_text(xMid,yMid,text = "Menu",font = "Arial 25 bold",fill="White")
        canvas.create_rectangle(data.width//3,8*data.height//10,2*data.width//3,9*data.height//10,fill="Black")
        configX = (data.width//2)
        configY = data.height*17//20
        canvas.create_text(configX,configY,text = "Calibrate",font = "Arial 25 bold",fill="White")
       # canvas.create_rectangle(data.width//3,8*data.height//10,2*data.width//3,9*data.height//10,fill="Black")
        
        
    
    numCubes = 100
    
    if(data.menu):
        for row in range(numCubes):
            for col in range(numCubes):
                colors = ["Red","Blue","Green","Yellow2","Orange","White"]
                #colorNum = (row + col)%5
                colorNum = random.randint(0,5)
                x0 = data.width//numCubes * row
                x1 = x0 + data.width//numCubes
                y0 = data.height//numCubes * col
                y1 = y0 + data.height//numCubes
                canvas.create_rectangle(x0,y0,x1,y1,fill=colors[colorNum],width=1)
            
            
    
        canvas.create_rectangle(data.width//25,data.height//20,24*data.width//25,3*data.height//20,fill="Black")
        canvas.create_text(data.width//2, data.height//10,text="Rubik's Cube Solver",font = "Arial 75 bold",fill="White")
        
        canvas.create_rectangle(data.buttonX0,data.box1Y0,data.buttonX1,data.box1Y1,fill="White", width = 5)
        canvas.create_text(data.buttonX0 + data.buttonWidth//2, data.box1Y0 + data.buttonHeight//2, text="Color Calibration",font="Arial 35 bold")
        
        canvas.create_rectangle(data.buttonX0,data.box2Y0,data.buttonX1,data.box2Y1,fill="White", width = 5)
        canvas.create_text(data.buttonX0 + data.buttonWidth//2, data.box2Y0 + data.buttonHeight//2, text="Solve Your Cube!",font="Arial 35 bold")
        
        canvas.create_rectangle(data.buttonX0,data.box3Y0,data.buttonX1,data.box3Y1,fill="White", width = 5)
        canvas.create_text(data.buttonX0 + data.buttonWidth//2, data.box3Y0 + data.buttonHeight//2, text="How To Solve a Rubik's Cube!",font="Arial 35 bold")
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 750 # milliseconds
    root = Tk()
    root.title("Rubik's Cube Solver!") 
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)



#start()




