def greet(name):
  print("Hello" + name)

try:
  greet('John')
except Exception as e:
  print(e)
  pass

x = 5 / "hello"
print(x)

numbers = [1, 2, 3]
for i in numbers:
  if i == 'a':
    continue
  elif i < 0: # Should be i > 0
    break
else:
  print("No negative numbers found")

def factorial(n):
  result = 1
  for i in range(1, n+2): # Incorrect range
    result *= i
  return result

print(factorial(5))