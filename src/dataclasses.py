import attrs
import random

STANDARD_HAND_SIZE = 7

@attrs.frozen
class Card:
    name: str = attrs.field()
    
@attrs.define
class Deck:
    _cards: list[Card] = attrs.field(factory=list)
    _exiled: list[Card] = attrs.field(factory=list)
    
        
    def add_cards(self, cards: list[Card]) -> None:
        self._cards.extend(cards)
    
    def shuffle(self) -> None:
        random.shuffle(self._cards)
    
    def draw_cards(self, num_cards: int) -> list[Card]:
        hand = self._cards[:num_cards]
        self._cards = self._cards[num_cards:]
        return hand

    def mulligan(self, hand: list[Card]) -> list[Card]:
        self._cards.extend(hand)
        return self.draw_cards(STANDARD_HAND_SIZE)
    
    def serum_powder(self, cards_to_exile: list[Card], cards_to_bottom: list[Card] | None = None) -> list[Card]:
        num_cards_to_draw = len(cards_to_exile)
        
        self._exiled.extend(cards_to_exile)
        
        if cards_to_bottom:
            self._cards.extend(cards_to_bottom)
        
        return self.draw_cards(num_cards_to_draw)
    
    def __len__(self) -> int:
        return len(self._cards)
        
        