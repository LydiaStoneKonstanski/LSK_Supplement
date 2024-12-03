single_digits = list(range(10))
#print(single_digits)
squares = []
for digit in single_digits:
  squares.append(digit * digit)
  print(digit)
  digit += 1
print(squares)

cubes = [digit ** 3 for digit in single_digits]

print(cubes)