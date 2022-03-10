def a(m,n):
  return(m+n)
def b(m,n):
  return(m-n)
def c(m,n):
  return(m*n)
def d(m,n):99
  return(m%n)
def e(m,n):
  return(m//n)
def f(m,n):
  return(m**n)
def g(m,n):
  return(m/n)
def calculation(num1,num2):
  sum=a(num1,num2)
  sub=b(num1,num2)
  multi=c(num1,num2)
  div=d(num1,num2)
  div2=e(num1,num2)
  exponent=f(num1,num2)
  div3=g(num1,num2)
  return sum,sub,multi,div,div2,exponent,div3
num1=int(input("enter number="))
num2=int(input("enter number="))
print(calculation(num1,num2))


