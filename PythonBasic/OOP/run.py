import os
from card_deck.cards_answer import Card, CardDeck
from card_deck.backup import to_json


if __name__ == '__main__':
    deck = CardDeck(suits={'Hearts', 'Diamonds', 'Clubs', 'Spades'},
                    values={'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'})

    for suit in deck.suits:
        for value in deck.values:
            Card(suit=suit, value=value, deck=deck)

    deck.shuffle_deck()

    print(deck)

    players_decks = {'player_' + str(n): deck.withdraw_card(6) for n in range(1, 5)}

    for player in players_decks:
        print(player, players_decks[player])

    to_json(card_deck=deck, players=players_decks, filename=os.path.abspath('saved_decks/backup.json'))
