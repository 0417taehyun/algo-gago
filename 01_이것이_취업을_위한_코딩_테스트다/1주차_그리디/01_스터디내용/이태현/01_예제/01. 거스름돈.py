def solution() -> None:
    N: int = int(input())
    
    answer: int = 0
    coins: list[int] = [500, 100, 50, 10]
    for coin in coins:
        answer += (N // coin)
        N %= coin
    
    print(answer)
    


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["1260"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
            
            assert test_stdout.getvalue() == "6\n"
    
    
    test_example_case()
    