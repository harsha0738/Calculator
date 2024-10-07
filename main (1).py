def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operation = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
}

# print(operation["*"](4,8))

another_continue = True
while another_continue:
  should_continue = True
  num1 = float(input("enter the first number: "))
  while should_continue:
      for i in operation:
        print(i)
      symbol = input("enter a operator you want : ")
      num2 = float(input("enter the second number? : "))
      answer = operation[symbol](num1, num2)
      print(f"{num1} {symbol} {num2} = {answer}")
  
      choice = input(f"type 'yes' if you want to perform with {answer}? or 'no' to start a new calculation.: ")
  
      if choice == "yes":
          num1 = answer
      else:
          should_continue = False
          print("\n" * 20)
        

  