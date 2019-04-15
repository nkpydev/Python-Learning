# Fibonacci Sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    
if __name__ == "__main__":
    user_input = int(input('\nEnter till how many terms:\t'))
    if user_input <= 0:
        print('\nFibonacci Sequence is for Positive numbers!!')
    else:
        print('\nFibonacci Sequence:\n')
        for i in range(user_input):
            print(fibonacci(i),end=',')
        print('\n')