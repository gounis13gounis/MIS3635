# I ran them in the console by shift+Alt+E
print(3.14e-2)

122+222

1.2*23

5/2

2**100

2**1000000

length_of_number=len(str(2**1000000))
print(length_of_number)
print(len("Alexandros"))

print(math.pi)

print(math.sqrt(25))

# random library

import random
print(random.random())

print(int(random.random()*100))

print(random.randint(1,6))

print(random.choice([1,2,3,4,5,6,7,8,9]))

print(random.choice(["Name","Name1","Name2","Name3"]))



low=int(input("please enter your lower bound"))
up=int(input("please enter your upper bound"))
print(random.randint((low),(up)))


# strings

print("I'm saying \"okay\"." )
print("I\"m learning\n\nPython.")



# Boolean

print(3>4)
print(3>2)

print(3>2 and 3>5)
print(3>2 or 3>5)

print(1==2)

n=int(input())
print(n>3)

# Conditionals
age=int(input("How old are you?"))
us=input("are you in us(write in lower case yes or no)")
if age>=21 and us.lower()=="yes":
    print("Yes you may")
elif age>=18 and us.lower()=="no":
    print("Yes you may")
else:
    print("stay out")
