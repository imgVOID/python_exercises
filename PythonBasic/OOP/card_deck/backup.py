import os
from sys import argv
import json


def to_json(card_deck, players, filename):
    with open(filename, 'w') as f:
        deck = {'suits': list(card_deck.suits),
                'values': list(card_deck.values),
                'cards': [(card.suit, card.value) for card in card_deck.cards],
                'players': dict()}
        for player in players:
            deck['players'].update({player: [(card.suit, card.value) for card in players[player]]})
        json.dump(deck, f)

