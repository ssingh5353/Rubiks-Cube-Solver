"""
CITATION FOR MVC FRAMEWORK:

Website: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
"""
import cv2
from videoCalibration import *
from moves import *
# Updated Animation Starter Code
from tkinter import *
from solutionAlgorithim import *

def solve(cube):
    def drawCubes(canvas,x0,y0,sideLen,colors,faceNum):
        for row in range(3):
            for col in range(3):
                if(faceNum == 4 or faceNum == 5):
                    color = colors[faceNum][2-col][2-row]
    
                else:
                    color = colors[faceNum][col][row]
                smallX0 = x0 + row*(sideLen/3)
                smallY0 = y0 + col*(sideLen/3)
                smallX1 = smallX0 + sideLen/3
                smallY1 = smallY0 + sideLen/3
                if(faceNum == 0 and row == 1 and col == 1):
                    color = "WHITE"
                canvas.create_rectangle(smallX0,smallY0,smallX1,smallY1,fill=color)
                #canvas.create_text(smallX0 + sideLen/6,smallY0 + sideLen/6,text=str([faceNum,col,row]))
        
    
    def drawSides(data,canvas,sideLen):
        # Drawing the outside boxes for the first four faces
        for side in range(4):
            colors = data.cube[side]
            x0 = (data.width//10 + side*sideLen)
            y0 = (2*data.height//5)
            x1 = x0 + sideLen
            y1 = y0 + sideLen
            canvas.create_rectangle(x0,y0,x1,y1,width=3)
            # Drawing the individual cubes for the first four faces
            drawCubes(canvas,x0,y0,sideLen,data.cube,side)
        # Drawing the outside box for the top face
        x0 = (data.width//10 + sideLen)
        y0 = (2*data.height//5) - sideLen
        x1 = x0 + sideLen
        y1 = y0 + sideLen   
        colors = data.cube[4]
        canvas.create_rectangle(x0,y0,x1,y1,width=5)
        # Drawing the individual cubes for the top face
        drawCubes(canvas,x0,y0,sideLen,data.cube,4)
        # Drawing the outside box for the bottom face
        y0 = (2*data.height//5) + sideLen
        y1 = y0 + sideLen
        colors = data.cube[5]
        canvas.create_rectangle(x0,y0,x1,y1,width=3)
        # Individual cubes for the bottom face
        drawCubes(canvas,x0,y0,sideLen,data.cube,5)
    
    
    ####################################
    # customize these functions
    ####################################
    
    def init(data):
        data.step = 0
        data.sideLen = data.width//5
        data.cube=cube
        data.whiteDaisy = False
        data.whiteT = False
        data.whiteFace = False
        data.middleLayer = False
        data.yellowT = False
        data.yellowFace = False
        data.finalLayer = False
        # load data.xyz as appropriate
        pass
    
    def mousePressed(event, data):
        # use event.x and event.y
        pass
    
    def keyPressed(event, data):
        data.step += 1
        checkWhiteDaisy(data)
        checkWhiteT(data)
        checkWhiteFace(data)
        checkMiddleLayer(data)
        checkYellowT(data)
        checkYellowFace(data)
        checkFinalLayer(data)
        
        # if event.keysym == "r":
        #     print("Here")
        #     right(data)
        #     
        # if event.keysym == "e":
        #     rightPrime(data)
    
   #    #   if event.keysym == "t":
        #     top(data)
        #     
        # if event.keysym == "y":
        #     topPrime(data)
        #     
        # if event.keysym == "l":
        #     left(data)
        #     
        # if event.keysym == "k":
        #     leftPrime(data)
        #     
        # if event.keysym == "d":
        #     down(data)
        # 
        # if event.keysym == "c":
        #     downPrime(data)
        #     
        # if event.keysym == "f":
        #     face(data)
        #     
        # if event.keysym == "g":
        #     facePrime(data)
        #     
        # if event.keysym == "b":
        #     back(data)
        #     
        # if event.keysym == "v":
        #     backPrime(data)
        
        if event.keysym == "a":
            print("")
            print("Step: " + str(data.step))
            if(not data.whiteDaisy):
                #print("WHITE DAISY - ")
                whiteDaisy(data)
            elif(not data.whiteT):
                #print("WHITE T")
                whiteT(data)
            elif(not data.whiteFace):
                #print("WHITE FACE - ")
                whiteFace(data)
            elif(not data.middleLayer):
                #print("MIDDLE LAYERS - ")
                middleLayer(data)
            elif(not data.yellowT):
                #print("YELLOW T - ")
                yellowT(data)
            elif(not data.yellowFace):
                #print("YELLOW FACE - ")
                yellowFace(data)
            else:
                #print("FINAL LAYERS - ")
                finalLayer(data)
        
        checkWhiteDaisy(data)
        checkWhiteT(data)
        checkWhiteFace(data)
        checkMiddleLayer(data)
        checkYellowT(data)
        checkYellowFace(data)
        checkFinalLayer(data)
    
        pass
    
    def timerFired(data):
        pass
    
    def redrawAll(canvas, data):
        if(data.whiteDaisy == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving White Daisy...",font="Arial 50 bold")
        elif(data.whiteT == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving White T...",font="Arial 50 bold")
        elif(data.whiteFace == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving White Face...",font="Arial 50 bold")
        elif(data.middleLayer == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving Middle Layers...",font="Arial 50 bold")
        elif(data.yellowT == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving Yellow T...",font="Arial 50 bold")
        elif(data.yellowFace == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving Yellow Face...",font="Arial 50 bold")
        elif(data.finalLayer == False):
            canvas.create_text(data.width//2,data.height//10,text="Solving Final Layers...",font="Arial 50 bold")
        else:    
            canvas.create_text(data.width//2,data.height//10,text="Cube is Solved!",font="Arial 50 bold")
           
        
        
        
        drawSides(data,canvas,data.sideLen)
        
    def checkWhiteDaisy(data):
        if(data.cube[2][0][1] == "WHITE" and data.cube[2][1][2] == "WHITE" and data.cube[2][2][1] == "WHITE" and data.cube[2][1][0] == "WHITE"):
            data.whiteDaisy = True
    
    def checkWhiteT(data):
        if(data.cube[0][0][1] == "WHITE" and data.cube[0][1][2] == "WHITE" and data.cube[0][2][1] == "WHITE" and data.cube[0][1][0] == "WHITE" and data.cube[1][1][0] == data.cube[1][1][1]):
            data.whiteDaisy = True
            data.whiteT = True
    
    def checkWhiteFace(data):
        whiteFace = True
        for row in range(3):
            for col in range(3):
                if(data.cube[0][row][col] != "WHITE"):
                    whiteFace = False
        for check in range(3):
            if(data.cube[1][check][0] != data.cube[1][1][1]):
                whiteFace = False
            if(data.cube[3][check][2] != data.cube[3][1][1]):
                whiteFace = False
            if(data.cube[4][check][2] != data.cube[4][1][1]):
                whiteFace = False
            if(data.cube[5][check][2] != data.cube[5][1][1]):
                whiteFace = False
        
        if(whiteFace):
            data.whiteT = True
            data.whiteDaisy = True
            data.whiteFace = True
    
    def checkMiddleLayer(data):
        middleLayer = True
        if(data.whiteFace == False):
            middleLayer = False
        if(data.cube[1][0][1] != data.cube[1][1][1] or data.cube[1][2][1] != data.cube[1][1][1]):
            middleLayer = False
        if(data.cube[4][2][1] != data.cube[4][1][1] or data.cube[4][0][1] != data.cube[4][1][1]):
            middleLayer = False
        if(data.cube[5][2][1] != data.cube[5][1][1] or data.cube[5][0][1] != data.cube[5][1][1]):
            middleLayer = False
        if(data.cube[3][0][1] != data.cube[3][1][1] or data.cube[3][2][1] != data.cube[3][1][1]):
            middleLayer = False
        
        if(middleLayer):
            data.whiteT = True
            data.whiteDaisy = True
            data.whiteFace = True
            data.middleLayer = True
    
    def checkYellowT(data):
        yellowT = True
        if(data.middleLayer == False):
            yellowT = False
        if(data.cube[2][0][1] != data.cube[2][1][1] or data.cube[2][2][1] != data.cube[2][1][1]):
            yellowT = False
        if(data.cube[2][1][0] != data.cube[2][1][1] or data.cube[2][1][2] != data.cube[2][1][1]):
            yellowT = False
        
        if(yellowT):
            data.whiteT = True
            data.whiteDaisy = True
            data.whiteFace = True
            data.middleLayer = True
            data.yellowT = True
            
    def checkYellowFace(data):
        yellowFace = True
        if(data.middleLayer == False or data.whiteFace == False):
            yellowFace = False
        for row in range(3):
            for col in range(3):
                if(data.cube[2][row][col] != "YELLOW"):
                    yellowFace = False
        if(yellowFace):
            data.whiteT = True
            data.whiteDaisy = True
            data.whiteFace = True
            data.middleLayer = True
            data.yellowT = True
            data.yellowFace = True
            
    def checkFinalLayer(data):
        finalLayer = True
        if(data.middleLayer == False or data. yellowFace == False or data.whiteFace == False):
            finalLayer = False
        if(data.cube[1][1][2] != data.cube[1][1][1] or data.cube[4][1][0] != data.cube[4][1][1] or data.cube[3][1][0] != data.cube[3][1][1] or data.cube[5][1][0] != data.cube[5][1][1]):
            finalLayer = False
        if(finalLayer):
            data.whiteT = True
            data.whiteDaisy = True
            data.whiteFace = True
            data.middleLayer = True
            data.yellowT = True
            data.yellowFace = True
            data.finalLayer = True
        
    
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
        data.timerDelay = 100 # milliseconds
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
    
    run(1000, 800)