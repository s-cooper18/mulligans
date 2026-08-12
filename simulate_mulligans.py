from collections.abc import Callable

from src import dataclasses, deck_loader

HAND_SIZE = 7


def choose_cards_to_return(
    hand: dataclasses.Hand, mulligans: int, print_func: Callable
) -> set[int]:
    chosen = set()
    if mulligans == 0:
        return chosen

    num_cards_can_keep = len(hand) - mulligans
    value = input(f"Choose {mulligans} card(s) to put back:")

    while len(chosen) > num_cards_can_keep:
        try:
            this_index = int(value)
            chosen.add(this_index)
        except ValueError, IndexError:
            print_func("Invalid value\n")
            continue
    return chosen


def run_mulligans(deck: dataclasses.Deck, print_func: Callable) -> None:
    mulligans = 0
    hand = deck.draw_cards(7)

    while True:
        print_func(hand.format_choices())
        print_func(
            f"\nHave taken {mulligans} mulligans(s), {deck.get_num_exiled()} card(s) in exile, {len(deck.cards)} in deck\n"
        )
        value = input(
            f"{'Serum (s), ' if hand.has_serum_powder() else ''}Mulligan (m) or Keep (k):"
        )

        if value not in ("s", "m", "k"):
            print_func("Invalid input\n")
            continue

        match value:
            case "s":
                cards_to_return = choose_cards_to_return(hand, mulligans, print)
                hand = deck.serum_powder(hand, cards_to_return)
                print_func(f"Exiled {len(hand._cards)} cards\n")
            case "m":
                hand = deck.mulligan(hand._cards)
                mulligans += 1
                print_func("Mulligan\n")
            case "k":
                cards_to_return = choose_cards_to_return(hand, mulligans, print)
                print_func(
                    f"Kept hand after {mulligans} mulligans with {deck.get_num_exiled()} cards in exile.\n"
                )
                break
            case _:
                continue


if __name__ == "__main__":
    filepath = "tests/sample_data/decklist.txt"
    deck = deck_loader.parse_decklist(filepath)

    run_mulligans(deck, print_func=print)
