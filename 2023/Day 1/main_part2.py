import re
input = open(r"input.txt","r")
lines = input.readlines()

answer = 0
dict_number = {
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8', 
    "nine" : '9'
}


for line in lines:

    digits_arr = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

    if len(digits_arr) > 0:

        first_num = digits_arr[0]
        second_num = digits_arr[len(digits_arr)-1]

        if not first_num.isdigit():
            first_num = dict_number[first_num]

        if not second_num.isdigit():
            second_num = dict_number[second_num]


        concat_str = first_num + second_num
        answer = answer + int(concat_str)

input.close()

print(answer)