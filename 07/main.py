import functools
import os
from pprint import pprint

cards = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]

cards_part2 = [
    "J",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "Q",
    "K",
    "A",
]


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        hands = f.read().splitlines()
        hands = {hand.split()[0]: int(hand.split()[1]) for hand in hands}
    return hands


def get_hand_result(hand):
    short_hand = set(hand)
    if len(short_hand) == 1:
        return "five"
    elif len(short_hand) == 2:
        count = sorted([hand.count(k) for k in cards if hand.count(k) > 0])
        if len(count) == 0:
            print(hand)
            input()
        if count[-1] == 4:
            return "four"
        else:
            return "full"
    elif len(short_hand) == 3:
        count = sorted([hand.count(k) for k in cards if hand.count(k) > 0])
        if count[-1] == 3:
            return "three"
        elif count[-1] == 2:
            return "two"
    elif len(short_hand) == 4:
        return "one"
    return "high"


def get_hand_result_2(hand):
    short_hand = set(hand)
    if len(short_hand) == 2:
        count = {k: hand.count(k) for k in cards_part2 if hand.count(k) > 0}
        if "J" in count:
            return "five"

    elif len(short_hand) == 3:
        count = {k: hand.count(k) for k in cards_part2 if hand.count(k) > 0}
        if "J" in count:
            if count["J"] in [2, 3]:
                return "four"
            elif count["J"] == 1:
                values = sorted(count.values(), reverse=True)
                if values[0] == 3:
                    return "four"
                elif values[0] == 2:
                    return "full"
    elif len(short_hand) == 4:
        count = {k: hand.count(k) for k in cards_part2 if hand.count(k) > 0}
        if "J" in count:
            return "three"
    elif len(short_hand) == 5:
        if "J" in hand:
            return "one"

    return get_hand_result(hand)


def compare_results(left, right):
    lr = get_hand_result(left)
    rr = get_hand_result(right)
    results = ["high", "one", "two", "three", "full", "four", "five"]
    if results.index(lr) > results.index(rr):
        return 1
    if results.index(lr) < results.index(rr):
        return -1
    if left == right == "high":
        lh = get_hand_high(left)
        rh = get_hand_high(right)
        if lh > rh:
            return 1
        if lh < rh:
            return -1
    return compare_characters(left, right)


def compare_results_2(left, right):
    lr = get_hand_result_2(left)
    rr = get_hand_result_2(right)
    results = ["high", "one", "two", "three", "full", "four", "five"]
    if results.index(lr) > results.index(rr):
        return 1
    if results.index(lr) < results.index(rr):
        return -1
    if left == right == "high":
        lh = get_hand_high_2(left)
        rh = get_hand_high_2(right)
        if lh > rh:
            return 1
        if lh < rh:
            return -1
    return compare_characters_2(left, right)


def compare_characters(left, right):
    for i in range(len(left)):
        if cards.index(left[i]) > cards.index(right[i]):
            return 1
        if cards.index(left[i]) < cards.index(right[i]):
            return -1
    return 0


def compare_characters_2(left, right):
    for i in range(len(left)):
        if cards_part2.index(left[i]) > cards_part2.index(right[i]):
            return 1
        if cards_part2.index(left[i]) < cards_part2.index(right[i]):
            return -1
    return 0


def get_hand_high(hand):
    high = 0
    for card in hand:
        if cards.index(card) > high:
            high = cards.index(card)
    return high


def get_hand_high_2(hand):
    high = 0
    for card in hand:
        if cards_part2.index(card) > high:
            high = cards_part2.index(card)
    return high


def part1():
    hands = read_input()
    sorted_hands = sorted(hands.keys(), key=functools.cmp_to_key(compare_results))
    total = 0
    for i, hand in enumerate(sorted_hands):
        total += hands[hand] * (i + 1)
    print(total)


def part2():
    hands = read_input()
    sorted_hands = sorted(hands.keys(), key=functools.cmp_to_key(compare_results_2))
    total = 0
    for i, hand in enumerate(sorted_hands):
        total += hands[hand] * (i + 1)
    print(total)


if __name__ == "__main__":
    part1()
    part2()
