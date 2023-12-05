
# 142 characters per line
# adjacent means next to or diagonally
# full stops don't count '.'

import re

def get_valid_numbers_strings(line):

    output = re.findall("([^\.]*[0-9]+[^\.]*)",line)

    # .usedigit() will return true IFF there is no symbol, therefore if it is false, we can deduce there is a symbol present
    inline_valid_numbers = [num for num in output if not num.isdigit()]

    return inline_valid_numbers


def remove_symbols(line:str):
    return re.findall("[0-9]+",line)[0] # CAREFUL here


def remove_symbols_for_list(lines:list,integers=True):
    results = []

    for line in lines:
        result = remove_symbols(line)
        if(integers):
            result = int(result)
        results.append(result)

    return results


def multiply_list(list):
    result = 1
    for x in list:
        result = result * x
    return result


def debug_print(values:list):
    for value in values:
        print(value)


def check_for_adjacents():
    return True


### MAIN

line = "617*.*617..."

valid_numbers = get_valid_numbers_strings(line)
valid_numbers = remove_symbols_for_list(valid_numbers)
result = multiply_list(valid_numbers)

print(result)