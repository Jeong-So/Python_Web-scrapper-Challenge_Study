while True:
  print("Choose a number:")
  num1 = input()
  print("Choose another one:")
  num2 = input()
  if num1.isnumeric() and num2.isnumeric():
    print("Choose an operation: \n\tOptions are: +, -, * or /. \n\tWrite 'exit' to finish.")
    operation = input()
    if operation == '+':
      print("Result: ", int(num1)+int(num2))
    elif operation == '-':
      print("Result: ", int(num1)-int(num2))
    elif operation == '*':
      print("Result: ", int(num1)*int(num2))
    elif operation == '/':
      print("Result: ", int(num1)/int(num2))
    elif operation == 'exit':
      break
    else:
      print("operation을 올바르게 입력하세요")
  else:
    print("숫자를 입력하세요.")
    
  