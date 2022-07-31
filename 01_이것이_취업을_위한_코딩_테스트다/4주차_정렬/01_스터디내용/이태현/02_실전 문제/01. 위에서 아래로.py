def solution() -> None:
    N: int = int(input())
    numbers: list[int] = [ int(input()) for _ in range(N) ]

    for number in sorted(numbers, reverse=True):
        print(number, end=' ')


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    

    case: dict[str, list[str] | str] = {
        "input": ['3', "15", "27", "12"],
        "output": "27 15 12 "
    }
    assert case["output"] == test_example_case(input=case["input"])
    