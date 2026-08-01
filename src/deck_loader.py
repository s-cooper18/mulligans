import mtg_parser

from src import dataclasses

DECK_SIZE = 60


class InvalidDeck(Exception):
    def __str__(self) -> str:
        return "Invalid deck"


def parse_decklist(filename: str) -> dataclasses.Deck:

    with open(filename) as f:
        lines = f.read()

    deck = dataclasses.Deck()

    deck_iterator = mtg_parser.parse_deck(lines)

    if deck_iterator is None:
        raise InvalidDeck()

    for unique_card in deck_iterator:
        deck.add_cards(unique_card.quantity * [dataclasses.Card(name=unique_card.name)])
        if len(deck) >= DECK_SIZE:
            break

    deck.shuffle()

    return deck
