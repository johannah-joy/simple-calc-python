'''
1. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.
  > What is the operation you'd like to perform? +
  > What is the first number? 5
  > What is the second number? 12
  > 5 + 12 = 17

2. Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.
  > what is the operation you'd like to perform? +
  > what is the first number? 5
  > what is the second number? 12
  > 5 + 12 = 17
  > what is the operation you'd like to perform? done
  > goodbye!
'''
#x = [num1 {operation} num2]
operation = ["+", "-", "*", "/"]
while True:
  op_input = input("What is the operation you'd like to perform (+, -, *, or /) or type done: ")
  if op_input == "done":
    break
  elif op_input in op_input:
    num1 = float(input("first number: "))
    num2 = float(input("second number: "))
    if op_input == "+":
      print(f"{num1} {op_input} {num2} = ")
      print(num1 + num2)
    elif op_input == "-":
      print(f"{num1} {op_input} {num2} = ")
      print(num1 - num2)
    elif op_input == "*":
      print(f"{num1} {op_input} {num2} = ")
      print(num1 * num2)
    elif op_input == "/":
      print(f"{num1} {op_input} {num2} = ")
      print(num1 / num2)
    else:
      print("Invalid input")
