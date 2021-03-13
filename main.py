#First we have to create a function using "def" instruction
def greet_user():
  print("\nPlease enter your name")
  name=input()
  print("Hello", name)
#Line 2 is the actual function.This line will not be executed without calling the function.
#To call the function we simply use its name once.You can call a function multiple time.If you want to execute the function 3 times, the programm will look  like this:
greet_user()
greet_user()
greet_user()