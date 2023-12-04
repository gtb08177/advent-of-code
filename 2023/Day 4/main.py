
import re
from collections import Counter

def calc_score(number_of_matches):
    if number_of_matches == 0: return 0

    score = 1

    for x in range (1,number_of_matches):
        score = score * 2

    return score

input = open(r"input.txt","r")
games = input.readlines()
running_score = 0

for game in games: 
    regex_groups = re.search("^[Cc]ard +[0-9]+: +(([0-9]+ +)+)\| +(([0-9]+ +)+[0-9]+)", game).groups()
    winning_numbers = Counter(regex_groups[0].split(" "))
    game_numbers = Counter(regex_groups[2].split(" "))
    
    # Find what values are shared
    common_numbers = winning_numbers & game_numbers
    common_numbers_list = [value for value in common_numbers.elements() if value and value.strip()]
    
    game_score = calc_score(len(common_numbers_list))
    running_score = running_score + game_score
    # print(winning_numbers)
    # print(game_numbers)
    # print(common_numbers)
    # print(calc_score(len(common_numbers_list)))
    # print()

print(running_score)