def solution() -> None:
    N: int = int(input())
    plan: list[str] = list(input().split())
    
    start: list[int] = [1, 1]
    for move in plan:
        if move == 'R':
            if start[1] == N:
                pass
            else:
                start[1] += 1
        
        elif move == 'L':
            if start[1] == 1:
                pass
            else:
                start[1] -= 1
        
        elif move == 'U':
            if start[0] == 1:
                pass
            else:
                start[0] -= 1
        
        elif move == 'D':
            if start[0] == N:
                pass
            else:
                start[0] += 1
    
    print(" ".join([ str(point) for point in start ]))


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["5", "R R R U D D"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "3 4\n"
    
    
    test_example_case()
    