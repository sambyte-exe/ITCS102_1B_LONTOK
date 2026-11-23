def my_factorial(sagot):
  fact = 1
  for x in range(sagot):
    fact *= x
  return fact

print('output', my_factorial(13))
print('output', my_factorial(7))
print('output', my_factorial(8))
print('output', my_factorial(5))
print('output', my_factorial(21))
