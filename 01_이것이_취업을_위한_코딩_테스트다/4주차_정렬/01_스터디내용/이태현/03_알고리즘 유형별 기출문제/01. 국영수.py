def solution() -> None:
    N: int = int(input())

    students: dict[str, list[int]] = {}
    for _ in range(N):
        name, korean, enlgish, math = input().split()
        students[name] = [int(korean), int(enlgish), int(math)]
    
    students = sorted(
        students.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0])
    )
    for name, _ in students:
        print(name)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    solution()
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str]] = {
        "input": [
            "12", "Junkyu 50 60 100", "Sangkeun 80 60 50",
            "Sunyoung 80 70 100", "Soong 50 60 90", "Haebin 50 60 100",
            "Kangsoo 60 80 100", "Donghyuk 80 60 100", "Sei 70 70 70",
            "Wonseob 70 70 90", "Sanghyun 70 70 80", "nsj 80 80 80",
            "Taewhan 50 60 90"
        ],
        "output": [
            "Donghyuk", "Sangkeun", "Sunyoung", "nsj", "Wonseob", "Sanghyun",
            "Sei", "Kangsoo", "Haebin", "Junkyu", "Soong", "Taewhan"
        ]
    }
    output: str = "\n".join(case["output"])
    assert f"{output}\n" == test_example_case(input=case["input"])
    