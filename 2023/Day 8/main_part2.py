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

    return results


def parse_instructions(line_instruction):
    results = list()
    matches = re.findall('[LR]',line_instruction)

    for match in matches:
        if(match == 'L'):
            results.append(Direction.LEFT)
        else:
            results.append(Direction.RIGHT) 

    return results


def find_nodes_ending_in(dict_of_nodes,ending_in_char):
    results = list()

    for node in dict_of_nodes:
        if node.endswith(ending_in_char):
            results.append(dict_of_nodes[node])

    return results

def find_path(start_node,end_node,dict_of_nodes,list_of_directions):
    end_node_reached = False
    steps_required = 0
    current_node = start_node

    while(not end_node_reached):
        for direction in list_of_directions:
            steps_required+=1

            if direction == Direction.LEFT:
                current_node = dict_of_nodes[current_node.left]
            else:
                current_node = dict_of_nodes[current_node.right]

            if current_node == end_node:
                end_node_reached = True
                break

    return steps_required

def all_end_with_z(list_of_where_am_i_nodes, list_of_end_nodes):
    counter = 0

    for node in list_of_where_am_i_nodes:
        if node in list_of_end_nodes:
            counter+=1

    return len(list_of_where_am_i_nodes) == counter

try:
    file_name = "input.txt"
    
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # Parse the file
        directions = parse_instructions(lines[0])
        dict_of_nodes = parse_nodes(lines[2:])

        # Split into starting nodes and end nodes
        list_of_starting_nodes = find_nodes_ending_in(dict_of_nodes,'A')
        list_of_end_nodes = find_nodes_ending_in(dict_of_nodes,'Z')

        steps_required = 0
        end_state_reached = False
        where_am_i_now_list = list_of_starting_nodes.copy()

        while (not end_state_reached):
            for direction in directions:
                where_am_i_going_list = []

                for current_node in where_am_i_now_list:

                    if direction == Direction.LEFT:
                        where_am_i_going_list.append(dict_of_nodes[current_node.left])
                    else:
                        where_am_i_going_list.append(dict_of_nodes[current_node.right])

                where_am_i_now_list = where_am_i_going_list
                steps_required+=1

                # Have I reached all Zs?
                if all_end_with_z(where_am_i_now_list,list_of_end_nodes):
                    end_state_reached = True
                    break

        print("Steps required :: " + str(steps_required))



except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")