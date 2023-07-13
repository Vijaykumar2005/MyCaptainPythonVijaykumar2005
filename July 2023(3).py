n=int(input("Enter length of fabonacci sequence:"))
a=0
b=1
count=2

if n<0:
  print("Enter only positive values")
elif n==1:
  print(a)
else:
  print(a)
  print(b)
  while count<n:
    c=a+b
    print(c)
    count+=1
    a=b
    b=c
