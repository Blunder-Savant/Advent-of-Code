#!/usr/bin/env python3
from pathlib import Path

CARD_STRENGTH = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

def camel_card_sorter(hand):
    cards = {"J": 0}
    value = 0

    for card in hand[0]:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1

    # Find and replace wildcard cards
    wildcards = cards.pop("J")
    if wildcards == 5:
        cards = {"A": 5}
    else:
        best_cards = [card for card, num in cards.items() if num == max(cards.values())]
        best_cards = sorted(best_cards, key=lambda card: CARD_STRENGTH[card])
        cards[best_cards[-1]] += wildcards

    # Five of a kind
    if [num for num in cards.values() if num == 5]:
        value += (len(CARD_STRENGTH) ** 6) * 6
    # Four of a kind
    elif [num for num in cards.values() if num == 4]:
        value += (len(CARD_STRENGTH) ** 6) * 5
    # Full house
    elif [num for num in cards.values() if num == 3] and [num for num in cards.values() if num == 2]:
        value += (len(CARD_STRENGTH) ** 6) * 4
    # Three of a kind
    elif [num for num in cards.values() if num == 3]:
        value += (len(CARD_STRENGTH) ** 6) * 3
    # Two pair
    elif len([num for num in cards.values() if num == 2]) == 2:
        value += (len(CARD_STRENGTH) ** 6) * 2
    # One pair
    elif [num for num in cards.values() if num == 2]:
        value += (len(CARD_STRENGTH) ** 6) * 1
    # Value each card from left to right (max value == 399,854 + 30,758 + 2,366 + 182 + 14)
    for val, card in enumerate(reversed(hand[0])):
        value += CARD_STRENGTH[card] * (len(CARD_STRENGTH) ** val)

    return value


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    camel_cards = file.read().split("\n")

hands = [(camel_card.split()[0], int(camel_card.split()[1])) for camel_card in camel_cards]
ranked_hands = sorted(hands, key=camel_card_sorter)

total_winnings = sum((rank + 1) * hand[1] for rank, hand in enumerate(ranked_hands))
print(total_winnings)