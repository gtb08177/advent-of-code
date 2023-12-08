import re
from enum import Enum

class Direction(Enum):
    LEFT= -1
    RIGHT = 1

class Node:
    me = None
    left = None
    right = None 

    def __init__(self,line):
        matches = re.findall("\w+",line)

        if(len(matches) == 3):
            self.me = matches[0]
            self.left = matches[1]
            self.right = matches[2]

    def __str__(self) -> str:
        return self.me + " = (" + self.left + ", " + self.right + ")"
    
    def __repr__(self) -> str:
        return self.__str__()


def parse_nodes(lines):
    results = dict()

    for line in lines:
        matches = re.findall("\w+",line)

        if(len(matches) == 3):
            results[matches[0]] = Node(line)

    print(*results,sep='\n')
    return results


def parse_instructions(line_instruction):
    results = list()
    matches = re.findall('[LR]',line_instruction)

    for match in matches:
        if(match == 'L'):
            results.append(Direction.LEFT)
        else:
            results.append(Direction.RIGHT) 

    #print(*results,sep='\n')
    return results

try:
    file_name = "input.txt"
    
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # Parse the original instruction line
        original_instructions = parse_instructions(lines[0])

        # Parse the nodes - assumes the second line of the file is an empty line
        list_of_nodes = parse_nodes(lines[2:])

        # Follow your instructions
        # Keep a count of how many steps you took
        # Remember to repeat through the array/list if required
        steps_required = 0
        end_node_reached = False
        end_node = list_of_nodes["ZZZ"]
        current_node = list_of_nodes["AAA"]
        
        while(not end_node_reached):
            for direction in original_instructions:
                steps_required+=1
                print("Current node is " + str(current_node))
                if direction == Direction.LEFT:
                    current_node = list_of_nodes[current_node.left]
                else:
                    current_node = list_of_nodes[current_node.right]

                if current_node.me == end_node.me:
                    end_node_reached = True
                    break

        print("Steps required :: " + str(steps_required))



except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")