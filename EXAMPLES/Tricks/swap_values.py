
def normal_old_school_method(a,b,tmp):
    tmp = a
    a = b
    b = tmp
    return a,b

def pythonic_swap(a,b):
    a,b = b,a
    return a,b

if __name__ == '__main__':
    a,b = 10,25
    tmp = 0
    print('Original [Before Swap Values]:\t',a,b)
    print('Old School Method:',normal_old_school_method(a,b,tmp))
    print('Pythonic Method:',pythonic_swap(a,b))