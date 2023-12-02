import sys

digits_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def create_first_digit_dict(line):
    first_digit_dict = {}
    for i in range(len(digits_list)):
        word_index = line.find(digits_list[i])
        if word_index != -1:
            first_digit_dict.update({word_index:i})
    for i, c in enumerate(line):
        if c.isdigit() == True:
            first_digit_dict.update({i:int(c)})
    min_value_key = min(first_digit_dict.keys())
    min_value = first_digit_dict[min_value_key]
    return str(min_value)

def create_last_digit_dict(line):
    last_digit_dict = {}
    for i in range(len(digits_list)):
        word_index = line.rfind(digits_list[i])
        if word_index != -1:
            last_digit_dict.update({word_index:i})
    for i, c in enumerate(line):
        if c.isdigit() == True:
            last_digit_dict.update({i:int(c)})
    max_value_key = max(last_digit_dict.keys())
    max_value = last_digit_dict[max_value_key]
    return str(max_value)

with open(sys.argv[1], 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)
sum = 0
for line in lines:
    first = create_first_digit_dict(line)
    last = create_last_digit_dict(line)
    combined_digits = first+last
    sum = sum + int(combined_digits)
print(sum)