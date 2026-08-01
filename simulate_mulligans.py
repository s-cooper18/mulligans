from src import dataclasses, deck_loader

HAND_SIZE = 7


def maybe_return_cards(hand: dataclasses.Hand, mulligans: int) -> None:
    num_cards_can_keep = HAND_SIZE - mulligans
    while len(hand) > num_cards_can_keep:
        value = input("Choose card to put back:")
        try:
            option = int(value)
            card_to_return = hand.return_card(option)
        except ValueError, IndexError:
            print("Invalid value\n")
            continue

        print(f"Returned {card_to_return}")


if __name__ == "__main__":
    filepath = "tests/sample_data/decklist.txt"

    deck = deck_loader.parse_decklist(filepath)
    mulligans = 0

    hand = deck.draw_cards(7)

    while True:
        print(hand.format_choices())
        print(
            f"\nHave taken {mulligans} mulligans(s), {deck.get_num_exiled()} card(s) in exile\n"
        )
        value = input(
            f"{'Serum (s), ' if hand.has_serum_powder() else ''}Mulligan (m) or Keep (k):"
        )

        if value not in ("s", "m", "k"):
            print("Invalid input\n")
            continue

        match value:
            case "s":
                hand = deck.serum_powder(hand._cards)
                maybe_return_cards(hand, mulligans)
                print(f"Exiled {len(hand._cards)} cards\n")
            case "m":
                hand = deck.mulligan(hand._cards)
                mulligans += 1
                print("Mulligan\n")
            case "k":
                maybe_return_cards(hand, mulligans)

                print(
                    f"Kept hand after {mulligans} mulligans with {deck.get_num_exiled()} cards in exile.\n"
                )
                break
            case _:
                continue
