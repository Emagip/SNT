##
##Simple program made for SNT course.
##Find square root using Héron method.
##Copyrights: Pigeaud Maxime
##hsqrt is for Héron SQuare RooT
##use the random module to set the value of x
##

import random as r
def hsqrt(a): # define the function
    e=[] # init a list to store the values
    x = r.randrange(2, 25, 1) # use the random module to set the value of x, from 2 to 25 in 1 to 1
    if a < 0 : # because negative value do not work, i block you and i quit the program
        print("Juste non. Essaye pas, ca marche pas. (Just don't. Do not try, i doesn't work.)") # """"Bad humor""""
        exit() # Evil action
    if a == 0:
        L=10
        for i in range(100):
            l=a/L
            L=(l+L)/2
        return L
    for i in range(15): # 15 iterations should be enough
        l = a/x # set l to a per x (for simplicity)
        x=(x+l)/2 # set x to itself plus l over 2
        e.append(x) # add x value to the e list and restart
    print(e[14]) # output the fifteenth value of the e list
