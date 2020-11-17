def deck_of_cards():
    return [a + b for a in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king'] for b in [' of hearts', ' of spades', ' of diamonds', ' of clubs']]


deck = deck_of_cards()
assert len(deck) == 52, "Your deck should have 52 cards"
