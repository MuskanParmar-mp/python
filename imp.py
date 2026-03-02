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

for i in range(1, 10):
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





num = int(input("Enter number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")






n = int(input("Enter limit: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b







text = input("Enter string: ")
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels =", count)






text = input("Enter string: ")
print("Reverse =", text[::-1])





a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("1.Add 2.Sub 3.Mul 4.Div")
choice = input("Choose option: ")

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
elif choice == "3":
    print(a * b)
elif choice == "4":
    print(a / b)
else:
    print("Invalid Choice")












num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)


num = int(input("Enter number: "))
temp = num
total = 0
digits = len(str(num))

while temp > 0:
    d = temp % 10
    total += d ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")





n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)




for i in range(1, 51):
    if i % 2 != 0:
        print(i)




nums = [10, 21, 4, 45, 66, 93]
even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)        










nums = [5, 20, 10, 40, 15]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest =", largest)



nums = [5, 20, 10, 40, 15]
smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print("Smallest =", smallest)