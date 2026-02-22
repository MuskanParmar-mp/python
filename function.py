fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)




def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)  


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())