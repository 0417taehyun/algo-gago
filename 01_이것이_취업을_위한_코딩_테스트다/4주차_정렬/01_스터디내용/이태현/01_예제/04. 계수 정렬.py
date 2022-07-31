def count_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]

    count: list[0] = [ 0 for _ in range(max(cards) + 1) ]
    for card in cards:
        count[card] += 1

    return [ card for card, count in enumerate(count) if count > 0 ] # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    answer: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert answer == count_sort()
    