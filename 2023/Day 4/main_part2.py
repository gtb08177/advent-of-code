
import re
from collections import Counter


def number_of_matches(regex_groups):
    winning_numbers = Counter(regex_groups[0].split(" "))
    game_numbers = Counter(regex_groups[2].split(" "))
    common_numbers = winning_numbers & game_numbers
    common_numbers_list = [value for value in common_numbers.elements() if value and value.strip()]
    return len(common_numbers_list)


input = open(r"input_test.txt","r")
games = input.readlines()

scratch_cards_remaining = 1
scratch_cards_played = 0

for game in games:
    
    # if we have no scratch cards left, kill this loop and print the answer
    if scratch_cards_remaining == -1: break

    # account for this scratch card
    scratch_cards_remaining -= 1

    regex_groups = re.search("^[Cc]ard +[0-9]+: +(([0-9]+ +)+)\| +(([0-9]+ +)+[0-9]+)", game).groups()
    num_of_matches = number_of_matches(regex_groups)

    print("scratch_cards_remaining :: " + str(scratch_cards_remaining))
    print("scratch_cards_played :: " + str(scratch_cards_played))

    print("Number of matches :: " + str(num_of_matches))

    scratch_cards_remaining += scratch_cards_remaining + num_of_matches
    scratch_cards_played += 1

    print("scratch_cards_remaining :: " + str(scratch_cards_remaining))
    print("scratch_cards_played :: " + str(scratch_cards_played))
    print()

print(scratch_cards_played)