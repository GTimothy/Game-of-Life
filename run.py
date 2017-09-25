import sys
import random
import curses
import time


def displayMatrix(mat):
    
    string =" "+ " ".join([str(x) for x in xrange(len(mat))])
    for i, x in enumerate(mat):
        string+="\n"+str(i)+" "+ " ".join([str(y) for y in x])
    win.addstr(0,0,string)
    win.refresh()
    time.sleep(0.2)



def intialLifeDensity():
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
    global win
    global num
    num = int(raw_input("Please chose a size for the game : "))
    global density
    density = float(raw_input("Please chose an intial life density for this game (between 0 and 1): "))
    stdscr = curses.initscr()

    
    Board_a = [ num*[0] for i in range(num) ]
    global Board_T
    Board_T = Board_a
    intialLifeDensity() #setting the initial board to the proper life density
  #  print("Board_T matrix :")
  #  displayMatrix(Board_T)
    Board_b = [ num*[0] for i in range(num) ]
    global Board_TPlus1
    Board_TPlus1 = Board_b
  #  print("\nBoard_TPlus1 matrix :")
  #  displayMatrix(Board_TPlus1)
    winSize = len(" "+ " ".join([str(x) for x in xrange(len(Board_T))]))
    win = curses.newwin(10+winSize,10+winSize,5,10)
    for i in range(100):
        #print("\ntick   ")
        tick()
        displayMatrix(Board_T)

    curses.endwin()



def tick():
    global Board_T
    global Board_TPlus1
    #displayMatrix(Board_T)
    #print(num)

    for i in range(num):
        for j in range(num):
            imin1=i-1
            iplus1=i+1
            if (i==0):
                imin1=num-1
            elif (i==num-1):
                iplus1=0

            jmin1=j-1
            jplus1=j+1
            if (j==0):
                jmin1=num-1
            elif (j==num-1):
                jplus1=0

#            print("\nCalculing for \n\ti="+str(i)+",imin1="+str(imin1)+",iplus1="+str(iplus1)+"\n\tj="+str(j)+",jmin1="+str(jmin1)+",jplus1="+str(jplus1))
#            print(">>Board_T[imin1][jmin1]="+str(Board_T[imin1][jmin1])+", Board_T[imin1][j]="+str(Board_T[imin1][j]) + ", Board_T[imin1][jplus1]="+str(Board_T[imin1][jplus1])+", Board_T[i][jmin1]="+str(Board_T[i][jmin1])+ ", Board_T[i][jplus1]="+str(Board_T[i][jplus1]) + ", Board_T[iplus1][jmin1]="+str(Board_T[iplus1][jmin1])+", Board_T[iplus1][j]="+str(Board_T[iplus1][j])+", Board_T[iplus1][jplus1]="+str(Board_T[iplus1][jplus1]))
            
            Surrounding = Board_T[imin1][jmin1] + Board_T[imin1][j] + Board_T[imin1][jplus1] + Board_T[i][jmin1] + Board_T[i][jplus1] + Board_T[iplus1][jmin1] + Board_T[iplus1][j] + Board_T[iplus1][jplus1]

            #print(">>Surrounding ="+str(Surrounding))
            if (Board_T[i][j]==0):
#                print("Board_T["+str(i)+"]["+str(j)+"] is DEAD")
                if (Surrounding==3):
#                    print("\t and is surrounded by 3 alive !!! \n\t>>Becomes ALIVE")
                    Board_TPlus1[i][j]=1
                else :
                    Board_TPlus1[i][j]=0
            else:
#                print("Board_T["+str(i)+"]["+str(j)+"] is ALIVE")
                if (not (Surrounding==2 or Surrounding==3)):
#                    print("\t and is surrounded by <2 or >3 alive !!! \n\t>>Becomes DEAD")
                    Board_TPlus1[i][j]=0
                else :
                    Board_TPlus1[i][j]=1
            
#    displayMatrix(Board_TPlus1)
    temp = Board_T
    Board_T=Board_TPlus1
    Board_TPlus1=temp











if __name__ == "__main__":
    if (len(sys.argv)==1):
	    initGame()
    else :
        print('run.py : There was an issue with the number arguments passed to this function : too many arguments, aborting.')

    
