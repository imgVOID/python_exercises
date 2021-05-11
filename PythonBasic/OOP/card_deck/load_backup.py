import json
from .cards_answer import Card, CardDeck


def from_json(filename):
    with open(filename) as f:
        card_deck_backup = json.load(f)

    card_deck = CardDeck(suits=card_deck_backup['suits'],
                         values=card_deck_backup['values'])
    players = dict()

    for card in card_deck_backup['cards']:
        Card(suit=card[0], value=card[1], deck=card_deck)

    for player in card_deck_backup['players']:
        players[player] = [Card(suit=card[0], value=card[1], deck=card_deck)
                           for card in card_deck_backup['players'][player]]

    return card_deck, players

