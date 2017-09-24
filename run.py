import sys
import random

def displayMatrix(mat):
    print " ", " ".join([str(x) for x in xrange(len(mat))])
    for i, x in enumerate(mat):
        print i, " ".join([str(y) for y in x])



def intialLifeDensity(Board_T, density,num):
    aliveCells=0
    aliveCellsGoal=int(density*num*num)
    print("Our aliveCellsGoal is : "+str(aliveCellsGoal))
    for i in range(num):
        for j in range(num):
            Board_T[i][j] = int(random.random()<=density)
            aliveCells+=Board_T[i][j]

    if (aliveCells<aliveCellsGoal):
        while (aliveCells<aliveCellsGoal):
            i=random.randint(0,num-1)
            j=random.randint(0,num-1)
            aliveCells+=1-Board_T[i][j]
            Board_T[i][j]=1
                
    if (aliveCells>aliveCellsGoal):
        while (aliveCells>aliveCellsGoal):
            i=random.randint(0,num-1)
            j=random.randint(0,num-1)
            aliveCells-=Board_T[i][j]
            Board_T[i][j]=0
    


def initGame():
    num = int(raw_input("Please chose a size for the game : "))
    density = float(raw_input("Please chose an intial life density for this game (between 0 and 1): "))
    Board_T = [ num*[0] for i in range(num) ]
    intialLifeDensity(Board_T,density,num) #setting the initial board to the proper life density
    print("Board_T matrix :")
    displayMatrix(Board_T)
    Board_TPlus1 = [ num*[0] for i in range(num) ]
    print("\nBoard_TPlus1 matrix :")
    displayMatrix(Board_TPlus1)











if __name__ == "__main__":
    if (len(sys.argv)==1):
	    initGame()
    else :
        print('run.py : There was an issue with the number arguments passed to this function : too many arguments, aborting.')

    
