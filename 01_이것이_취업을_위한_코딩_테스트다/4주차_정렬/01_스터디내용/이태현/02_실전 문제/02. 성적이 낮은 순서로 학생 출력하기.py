def solution() -> None:
    N: int = int(input())
    students: dict[str, int] = {}
    for _ in range(N):
        name, score = input().split()
        students[name] = int(score)

    for name, _ in sorted(students.items(), key=lambda x: x[1]):
        print(name, end=' ')


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    

    case: dict[str, list[str] | str] = {
        "input": ['2', "홍길동 95", "이순신 77"],
        "output": "이순신 홍길동 "
    }
    assert case["output"] == test_example_case(input=case["input"])
    