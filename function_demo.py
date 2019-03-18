def square_plus_one(a):
    return a**2+1

square_plus_one(9)
square_plus_one(2)
square_plus_one(100)

def triangle_area(base,height):
    return (base*height)/2

triangle_area(1,2)

for i in range(100):
    print(square_plus_one(i))


# version 1

def quadratic(a,b,c):
    # a*x**2+b*x+c=0
    import cmath
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {} and {}'.format(sol1, sol2))

quadratic(1,2,3)

# version 2

def quadratic1(a,b,c):
    import cmath, math
    d = b**2-4*a*c
    if d < 0:
        sol1 = (-b - cmath.sqrt(d)) / (2 * a)
        sol2 = (-b + cmath.sqrt(d)) / (2 * a)
        print('The solution are {} and {}'.format(sol1, sol2))
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print ("This equation has one solutions: ", x)
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
        print ("This equation has two solutions: ", x1, " and", x2)

quadratic1(1,2,3)

def bmicalc(weight,height):
    bmi=703*(weight/height**2)
    if bmi>=30:
        print("Obesity:{:.2f} ".format(bmi))
    elif bmi>=25:
        print("Overweight:{:.2f} ".format(bmi))
    elif bmi>18.5:
        print("Normal weight:{:.2f} ".format(bmi))
    else:
        print("Underweight:{:.2f} ".format(bmi))

bmicalc(190.66,75)

def fab(n):
    """ this function will return the nth fabonacci nubmer
    this parameter
    :param n:
    :return:
    """
    if n== 1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

fab(1)

fab(6)

for i in range(1,10):
    print(fab(i))