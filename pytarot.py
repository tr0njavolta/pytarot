#!/opt/homebrew/bin/python3.12
#!/opt/homebrew/bin/python3.12
import os
import random
import json
from pathlib import Path

DATFILE = (Path(__file__) / '..' / 'cards.json').resolve()

def get_cards():
    with open(DATFILE, 'r') as f:
        data = json.load(f)
    return data['cards']

def card():
    cards = get_cards()
    return random.choice(cards)

for position in ["Past", "Present", "Future"]:
    selected_card = card()
    is_reversed = random.choice([True, False])
    meaning = selected_card['meaning_rev'] if is_reversed else selected_card['meaning_up']
    print(f"{position}: {selected_card['name']}")
    print(f"Reversed: {is_reversed}")
    print(f"Meaning: {meaning}")
    print()  # Print an empty line for separation
