def solution() -> None:    
    N: int = int(input())
    houses: list[int] = list(map(int, input().split()))

    houses.sort()
    if N % 2:
        print(houses[N//2])
    else:
        print(houses[(N//2)-1])


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> int:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    case: dict[str | list[str] | str] = {
        "input": ['4', "5 1 7 9"],
        "output": "5\n",
    }
    assert case["output"] == test_example_case(input=case["input"])
    