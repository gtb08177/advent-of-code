from enum import Enum
from collections import Counter

class HandValue(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1
    NONE = 0

class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14

class Hand():
    cards = list()
    score = HandValue.NONE

    def __init__(self, card_string):
        self.cards = [*card_string]

class Play():
    bid = 0
    hand = None

    def __init__(self,line):
        values = line.split(" ")
        self.hand = Hand(values[0])
        self.bid = values[1]

        score_hand(self.hand)

def characters_equal(char_list, matches_needed):
    # Check if at least 'matches_needed' values in the list are equal
    return sum(char == char_list[0] for char in char_list) >= matches_needed


def check_full_house(cards):
    # if the answer is 2 then we know we had 2 values across 5 cards
    return len(Counter(cards)) == 2 


def check_two_pair(cards):
    # if the answer is 3 then we know we had 3 values across 5 cards
    return len(Counter(cards)) == 3 


def check_one_pair(cards):
    # if the answer is 4 then we know we had 4 values across 5 cards
    return len(Counter(cards)) == 4 


def score_hand(hand: Hand):
    cards = hand.cards
    # Assume HIGH_CARD until otherwise
    value = HandValue.HIGH_CARD

    if characters_equal(cards, 5):
        value = HandValue.FIVE_OF_A_KIND
    elif characters_equal(cards,4):
        value = HandValue.FOUR_OF_A_KIND
    elif check_full_house(cards):
        value = HandValue.FULL_HOUSE
    elif characters_equal(cards,3):
        value = HandValue.THREE_OF_A_KIND
    elif check_two_pair(cards):
        value = HandValue.TWO_PAIR
    elif check_one_pair(cards,2):
        value = HandValue.ONE_PAIR

    hand.score = value


def compare_cards(card_list_one, card_list_two, index=0):
    # Base case, if we have compared all the cards and we reach here, something is wrong.
    if index == len(card_list_one) or index == len(card_list_two):
        return None
    
    if card_list_one[index] > card_list_two[index]:
        return True
    elif card_list_two[index] > card_list_one[index]:
        return False
    else:
        return compare_cards(card_list_one,card_list_two,index+1)


def parse(lines):
    all_hands = []
    for line in lines:
        all_hands.append(Hand(line))
        

# you get a list of hands
# your goal is to order the hands in terms of strength
# a hand consists for five cards

try:
    file_name = "input.txt"
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        all_hands = []

        for line in lines:
            play = Play(line)
            all_hands.append(play)




        print(len(all_hands))

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")