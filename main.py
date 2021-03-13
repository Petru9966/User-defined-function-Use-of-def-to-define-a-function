#First we have to create a function using "def" instruction
def greet_user():
  print("\nPlease enter your name")
  name=input()
  print("Hello", name)
#Line 2 is the actual function.This line will not be executed without calling the function.
#To call the function we simply use its name like this
greet_user()