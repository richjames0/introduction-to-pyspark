import random

random.seed(42)

file = open('/Users/Richard/Desktop/addresses.txt')

for line in file:
    random_number = random.random()
    if random_number < 0.2:
        line = line.upper()
    elif random_number < 0.4:
        line = line.lower()
    if int(random_number * 10) % 4 == 0:
        line = line.replace(' ', '')
    if int(random_number * 100) % 10 % 4 == 0:
        line = line.replace('o', '0').replace('O', '0').replace('e', '3').replace('E', '3')
    print(line)