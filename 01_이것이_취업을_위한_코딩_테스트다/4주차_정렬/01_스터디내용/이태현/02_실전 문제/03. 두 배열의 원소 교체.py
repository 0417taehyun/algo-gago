def solution() -> None:
    N, K = map(int, input().split())
    A: list[int] = list(map(int, input().split()))
    B: list[int] = list(map(int, input().split()))

    answer: int = 0
    for a_num, b_num in zip(sorted(A), sorted(B, reverse=True)):
        if K > 0:
            if a_num < b_num:
                answer += b_num
            
            else:
                answer += a_num
        
            K -= 1
        
        else:
            answer += a_num

    print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    

    case: dict[str, list[str] | str] = {
        "input": ["5 3", "1 2 5 4 3", "5 5 6 6 5"],
        "output": "26\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    