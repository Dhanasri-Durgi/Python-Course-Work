a=input("Enter your name:")
b=list(map(float,input("Enter your marks:").split()))

sum1=sum(b)
len1=len(b)
avg=sum1/len1
print("Sum of given marks:",sum1)
print("Average of given marks:",avg)
