n=int(input("Enter a number: "))
n1=int("%s" %n)
n2=int("%s%s" %(n,n))
n3=int("%s%s%s" %(n,n,n))
num=n1+n2+n3
print(f"The value is: {num}")