#Write a Program to solve Quadratic Equation depending upon the value of Delta.

#Details:
#The program is used to solve quadratic equation i.e. ax2 + bx + c = 0 depending upon the value of Delta.
#The formula for calculating Delta is d = b*b-4*a*c.

import cmath
a = int(input("Please enter the 'a ' value of a Quadratic Equation : "))
b = int(input("Please enter the 'b' Value of a Quadratic Equation : "))
c = int(input("Please enter the 'c' Value of a Quadratic Equation : "))


# calculate the discriminant
d = (b**2) - (4*a*c)         #CALCULATING THE VALUE OF DISCRIMINANT

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The value of discriminant is',d)
print('The solution are ',sol1,sol2)