n=int(input("Enter the number of terms:"))
fib=[]
a,b=0,1
for i in range(n):
    fib.append(a)
    a,b=b,a+b
print(fib)
sumi=sum(fib)
print(sumi)
