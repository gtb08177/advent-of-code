
import re

class SourceToDestEntry:
    source = 0
    dest = 0
    range = 0

    def __init__(self, dest,source,range):
        self.dest = dest
        self.source = source
        self.range = range
 
    def getTarget(self,number):
        return (number - self.source) + self.dest
    
    def isWithinSourceRange(self,number):
        return self.source <= number < self.source + self.range
    
    def __str__(self):
        return "source=" + str(self.source) + "|dest=" + str(self.dest) + "|range=" + str(self.range)

    def __repr__(self) -> str:
        return self.__str__()


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
            data[current_section] = []
        else:
            # Store the value of the line against the current known section
            values = list(map(int, line.split()))
            dest = values[0]
            source = values[1]
            range = values[2]

            current = SourceToDestEntry(dest,source,range)
            data[current_section].append(current)

    return data

def get_seed_numbers(lines):
    first_line = lines[0]
    return list(map(int,re.search("^seeds: (.*$)", first_line).groups()[0].split(" ")))

def find_destination_for_map(map,source):
    result = source

    for entry in map:
        if entry.isWithinSourceRange(source):
            result = entry.getTarget(source)

    return result

try:
    file_name = "input.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # pull out the seed numbers and delete from the remainder of the "file"
        seeds = get_seed_numbers(lines)
        # delete the `seed` line from lines
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

        lowest_running_loc = -1
        for seed in seeds:
            source = find_destination_for_map(seed_to_soil_map, seed)
            source = find_destination_for_map(soil_to_fertilizer_map, source)
            source = find_destination_for_map(fertilizer_to_water_map, source)
            source = find_destination_for_map(water_to_light_map, source)
            source = find_destination_for_map(light_to_temperature_map, source)
            source = find_destination_for_map(temperature_to_humidity_map, source)
            source = find_destination_for_map(humidity_to_location_map, source)

            if(lowest_running_loc == -1):
                lowest_running_loc = source
            else:
                lowest_running_loc = min(lowest_running_loc,source)
    
        print(lowest_running_loc)
    

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")