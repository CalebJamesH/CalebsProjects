# Function to get a number and to make sure that it is in between the min and max parameters
def valid_int(question, min, max):
    """
    get a whole number between the min and max parameters
    
    Args:
        question (string): A s
        arg2 (type): Description of arg2
    
    Returns:
        type: Description of the return value
    """
    x = int(input(question))
    while((x < min) or (x > max)):
        x = int(input(question))

# Function to calculate the factorial of the numbers received from valid_int function
def factorial(num):
    """
    Calculates the factorial of given number
    
    Args:
        num (int): a whole number above 0
    
    Returns:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat = fat * i
    return fat
    
x = valid_int('Type a value to calculate the factorial: ', 0, 9999)
print(f"{x}! - {factorial(x)}")