import random
from collections.abc import Collection

import attrs

STANDARD_HAND_SIZE = 7


@attrs.frozen
class Card:
    name: str = attrs.field()

    def __str__(self) -> str:
        return self.name


@attrs.frozen
class Hand:
    _cards: list[Card] = attrs.field()

    def format_as_str(self) -> str:
        return "\n".join([card.name for card in self._cards])

    def format_choices(self) -> str:
        return "\n".join([f"({i + 1}) {self._cards[i]}" for i in range(len(self._cards))])

    def has_serum_powder(self) -> bool:
        return any(card.name for card in self._cards if card.name == "Serum Powder")

    def return_card(self, position: int) -> Card:
        return self._cards.pop(position - 1)

    def __len__(self) -> int:
        return len(self._cards)

    def get_card(self, which: int) -> Card:
        assert which in range(len(self._cards))
        return self._cards[which]


@attrs.define
class Deck:
    cards: list[Card] = attrs.field(factory=list)
    exiled: list[Card] = attrs.field(factory=list)

    def add_cards(self, cards: list[Card]) -> None:
        self.cards.extend(cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_cards(self, num_cards: int) -> Hand:
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return Hand(hand)

    def mulligan(self, hand: list[Card]) -> Hand:
        self.cards.extend(hand)
        self.shuffle()
        return self.draw_cards(STANDARD_HAND_SIZE)

    def serum_powder(self, hand: Hand, items_to_bottom: set[int] | None = None) -> Hand:
        possible_indices = set(range(len(hand)))

        if not items_to_bottom:
            self.exile_cards(hand._cards)
            return self.draw_cards(7)

        # are all valid choices
        assert items_to_bottom.intersection(possible_indices) == items_to_bottom

        cards_to_exile = (
            {hand.get_card(i) for i in possible_indices.difference(items_to_bottom)}
            if items_to_bottom
            else hand._cards
        )

        cards_to_bottom = {hand.get_card(i) for i in items_to_bottom}
        self.return_cards(cards_to_bottom)

        self.exile_cards(cards_to_exile)

        return self.draw_cards(len(cards_to_exile))

    def __len__(self) -> int:
        return len(self.cards)

    def get_num_exiled(self) -> int:
        return len(self.exiled)

    def return_cards(self, cards: set[Card]) -> None:
        cards_to_return = list(cards)
        random.shuffle(cards_to_return)
        self.cards.extend(cards_to_return)

    def exile_cards(self, cards: Collection[Card]) -> None:
        self.exiled.extend(cards)
