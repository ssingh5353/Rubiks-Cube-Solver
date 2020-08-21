import numpy as np
import cv2
import copy
#from menuScreen import *

def colorRecognition():
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
            
            cv2.rectangle(frame,(x0,y0),(x1,y1),(255,255,255),3)
            
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
            
            if(calibrationNum == 1):
                cv2.putText(frame,"Please calibrate the white color",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    whiteColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 2):
                cv2.putText(frame,"Please calibrate the blue color",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    blueColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 3):
                cv2.putText(frame,"Please calibrate the yellow color",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    yellowColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 4):
                cv2.putText(frame,"Please calibrate the green color",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    greenColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 5):
                cv2.putText(frame,"Please calibrate the orange color",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    orangeColor = [bTot,gTot,rTot]
                    calibrationNum += 1
            elif(calibrationNum == 6):
                cv2.putText(frame,"Please calibrate the red color",(height//3,width//10), font, 2,(0,0,0),2,cv2.LINE_AA)
                if cv2.waitKey(1) == ord('r'):
                    redColor = [bTot,gTot,rTot]
                    calibrationStep = False
            
        else:
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
                
            
            
            cv2.putText(frame,"Face " + str(faceCount),(35*width//80,9*height//10), font, 2,(0,0,0),2,cv2.LINE_AA)
            
            
            
            
            
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
                    
                    whiteBDiff = abs(whiteColor[0] - bTot)
                    whiteGDiff = abs(whiteColor[1] - gTot)
                    whiteRDiff = abs(whiteColor[2] - rTot)
                    
                    yellowBDiff = abs(yellowColor[0] - bTot)
                    yellowGDiff = abs(yellowColor[1] - gTot)
                    yellowRDiff = abs(yellowColor[2] - rTot)
                    
                    blueBDiff = abs(blueColor[0] - bTot)
                    blueGDiff = abs(blueColor[1] - gTot)
                    blueRDiff = abs(blueColor[2] - rTot)
                    
                    redBDiff = abs(redColor[0] - bTot)
                    redGDiff = abs(redColor[1] - gTot)
                    redRDiff = abs(redColor[2] - rTot)
                    
                    orangeBDiff = abs(orangeColor[0] - bTot)
                    orangeGDiff = abs(orangeColor[1] - gTot)
                    orangeRDiff = abs(orangeColor[2] - rTot)
                    
                    greenBDiff = abs(greenColor[0] - bTot)
                    greenGDiff = abs(greenColor[1] - gTot)
                    greenRDiff = abs(greenColor[2] - rTot)
                    
                    
                    
                    
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
                    elif(redBDiff < 70 and redGDiff < 70 and redRDiff < 70):
                        cv2.putText(frame,"RED",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                        cubeSide[cols][2-rows] = "RED"
                        cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,0,255),-1)
                    elif(orangeBDiff < 60 and orangeGDiff < 60 and orangeRDiff < 60):
                        cv2.putText(frame,"ORANGE",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                        cubeSide[cols][2-rows] = "ORANGE"
                        cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,165,255),-1)
                    elif(greenBDiff < 90 and greenGDiff < 90 and greenRDiff < 90):
                        cv2.putText(frame,"GREEN",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                        cubeSide[cols][2-rows] = "GREEN"
                        cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(0,255,0),-1)
                    elif(blueBDiff < 120 and blueGDiff < 120 and blueRDiff < 120):
                        cv2.putText(frame,"BLUE",(x0+sideLength//5,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                        cubeSide[cols][2-rows] = "BLUE"
                        cv2.rectangle(frame,(animationX0,y0),(animationX1,y1),(255,0,0),-1)
                    else:
                        #cv2.putText(frame,str([blueDiff,greenDiff,redDiff]),(x0+sideLength//10,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
                        cv2.putText(frame,"NO COLOR" + str(faceCount),(x0+sideLength//10,y0+sideLength//2), font, .5,(0,0,0),2,cv2.LINE_AA)
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
                
        
        if(faceCount == 7):
            cube = [side1,side2,side3,side4,side5,side6]
            return cube
            
        
        
        # Display the resulting frame
        cv2.imshow("Rubik's Cube Scanner!",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #print(cv2.waitKey(1))
            cameraRunning = False
            
        
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()



