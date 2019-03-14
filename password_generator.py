#--- Generic Imports ---#
import string
import random
from random import randint

if __name__ == '__main__':
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for x in range(randint(8,16)))
    print('Password:\t',password)