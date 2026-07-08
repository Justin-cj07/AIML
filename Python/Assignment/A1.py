#1. Add two numbers
a=10
b=50
result1=a+b
print(result1)

#2.check condition a<10 and a>b
a=10
b=50
result2=a<10 and a>b
print(result2)

#3. check conditions a,b is both/not/either divisble by 10
a=10
b=50
if a%10==0 and b%10==0:  #both
    print(True)
elif a%10==0 or b%10==0: #either
    print(True)
else:                    #neither
    print(False)

#4 Find the first digit of a 4 digit number
n=4567
result4=n//1000
print(result4)

#5 Find the last digit of a 4 digit number
n=4567
result5=n%10
print(result5)

#6 Find the remainder where a is divisor and b is dividend
a=10
b=50
result6=b%a
print(result6)

#7 Multiply two numbers
a=10
b=50
result7=a*b
print(result7)

#8 Calculate total marks and average
a=60
b=70
c=80
sum=a+b+c
avg=sum/3
print("Total marks=",sum,"Average marks= ",avg)