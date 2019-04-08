# We want the Output to be a Dict - {1:1,2:4,3:9...}
# We also want to use the LAMBDA Function

user_input = [1,2,3,4,5,6,7,8,9,10]
sq_of_number = lambda num: num*num
result_dict = {}


for x in user_input:
    result_dict[x] = sq_of_number(x)
print(result_dict)