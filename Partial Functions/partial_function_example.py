from functools import partial

def multiplication(x,y):
    return x * y

multiply_by_4 = partial(multiplication,4)

print(multiply_by_4(10))