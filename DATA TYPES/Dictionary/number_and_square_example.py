# We want the Output to be a Dict - {1:1,2:4,3:9...}
def basic_method(user_input):
    sq_of_number = lambda num: num*num
    result_dict_1 = {}
    for x in user_input:
        result_dict_1[x] = sq_of_number(x)
    print(result_dict_1)

def pythonic_simple_method(user_input):
    result_dict_2 = {x:x*x for x in user_input}
    print(result_dict_2)

if __name__ == "__main__":
    user_input = [1,2,3,4,5,6,7,8,9,10]
    user_choice = int(input('\nEnter your Choice: 1] Basic Method\t2] Pythonic Simple Method:\t'))
    if user_choice == 1:
        basic_method(user_input)
    elif user_choice == 2:
        pythonic_simple_method(user_input)
    else:
        print('Wrong Choice!!')