print("Hello, World!") 


name = "Muskan"
age = 20
price = 99.50
is_active = True

print(name, age, price, is_active)


name = input("Enter your name: ")
print("Welcome", name)


age = int(input("Enter age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")




num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


for i in range(1, 6):
    print(i)    


i = 1
while i <= 5:
    print(i)
    i += 1

num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)


def add(a, b):
    return a + b

print(add(5, 10))



def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))


fruits = ["apple", "banana", "mango"]
print(fruits)
fruits.append("orange")
print(fruits)


numbers = [10, 20, 30, 40]

for n in numbers:
    print(n)




data = (10, 20, 30)
print(data)



nums = {1, 2, 3, 3, 4}
print(nums)


student = {
    "name": "Muskan",
    "age": 20,
    "course": "Python"
}

print(student["name"])



name = "Python"
print(name[::-1])



text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



file = open("data.txt", "w")
file.write("Hello Python")
file.close()



x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



