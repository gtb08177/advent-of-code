
import re

class SourceToDestEntry:
    source = 0
    dest = 0
    range = 0

    def __init__(self,dest,source,range):
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


def get_seed_numbers_with_ranges(seed_line):
    values = list(map(int,re.search("^seeds: (.*$)", seed_line).groups()[0].split(" ")))

    generated_seeds_and_ranges = list()

    while len(values) > 0:
        range_start = values[0]
        range_length = values[1]

        generated_seeds_and_ranges.append(range(range_start,(range_start+range_length-1)))

        del values[1]
        del values[0]

    return generated_seeds_and_ranges

def find_destination_for_map(map,source):
    result = source

    for entry in map:
        if entry.isWithinSourceRange(source):
            result = entry.getTarget(source)

    return result

try:
    file_name = "input.txt"
    #file_name = "input_test.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # extract the seed number and its range length
        list_seed_numbers_with_range = get_seed_numbers_with_ranges(lines[0])
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


        lowest_running_loc = None

        # Now we've got the maps we need, loop for each seed number within a given seed starting number and range, track the lowest location value as we go
        for range in list_seed_numbers_with_range:
            for seed in range:
                target = find_destination_for_map(seed_to_soil_map, seed)
                target = find_destination_for_map(soil_to_fertilizer_map, target)
                target = find_destination_for_map(fertilizer_to_water_map, target)
                target = find_destination_for_map(water_to_light_map, target)
                target = find_destination_for_map(light_to_temperature_map, target)
                target = find_destination_for_map(temperature_to_humidity_map, target)
                target = find_destination_for_map(humidity_to_location_map, target)

                if(lowest_running_loc != None):
                    lowest_running_loc = min(lowest_running_loc,target)
                else:
                    lowest_running_loc = target

                #print("| SEED | LOWEST RUNNING LOC |")
                #print(seed,target,lowest_running_loc)

        print("RYAN")
        print(lowest_running_loc)

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")