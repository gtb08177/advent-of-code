# milliseconds + millimeters

import re

try:
    file_name = "input.txt"
    #file_name = "input_test.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        # \b word boundary, \d decimal
        regex_pattern = r'\b(\d+)\b'
        
        time_values = re.findall(regex_pattern, lines[0])
        # flip to integers for calcs later
        time_values = [int(match) for match in time_values]

        dist_values = re.findall(regex_pattern, lines[1])
        # flip to integers for calcs later
        dist_values = [int(match) for match in dist_values]    


        # PRINT STATEMENTS
        print(time_values)
        print(dist_values)

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")