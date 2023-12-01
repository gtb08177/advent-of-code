import re

input = open(r"input.txt","r")

lines = input.readlines()

answer = 0

for line in lines:
    # Use regex to pull out all digits
    digits_arr = re.findall('\d', line)
    #print(digits_arr)
    
    if len(digits_arr) > 0:
        first_num = digits_arr[0]
        second_num = digits_arr[len(digits_arr)-1]

        concat_str = first_num + second_num
        answer = answer + int(concat_str)

input.close()

print(answer)