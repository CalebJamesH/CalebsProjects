number_one = float(input("give me a number: "))
number_two = float(input("give me a second number: "))
operation = input("select operation: ")

if operation == "+":
    result = number_one + number_two
elif operation == "-":
    result = number_one - number_two
elif operation == "*":
    result = number_one * number_two
elif operation == "/":
    if number_two != 0:
        result = number_one / number_two
    else:
        result = "N/A"
else: 
    result = "Invalid operation"

print(f"{number_one} {operation} {number_two} = {result}")
  