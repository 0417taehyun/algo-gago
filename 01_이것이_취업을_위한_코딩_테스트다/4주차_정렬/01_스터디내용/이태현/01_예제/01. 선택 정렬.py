def selection_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]

    for i in range(len(cards)):
        min_idx: int = i
        for j in range(i+1, len(cards)):
            if cards[min_idx] > cards[j]:
                min_idx = j

        cards[i], cards[min_idx] = cards[min_idx], cards[i]
    
    return cards # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    answer: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert answer == selection_sort()
    