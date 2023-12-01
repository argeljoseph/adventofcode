import sys

digits_dict = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

def get_digits(line_from_list):
    digits_word_index = []
    digits_index = []
    number = []
    for num in digits_dict:
        word_num = line_from_list.find(num)
        if word_num != -1:
            digits_word_index.append(word_num)
    for i, c in enumerate(line_from_list):
        if c.isdigit() == True:
            digits_index.append(i)
    numbers_index = digits_index + digits_word_index
    numbers_index.sort()
    if line_from_list[numbers_index[0]].isdigit():
        first_digit = line_from_list[numbers_index[0]]
        number.append(first_digit)
    else:
        for num in digits_dict:
            word_num =line_from_list.find(num)
            if word_num == numbers_index[0]:
                number.append(digits_dict[num])
                break
    if line_from_list[numbers_index[-1]].isdigit():
        last_digit = line_from_list[numbers_index[-1]]
        number.append(last_digit)
    else:
        for num in digits_dict:
            word_num =line_from_list.find(num)
            if word_num == numbers_index[-1]:
                number.append(digits_dict[num])
                break
    return number

with open(sys.argv[1], 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)
sum = 0
for line in lines:
    number = get_digits(line)
    combine_digits = number[0] + number[1]
    sum = sum + int(combine_digits)

print(sum)
