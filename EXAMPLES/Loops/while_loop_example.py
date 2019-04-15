'''
This is to print:
*
**
***
****
*****
'''
def ascending_print(asterick):
    count = 0
    while count < 5:
        for i in range(count):
            print(asterick,end='')
        print('\n')
        count += 1


'''
This is to print:
*****
****
***
**
*
'''
def descending_print(asterick):
    count = 5
    while count != 0:
        for j in range(count):
            print(asterick,end='')
        print('\n')
        count -= 1

if __name__ == "__main__":
    user_input = int(input('\nEnter your choice: 1]\t2]:\t'))
    asterick = '*'
    if user_input == 1:
        ascending_print(asterick)
    elif user_input == 2:
        descending_print(asterick)
    else:
        print('Wrong Choice!')
