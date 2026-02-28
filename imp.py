num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")




num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")    




a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print("a is greater")
else:
    print("b is greater")    






a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("a is greatest")
elif b > c:
    print("b is greatest")
else:
    print("c is greatest") 





a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("a is greatest")
elif b > c:
    print("b is greatest")
else:
    print("c is greatest")





year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")






num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)





num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)



num = int(input("Enter number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reverse =", rev)







num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")







num = int(input("Enter number: "))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum =", total)
