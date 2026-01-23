def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
a=int(input("Enter the first number:"))
b=int(input("Enter the second number"))
c=input("Enter the operation symbol:")
if c=="+":
    add(a,b)
elif c=="-":
    sub(a,b)
elif c=="*":
    mul(a,b)
elif c=="/":
    div(a,b)
else:
    print("Invalid symbol")
    
