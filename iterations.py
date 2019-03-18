sum=0
# for i in range(100):
#     print("in the {}th iteration, current i is{}, sum is {}".format(i,i,sum))
#     sum= sum+i
#     print("\t after adding {} , the new sum is {}\n".format(i,sum))

sum=0
for i in range(1001):
    sum=sum+i**2
    print(sum)




name="alexandros"
sum=0
for letter in name:
    sum =sum+ (ord(letter) - 96)

print(sum)
def countdown(n):
    while n>0:
        print(n)
        n=n-1
        import time
        time.sleep(.5)
    print("Breaktime")


countdown(20)
# odd numbers
result=0
for number in range(1,1001,2):
    result=result+number
print(result)

# even numbers
result=0
for number in range(0,1001,2):
    result=result+number
print(result)