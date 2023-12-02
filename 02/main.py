import re
import os


class Draw:
    def __init__(self, stringed) -> None:
        self.quantity = int(re.findall(r"(\d+)", stringed)[0])
        self.type = re.findall(r"(\w+)", stringed)[1]

    def __repr__(self):
        return f"{self.quantity} {self.type}"

    def __str__(self):
        return f"{self.quantity} {self.type}"


class Game:
    def __init__(self, stringed=None) -> None:
        self.number = int(re.search(r"Game (\d+)", stringed).group(1))
        self.matches = []
        pattern = re.compile(
            r"([0-9]+\s(red|green|blue),\s)*[0-9]+\s(red|green|blue);?"
        )
        for match in pattern.finditer(stringed):
            match_string = match.group()
            match_string = match_string.replace(";", "")
            to_draw = match_string.split(",")
            single_match = []
            for draw in to_draw:
                single_match.append(Draw(draw))
            self.matches.append(single_match)

    def __repr__(self):
        return f"Game {self.number} {self.matches}"

    def __str__(self):
        return f"Game {self.number} {self.matches}"


def read_input():
    games = []
    with open(os.getcwd() + "/input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            game = Game(line)
            games.append(game)
    return games


def part1():
    games = read_input()
    items = [Draw("12 red"), Draw("13 green"), Draw("14 blue")]
    contained_items = {d.type: d for d in items}
    possible_games = []
    for i, game in enumerate(games):
        possible = True
        for match in game.matches:
            for draw in match:
                if draw.type in contained_items:
                    if draw.quantity > contained_items[draw.type].quantity:
                        possible = False
        if possible:
            possible_games.append(game.number)
    print(sum(possible_games))


def part2():
    games = read_input()
    minimums = []
    for game in games:
        game_minimum = {
            "blue": Draw("1 blue"),
            "green": Draw("1 green"),
            "red": Draw("1 red"),
        }

        for match in game.matches:
            for draw in match:
                if draw.quantity > game_minimum[draw.type].quantity:
                    game_minimum[draw.type] = draw

        minimums.append(
            game_minimum["red"].quantity
            * game_minimum["blue"].quantity
            * game_minimum["green"].quantity
        )
    print(sum(minimums))


if __name__ == "__main__":
    part1()
    part2()
