#!/opt/homebrew/bin/python3.12
import os
import random
import re
from pathlib import Path

DATFILES = (Path(__file__) / '..' / 'datfiles').resolve()


def _get_files():
    files = os.listdir(DATFILES)
    return [DATFILES / file for file in files]


def card():
    paths = _get_files()
    cards = []
    for path in paths:
        with open(path, 'r') as f:
            text = re.split(r'[\n|\r\n]%[\n|\r\n]', f.read())
        text = [cards for cards in text if cards.strip('\n\r')]
        cards += text
    return random.sample(cards, k=3)


print("Past:",  (card()[0]), "Reversed:", random.choice([True, False]), end="\n")
print("Present:",  (card()[0]), "Reversed:", random.choice([True, False]), end="\n")
print("Future:",  (card()[0]), "Reversed:", random.choice([True, False]), end="\n")
