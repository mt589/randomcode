import random
numbers = []
for x in range (100):
    numbers.append(random.randint(10,99))
print (numbers)

for item in numbers:
    if item % 5 == 0:
        print(item)
