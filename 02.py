from enum import Enum, auto

from util.read_data import read_data

input = read_data("02/input.txt")

rounds = [i.split(' ') for i in  input.split('\n')]

class Turn():
    @classmethod
    def get_turn(cls, character: str) -> "Turn":
        key = {
            "A": cls.Rock,
            "B": cls.Paper,
            "C": cls.Scissors,
            "X": cls.Rock,
            "Y": cls.Paper,
            "Z": cls.Scissors
        }

        return key.get(character)

    Rock="ROCK"
    Paper="PAPER"
    Scissors="SCISSORS"


class Winner(Enum):
    Elf=auto()
    You=auto()
    Draw=auto()


class Intent(Enum):
    @classmethod
    def get_intent(cls, char:str) -> "Intent":
        key = {
            "X": cls.Lose,
            "Y": cls.Draw,
            "Z": cls.Win
        }
        return key.get(char)

    Win=auto()
    Lose=auto()
    Draw=auto()

lose_hash = {
    Turn.Rock: Turn.Scissors,
    Turn.Paper: Turn.Rock,
    Turn.Scissors: Turn.Paper
}

win_hash = {
    Turn.Rock: Turn.Paper,
    Turn.Paper: Turn.Scissors,
    Turn.Scissors: Turn.Rock
}


def get_winner_by_round(elf: Turn, you: Turn) -> Winner:
    if elf == you:
        return Winner.Draw

    elf_beats = lose_hash.get(elf)

    return Winner.Elf if elf_beats == you else Winner.You


def score_round(elf: Turn, you: Turn):
    score = 0
    initial_scores = {
        Turn.Rock: 1,
        Turn.Paper: 2,
        Turn.Scissors: 3
    }

    score += initial_scores.get(you)

    winner = get_winner_by_round(elf, you)
    
    if winner == Winner.Draw:
        score += 3
    elif winner == Winner.You:
        score += 6

    return score

turns = [
    list(map(Turn.get_turn, i))
    for i in rounds
]
scores = [score_round(*i) for i in turns]


print(f"Part 1: {sum(scores)}")


def get_turn_for_intent(elf: Turn, intent: Intent) -> Turn:
    elf_turn = Turn.get_turn(elf)
    turn_intent = Intent.get_intent(intent)
    if turn_intent == Intent.Draw:
        return elf_turn

    return win_hash.get(elf_turn) if turn_intent == Intent.Win else lose_hash.get(elf_turn)


intents = [
    [Turn.get_turn(i[0]), get_turn_for_intent(i[0], i[1])] for i in rounds
]
scores_for_part_two = sum([score_round(*i) for i in intents])

print(f"Part Two: {scores_for_part_two}")