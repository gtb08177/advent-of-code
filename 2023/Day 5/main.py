
import re

class SeedToSoilEntry:
    source = 0
    dest = 0
    range = 0

    def __init__(self, source,dest,range):
        self.source = source
        self.dest = dest
        self.range = dest
 
    def maxDest(self):
        return (self.dest + self.range - 1)


def parse_input(input_text):
    # Initialize an empty dictionary to store parsed data
    data = {}
    # Variable to keep track of the current section being processed
    current_section = None

    # Iterate through each line in the input text
    for line in input_text:
        # Remove leading and trailing whitespaces from the line
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue

        # Check if the line ends with a colon (indicating a new section) that is not the first line
        if line.endswith(':'):
            # Extract the section name and convert it to lowercase
            current_section = line[:-1].lower()
            # Create an empty dictionary for the current section in the data dictionary
            data[current_section] = {}
        else:
            # Store the value of the line against the current known section
            values = list(map(int, line.split()))
            data[current_section][tuple(values[:-1])] = values[-1]

    return data


try:
    file_name = "input_test.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # pull out the seed numbers and delete from the remainder of the "file"
        first_line = lines[0]
        seeds = re.search("^seeds: (.*$)", first_line).groups()[0].split(" ")
        del lines[0]

        # search the remainder of the file for the remaining maps
        parsed_data = parse_input(lines)
        
        seed_to_soil_map = parsed_data.get('seed-to-soil map', {})
        soil_to_fertilizer_map = parsed_data.get('soil-to-fertilizer map', {})
        fertilizer_to_water_map = parsed_data.get('fertilizer-to-water map', {})
        water_to_light_map = parsed_data.get('water-to-light map', {})
        light_to_temperature_map = parsed_data.get('light-to-temperature map', {})
        temperature_to_humidity_map = parsed_data.get('temperature-to-humidity map', {})
        humidity_to_location_map = parsed_data.get('humidity-to-location map', {})

        print("seeds:", seeds)
        print("seed-to-soil map:", seed_to_soil_map)
        print("soil-to-fertilizer map:", soil_to_fertilizer_map)
        print("fertilizer-to-water map:", fertilizer_to_water_map)
        print("water-to-light map:", water_to_light_map)
        print("light-to-temperature map:", light_to_temperature_map)
        print("temperature-to-humidity map:", temperature_to_humidity_map)
        print("humidity-to-location map:", humidity_to_location_map)

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")