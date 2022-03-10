num1=int(input("enter number="))
num2=int(input("enter the number="))
sign=input("operator=")
def sum(num1,num2):
  if sign=="+":
    print(num1+num2)
def sub(num1,num2):
  if sign=="-":
    print(num1-num2)
def multi(num1,num2):
  if sign=="*":
    print(num1*num2)
def exponent(num1,num2):
  if sign=="**":
    print(num1**num2)
def div(num1,num2):
  if sign=="%": 
    print(num1%num2)
def main():
  sum(num1,num1)
  sub(num1,num2)
  multi(num1,num2)
  exponent(num1,num2)
  div(num1,num2)
main()