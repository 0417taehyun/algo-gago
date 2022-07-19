def insertion_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]

    for i in range(1, len(cards)):
        for j in range(i, 0, -1):
            if cards[j] < cards[j-1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]

            else:
                break

    return cards # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    answer: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert answer == insertion_sort()
    