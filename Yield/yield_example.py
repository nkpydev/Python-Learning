#-----------------------------------------------------------------#
#! Python3
# Author            : NK
# Month, Year       : March, 2019
# Info              : Program to get Squares of numbers upto 25, using yield
# Desc              : An example program to show usage of yield
#-----------------------------------------------------------------#

def nextSquare():
    i = 1
    while True:
        yield i*i
        i += 1

def main():
    for num in nextSquare():
        if num > 625:
            break
        print(num)

if __name__ == '__main__':
    main()