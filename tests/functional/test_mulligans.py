from src import dataclasses


def create_sample_deck() -> dataclasses.Deck:
    return dataclasses.Deck(
        cards=[dataclasses.Card(name=f"card {i}") for i in range(60)]
    )


def test_simple_path() -> None:
    deck = create_sample_deck()

    assert len(deck) == 60
    hand = deck.draw_cards(7)

    assert len(hand) == 7
    assert len(deck) == 53

    for _ in range(10):
        hand = deck.mulligan(hand._cards)
        assert len(hand) == 7
        assert len(deck) == 53


def test_serum_powder() -> None:
    deck = create_sample_deck()

    assert len(deck) == 60
    hand = deck.draw_cards(7)

    assert len(hand) == 7
    assert len(deck) == 53

    hand = deck.serum_powder(hand._cards)
    assert len(hand) == 7
    assert len(deck) == 46

    hand = deck.serum_powder(hand._cards)
    assert len(hand) == 7
    assert len(deck) == 39


def test_serum_powder_after_mulligan() -> None:
    deck = create_sample_deck()

    assert len(deck) == 60
    hand = deck.draw_cards(7)

    assert len(hand) == 7
    assert len(deck) == 53

    bottom = hand._cards[0]
    exile = hand._cards[1:]

    hand = deck.serum_powder(cards_to_exile=exile, cards_to_bottom=[bottom])
    assert len(hand) == 6

    assert deck.cards[-1] == bottom

    assert deck.get_num_exiled() == 6
    assert len(deck) == 48
