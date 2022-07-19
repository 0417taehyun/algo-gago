def solution() -> None:
    N: int = int(input())
    cards: list[int] = [ int(input()) for _ in range(N) ]
    
    cards.sort()
    answer = cards.pop(0)    
    
    while cards:
        answer += cards.pop(0)
        cards.append(answer)
        cards.sort()
        
    
        


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    solution()
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ['3', "10", "20", "40"],
        "output": "100\n",
    }
    assert case["output"] == test_example_case(input=case["input"])
    