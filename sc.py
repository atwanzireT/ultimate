import random


list_of_numbers = [i for i in range(10)]

code = []
for i in range(4):
    number = random.choice(list_of_numbers)
    code.append(number)

    string_code = "".join(str(item)  for item in code)

print(code)
print(string_code)

