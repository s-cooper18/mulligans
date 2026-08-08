import random

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
        return "\n".join(
            [f"({i + 1}) {self._cards[i]}" for i in range(len(self._cards))]
        )

    def has_serum_powder(self) -> bool:
        return any(card.name for card in self._cards if card.name == "Serum Powder")

    def return_card(self, position: int) -> Card:
        return self._cards.pop(position - 1)

    def __len__(self) -> int:
        return len(self._cards)


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
        return self.draw_cards(STANDARD_HAND_SIZE)

    def serum_powder(
        self, cards_to_exile: list[Card], cards_to_bottom: list[Card] | None = None
    ) -> Hand:
        num_cards_to_draw = len(cards_to_exile)
        self.exiled.extend(cards_to_exile)
        if cards_to_bottom:
            self.cards.extend(cards_to_bottom)
        return self.draw_cards(num_cards_to_draw)

    def __len__(self) -> int:
        return len(self.cards)

    def get_num_exiled(self) -> int:
        return len(self.exiled)
