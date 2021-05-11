from card_deck.load_backup import from_json
import os

if __name__ == '__main__':
    card_deck, players = from_json(os.path.abspath('saved_decks/backup.json'))
    print(card_deck)
    for player in players:
        print(player, players[player])
