squares=[i*i for i in range(6)] #list comprehension is used to create a list in one line
print(squares)

numbers=[1,2,3,4,5]
square=[]
for i in numbers:
    square.append(i*i)
print(square)

numbers=[1,2,3,4,5]
square=[i*i for i in numbers]
print(square)

squares=[i*i for i in range(1,6)] 
print(squares)

even=[i for i in range(1,11) if i%2==0] #list comprehension with even condition
print(even)

odd=[i for i in range(1,11) if i%2!=0] #list comprehension with odd condition
print(odd)

names=["rahul","sachin","saurav"]
upper_names=[name.upper() for name in names] #list comprehension with upper case
print(upper_names)

names=['RAHUL', 'SACHIN', 'SAURAV']
lower_names=[name.lower() for name in names] #list comprehension with lower case
print(lower_names)

names=['RahuL', 'SachiN', 'SauraV']
swap_names=[name.swapcase() for name in names] #list comprehension with swap case
print(swap_names)

names=['Rahul', 'Sachin', 'Saurav']
lengths=[len(name) for name in names]
print(lengths)

result=['even' if x%2==0 else "Odd" for x in range(1,9)]
print(result)

matrix=[[j for j in range(4)]for i in range(4)]
print(matrix)

#Functions are a reusable block of code used to perform specific task

def greet(name,age): 
    return f"Hello, {name} and {age}" 

Name=input("Enter your Name: ")
age=int(input("Enter your Age: "))
res=greet(Name,age)
print(res)


def add(a,b): #add 2 numbers
    return a+b
a=2
b=3
res=add(a,b)
print(res)

square=lambda x:x*x #lambda functions are used to specify the function in one line
print(square(5))


multiply=lambda a,b:a*b #this could be used to pass multiple variable

a=int(input("Enter no"))
b=int(input("Enter no"))
print(multiply(a,b))

students=[("aman",80),("Rahul",60),("Priya",88)]
students.sort(key=lambda x:x[1])
print(students)