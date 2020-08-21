import copy

def right(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[0][0][2] = tempCube[5][2][2]
    data.cube[0][1][2] = tempCube[5][2][1]
    data.cube[0][2][2] = tempCube[5][2][0]
    
    data.cube[4][0][0] = tempCube[0][0][2]
    data.cube[4][0][1] = tempCube[0][1][2]
    data.cube[4][0][2] = tempCube[0][2][2]
    
    data.cube[2][0][0] = tempCube[4][0][2]
    data.cube[2][1][0] = tempCube[4][0][1]
    data.cube[2][2][0] = tempCube[4][0][0]
    
    data.cube[5][2][0] = tempCube[2][0][0]
    data.cube[5][2][1] = tempCube[2][1][0]
    data.cube[5][2][2] = tempCube[2][2][0]
    
    data.cube[1][0][0] = tempCube[1][2][0]
    data.cube[1][0][1] = tempCube[1][1][0]
    data.cube[1][0][2] = tempCube[1][0][0]
    data.cube[1][1][2] = tempCube[1][0][1]
    data.cube[1][2][2] = tempCube[1][0][2]
    data.cube[1][2][1] = tempCube[1][1][2]
    data.cube[1][2][0] = tempCube[1][2][2]
    data.cube[1][1][0] = tempCube[1][2][1]
    
def rightPrime(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[5][2][2] = tempCube[0][0][2]
    data.cube[5][2][1] = tempCube[0][1][2]
    data.cube[5][2][0] = tempCube[0][2][2]
    
    data.cube[0][0][2] = tempCube[4][0][0]
    data.cube[0][1][2] = tempCube[4][0][1]
    data.cube[0][2][2] = tempCube[4][0][2]
    
    data.cube[4][0][0] = tempCube[2][2][0]
    data.cube[4][0][1] = tempCube[2][1][0]
    data.cube[4][0][2] = tempCube[2][0][0]
    
    data.cube[2][0][0] = tempCube[5][2][0]
    data.cube[2][1][0] = tempCube[5][2][1]
    data.cube[2][2][0] = tempCube[5][2][2]
    
    data.cube[1][2][0] = tempCube[1][0][0]
    data.cube[1][1][0] = tempCube[1][0][1]
    data.cube[1][0][0] = tempCube[1][0][2]
    data.cube[1][0][1] = tempCube[1][1][2]
    data.cube[1][0][2] = tempCube[1][2][2]
    data.cube[1][1][2] = tempCube[1][2][1]
    data.cube[1][2][2] = tempCube[1][2][0]
    data.cube[1][2][1] = tempCube[1][1][0]
    
def topPrime(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[1][0][0] = tempCube[0][0][0]
    data.cube[1][0][1] = tempCube[0][0][1]
    data.cube[1][0][2] = tempCube[0][0][2]
    
    data.cube[2][0][0] = tempCube[1][0][0]
    data.cube[2][0][1] = tempCube[1][0][1]
    data.cube[2][0][2] = tempCube[1][0][2]
    
    data.cube[3][0][0] = tempCube[2][0][0]
    data.cube[3][0][1] = tempCube[2][0][1]
    data.cube[3][0][2] = tempCube[2][0][2]
    
    data.cube[0][0][0] = tempCube[3][0][0]
    data.cube[0][0][1] = tempCube[3][0][1]
    data.cube[0][0][2] = tempCube[3][0][2]
    
    data.cube[4][0][0] = tempCube[4][0][2]
    data.cube[4][1][0] = tempCube[4][0][1]
    data.cube[4][2][0] = tempCube[4][0][0]
    data.cube[4][2][1] = tempCube[4][1][0]
    data.cube[4][2][2] = tempCube[4][2][0]
    data.cube[4][1][2] = tempCube[4][2][1]
    data.cube[4][0][2] = tempCube[4][2][2]
    data.cube[4][0][1] = tempCube[4][1][2]
    
def top(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[0][0][0] = tempCube[1][0][0]
    data.cube[0][0][1] = tempCube[1][0][1]
    data.cube[0][0][2] = tempCube[1][0][2]
    
    data.cube[1][0][0] = tempCube[2][0][0]
    data.cube[1][0][1] = tempCube[2][0][1]
    data.cube[1][0][2] = tempCube[2][0][2]
    
    data.cube[2][0][0] = tempCube[3][0][0]
    data.cube[2][0][1] = tempCube[3][0][1]
    data.cube[2][0][2] = tempCube[3][0][2]
    
    data.cube[3][0][0] = tempCube[0][0][0]
    data.cube[3][0][1] = tempCube[0][0][1]
    data.cube[3][0][2] = tempCube[0][0][2]
    
    data.cube[4][0][2] = tempCube[4][0][0]
    data.cube[4][0][1] = tempCube[4][1][0]
    data.cube[4][0][0] = tempCube[4][2][0]
    data.cube[4][1][0] = tempCube[4][2][1]
    data.cube[4][2][0] = tempCube[4][2][2]
    data.cube[4][2][1] = tempCube[4][1][2]
    data.cube[4][2][2] = tempCube[4][0][2]
    data.cube[4][1][2] = tempCube[4][0][1]
    
def left(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[0][0][0] = tempCube[4][2][0]
    data.cube[0][1][0] = tempCube[4][2][1]
    data.cube[0][2][0] = tempCube[4][2][2]
    
    data.cube[5][0][0] = tempCube[0][2][0]
    data.cube[5][0][1] = tempCube[0][1][0]
    data.cube[5][0][2] = tempCube[0][0][0]
    
    data.cube[2][0][2] = tempCube[5][0][0]
    data.cube[2][1][2] = tempCube[5][0][1]
    data.cube[2][2][2] = tempCube[5][0][2]
    
    data.cube[4][2][2] = tempCube[2][0][2]
    data.cube[4][2][1] = tempCube[2][1][2]
    data.cube[4][2][0] = tempCube[2][2][2]
    
    data.cube[3][0][2] = tempCube[3][0][0]
    data.cube[3][0][1] = tempCube[3][1][0]
    data.cube[3][0][0] = tempCube[3][2][0]
    data.cube[3][1][0] = tempCube[3][2][1]
    data.cube[3][2][0] = tempCube[3][2][2]
    data.cube[3][2][1] = tempCube[3][1][2]
    data.cube[3][2][2] = tempCube[3][0][2]
    data.cube[3][1][2] = tempCube[3][0][1]
    
def leftPrime(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[4][2][0] = tempCube[0][0][0]
    data.cube[4][2][1] = tempCube[0][1][0]
    data.cube[4][2][2] = tempCube[0][2][0]
    
    data.cube[0][2][0] = tempCube[5][0][0]
    data.cube[0][1][0] = tempCube[5][0][1]
    data.cube[0][0][0] = tempCube[5][0][2]
    
    data.cube[5][0][0] = tempCube[2][0][2]
    data.cube[5][0][1] = tempCube[2][1][2]
    data.cube[5][0][2] = tempCube[2][2][2]
    
    data.cube[2][0][2] = tempCube[4][2][2]
    data.cube[2][1][2] = tempCube[4][2][1]
    data.cube[2][2][2] = tempCube[4][2][0]
    
    data.cube[3][0][0] = tempCube[3][0][2]
    data.cube[3][1][0] = tempCube[3][0][1]
    data.cube[3][2][0] = tempCube[3][0][0]
    data.cube[3][2][1] = tempCube[3][1][0]
    data.cube[3][2][2] = tempCube[3][2][0]
    data.cube[3][1][2] = tempCube[3][2][1]
    data.cube[3][0][2] = tempCube[3][2][2]
    data.cube[3][0][1] = tempCube[3][1][2]
    
def down(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[1][2][0] = tempCube[0][2][0]
    data.cube[1][2][1] = tempCube[0][2][1]
    data.cube[1][2][2] = tempCube[0][2][2]
    
    data.cube[2][2][0] = tempCube[1][2][0]
    data.cube[2][2][1] = tempCube[1][2][1]
    data.cube[2][2][2] = tempCube[1][2][2]
    
    data.cube[3][2][0] = tempCube[2][2][0]
    data.cube[3][2][1] = tempCube[2][2][1]
    data.cube[3][2][2] = tempCube[2][2][2]
    
    data.cube[0][2][0] = tempCube[3][2][0]
    data.cube[0][2][1] = tempCube[3][2][1]
    data.cube[0][2][2] = tempCube[3][2][2]
    
    data.cube[5][2][0] = tempCube[5][2][2]
    data.cube[5][2][1] = tempCube[5][1][2]
    data.cube[5][2][2] = tempCube[5][0][2]
    data.cube[5][1][2] = tempCube[5][0][1]
    data.cube[5][0][2] = tempCube[5][0][0]
    data.cube[5][0][1] = tempCube[5][1][0]
    data.cube[5][0][0] = tempCube[5][2][0]
    data.cube[5][1][0] = tempCube[5][2][1]

def downPrime(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[0][2][0] = tempCube[1][2][0]
    data.cube[0][2][1] = tempCube[1][2][1]
    data.cube[0][2][2] = tempCube[1][2][2]
    
    data.cube[1][2][0] = tempCube[2][2][0]
    data.cube[1][2][1] = tempCube[2][2][1]
    data.cube[1][2][2] = tempCube[2][2][2]
    
    data.cube[2][2][0] = tempCube[3][2][0]
    data.cube[2][2][1] = tempCube[3][2][1]
    data.cube[2][2][2] = tempCube[3][2][2]
    
    data.cube[3][2][0] = tempCube[0][2][0]
    data.cube[3][2][1] = tempCube[0][2][1]
    data.cube[3][2][2] = tempCube[0][2][2]
    
    data.cube[5][2][2] = tempCube[5][2][0]
    data.cube[5][1][2] = tempCube[5][2][1]
    data.cube[5][0][2] = tempCube[5][2][2]
    data.cube[5][0][1] = tempCube[5][1][2]
    data.cube[5][0][0] = tempCube[5][0][2]
    data.cube[5][1][0] = tempCube[5][0][1]
    data.cube[5][2][0] = tempCube[5][0][0]
    data.cube[5][2][1] = tempCube[5][1][0]
    
def face(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[1][0][0] = tempCube[4][2][2]
    data.cube[1][1][0] = tempCube[4][1][2]
    data.cube[1][2][0] = tempCube[4][0][2]
    
    data.cube[5][2][2] = tempCube[1][0][0]
    data.cube[5][1][2] = tempCube[1][1][0]
    data.cube[5][0][2] = tempCube[1][2][0]
    
    data.cube[3][0][2] = tempCube[5][2][2]
    data.cube[3][1][2] = tempCube[5][1][2]
    data.cube[3][2][2] = tempCube[5][0][2]
    
    data.cube[4][2][2] = tempCube[3][0][2]
    data.cube[4][1][2] = tempCube[3][1][2]
    data.cube[4][0][2] = tempCube[3][2][2]
    
    data.cube[0][0][0] = tempCube[0][2][0]
    data.cube[0][0][1] = tempCube[0][1][0]
    data.cube[0][0][2] = tempCube[0][0][0]
    data.cube[0][1][2] = tempCube[0][0][1]
    data.cube[0][2][2] = tempCube[0][0][2]
    data.cube[0][2][1] = tempCube[0][1][2]
    data.cube[0][2][0] = tempCube[0][2][2]
    data.cube[0][1][0] = tempCube[0][2][1]
    
def facePrime(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[4][2][2] = tempCube[1][0][0]
    data.cube[4][1][2] = tempCube[1][1][0]
    data.cube[4][0][2] = tempCube[1][2][0]
    
    data.cube[1][0][0] = tempCube[5][2][2]
    data.cube[1][1][0] = tempCube[5][1][2]
    data.cube[1][2][0] = tempCube[5][0][2]
    
    data.cube[5][2][2] = tempCube[3][0][2]
    data.cube[5][1][2] = tempCube[3][1][2]
    data.cube[5][0][2] = tempCube[3][2][2]
    
    data.cube[3][0][2] = tempCube[4][2][2]
    data.cube[3][1][2] = tempCube[4][1][2]
    data.cube[3][2][2] = tempCube[4][0][2]
    
    data.cube[0][2][0] = tempCube[0][0][0]
    data.cube[0][1][0] = tempCube[0][0][1]
    data.cube[0][0][0] = tempCube[0][0][2]
    data.cube[0][0][1] = tempCube[0][1][2]
    data.cube[0][0][2] = tempCube[0][2][2]
    data.cube[0][1][2] = tempCube[0][2][1]
    data.cube[0][2][2] = tempCube[0][2][0]
    data.cube[0][2][1] = tempCube[0][1][0]
    
def back(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[3][2][0] = tempCube[4][2][0]
    data.cube[3][1][0] = tempCube[4][1][0]
    data.cube[3][0][0] = tempCube[4][0][0]
    
    data.cube[5][2][0] = tempCube[3][2][0]
    data.cube[5][1][0] = tempCube[3][1][0]
    data.cube[5][0][0] = tempCube[3][0][0]
    
    data.cube[1][0][2] = tempCube[5][2][0]
    data.cube[1][1][2] = tempCube[5][1][0]
    data.cube[1][2][2] = tempCube[5][0][0]
    
    data.cube[4][2][0] = tempCube[1][0][2]
    data.cube[4][1][0] = tempCube[1][1][2]
    data.cube[4][0][0] = tempCube[1][2][2]
    
    data.cube[2][0][0] = tempCube[2][2][0]
    data.cube[2][0][1] = tempCube[2][1][0]
    data.cube[2][0][2] = tempCube[2][0][0]
    data.cube[2][1][2] = tempCube[2][0][1]
    data.cube[2][2][2] = tempCube[2][0][2]
    data.cube[2][2][1] = tempCube[2][1][2]
    data.cube[2][2][0] = tempCube[2][2][2]
    data.cube[2][1][0] = tempCube[2][2][1]
    
def backPrime(data):
    tempCube = copy.deepcopy(data.cube)
    data.cube[4][2][0] = tempCube[3][2][0]
    data.cube[4][1][0] = tempCube[3][1][0]
    data.cube[4][0][0] = tempCube[3][0][0]
    
    data.cube[3][2][0] = tempCube[5][2][0]
    data.cube[3][1][0] = tempCube[5][1][0]
    data.cube[3][0][0] = tempCube[5][0][0]
    
    data.cube[5][2][0] = tempCube[1][0][2]
    data.cube[5][1][0] = tempCube[1][1][2]
    data.cube[5][0][0] = tempCube[1][2][2]
    
    data.cube[1][0][2] = tempCube[4][2][0]
    data.cube[1][1][2] = tempCube[4][1][0]
    data.cube[1][2][2] = tempCube[4][0][0]
    
    data.cube[2][2][0] = tempCube[2][0][0]
    data.cube[2][1][0] = tempCube[2][0][1]
    data.cube[2][0][0] = tempCube[2][0][2]
    data.cube[2][0][1] = tempCube[2][1][2]
    data.cube[2][0][2] = tempCube[2][2][2]
    data.cube[2][1][2] = tempCube[2][2][1]
    data.cube[2][2][2] = tempCube[2][2][0]
    data.cube[2][2][1] = tempCube[2][1][0]
    
    