first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

fird_string = first_strings + second_strings

first_result = [string for string in first_strings if len(string) > 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x:len(x) for x in fird_string if len(x) % 2 == 0}

print(first_result)

print(second_result)

print(third_result)