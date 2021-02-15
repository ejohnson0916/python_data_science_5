# Write a Python Program to execute a string containing Python Code


def exec_code():
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC)


# Driver Code
exec_code()

# Write a Python Function to insert a string in the middle of a string


def insert_string(str, word):
    midpoint = len(str)//2
    return str[:midpoint] + word + str[midpoint:]


print(insert_string('This is a python program', '(Hello World)'))


