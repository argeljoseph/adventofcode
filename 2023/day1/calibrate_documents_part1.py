import sys

def get_first_digit(line_from_list):
    for i, c in enumerate(line_from_list):
        if c.isdigit() == True:
            return c
            break

def reverse_string(line_from_list):
    return line_from_list[::-1]

def combine_digits(first, second):
    number = first + second
    return int(number)

with open(sys.argv[1], 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)

sum = 0
for line in lines:
    first_digit = get_first_digit(line)
    last_digit = get_first_digit(reverse_string(line))
    number = combine_digits(first_digit, last_digit)
    print(number)
    sum = sum + number

print(sum)