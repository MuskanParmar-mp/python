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



