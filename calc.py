# ex 1
# print("hello, world")
#
# print("hello, class")
#
# print((3+15+2+43)*2019)
#
# print("Hey Jude","Don't make it bad")

# print("1+2+3=',1+2+3)

# name=input("What's your name?")
# print("hello",name,"!")
#
# a="ABC"
# # b=a
# # a="XYZ"
# # print(b)
#
# # print("a is ",a,"b is",b)
# #
# # # first_name='John'
# # # last_name='Lennon'
# # name=first_name+" "+last_name
# # age=input("How old are you?")
# # # print(first_name+" "+last_name)
# # #print(first_name*20)
# # print("hello,{}! you are {}! years old.".format(name,age))
# template="hello,{name}! you are {age}! years old."
# name1="Grace"
# age1=20
#
# name2="Aida"
# age2=18
#
# print(template.format(age=age1,name=name1))
# print(template.format(name2,age2))
#
# print('Pi equals {:.2f}'.format(3.1415926))
#
#
# import math
# print(math.pow(math.pi,5))
# print(math.pi)
# print(2**38)
# # If you run a 10 kilometer race in 42 minutes 42 seconds,
# what is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?
# distance in miles
x=10*0.621371
# minutes
minutes=42+42/60
minpace=minutes/x
# seconds
seconds=42*60+42
secpace=seconds/x
# hour
hour=minutes/60
hourpace=hour/x
# Answer
print("Average mile pace in minutes:{:.2f}, Average mile pace in seconds:{:.2f}, Average mile pace in hours:{:.2f}.".format(minpace,secpace,hourpace))
#
# Add more into calc.py. Add comments when necessary.
#
# The volume of a sphere with radius r is $$(4/3)\pi r^3.$$ What is the volume of a sphere with radius 5?
import math
r=input("enter radius")
volume=(4/3)*math.pi*math.pow(float(r),3)
print("The sphere's volume is:{:.2f}".format(volume))
#
# Suppose the cover price of a book is \$24.95, but bookstores get a 40\% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
coverp=24.95
shipc=3
addship=.75
bookn=60
discount=.4
price=coverp*bookn*discount+shipc+addship*(bookn-1)
print("The total wholesale cost for {} copies is ${:.2f}".format(bookn,price))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and
# 1 mile at easy pace again,
# what time do I get home for breakfast?

import datetime
hour=6
minutes=52
epace=8+15/60
tpace=7+12/60
measy=4
mtempo=1
time_running=epace*measy+tpace*mtempo
print(time_running)
now=datetime.time(hour,minutes)

btime=now+datetime.time(hour,minutes+(time_running))
print(btime)
# If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.