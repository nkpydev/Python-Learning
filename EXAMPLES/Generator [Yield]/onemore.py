def nextSquare():
    y = 1
    while True:
        yield y,y*y
        y += 1

def main():
    resultant_dict = {}
    resultant_list = []
    for x in nextSquare():
        resultant_list.append(x)
        if x[1] > 625:
            break
        #print(x)
    print(resultant_list)

if __name__ == '__main__':
    main()