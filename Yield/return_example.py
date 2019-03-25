#-----------------------------------------------------------------#
#! Python3
# Author            : NK
# Month, Year       : March, 2019
# Info              : Program to get Squares of numbers upto 25, using return
# Desc              : An example program to show usage of return
#-----------------------------------------------------------------#

def nextSquare(x):
    return x*x
        
def main():
    for x in range(25):
        print(nextSquare(x))

if __name__ == '__main__':
    main()