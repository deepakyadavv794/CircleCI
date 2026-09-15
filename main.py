def to_upper(name):
  return name.upper()
def say_hello(name):
  return f"Hello, {name}!"
if __name__ == "__main__":
  name = input("Enter your name: ")
  upper_name = to_upper(name)
  greeting = say_hello(upper_name)
  print(greeting)