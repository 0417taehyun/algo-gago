def quick_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]


    return cards # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    answer: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert answer == quick_sort()
    