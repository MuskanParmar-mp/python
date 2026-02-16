#arthimetic practice question
# Write a program that takes two numbers as input from a user and prints their sum, difference, product, quotient, and the remainder.

# x = int(input("enter a no : "))
# y = int(input("enter a no : "))
# print("sum =",x+y)

# a = int(input("enter a no :"))
# b = int(input("enter a no:"))
# difference = a - b
# print("difference = ",difference)

# p = 2
# q = 5
# print("product = ", p*q)


# x = float(input("enter a no : "))
# y = float(input("enter a no : "))
# print("division =",x/y)


# m  = 10
# n = 3
# print("reminder = ", m%n)


# #Calculate the area of a rectangle given its length and width as inputs.

length = int(input("enter a len :"))
width = int(input("enetr a width :"))
ans = length * width
print(ans)

#Find the square and cube of a number using the exponentiation (**) operator.

num = int(input("Enter a number: "))

print("Square is:", num ** 2)
print("Cube is:", num ** 3)

#Swap the values of two variables (e.g., a and b) without using a third temporary variable, using arithmetic operators.

a = int(input("enter a no :"))
b = int(input("enter a no :"))

a = a + b 
b = a - b
a = a - b

print("a =", a)
print("b =", b)
