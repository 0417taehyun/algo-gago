def solution() -> None:
    N: int = int(input())
     
    hour_count: int = 0
    for time in range(N + 1):
        if '3' in str(time):
            hour_count += 1
            
    others_count: int = 0
    for time in range(60):
        if '3' in str(time):
            others_count += 1
    
    second_count: int = others_count * 60 * (N + 1)
    minute_count: int = others_count * 60 * (N + 1)
    total_hour_count = hour_count * 60 * 60
    
    second_minutue_dupliacated = (N + 1) * others_count * others_count
    second_hour_dulicated = hour_count * 60 * others_count
    minute_hour_duplicate = hour_count * others_count * 60
    second_minute_hour_duplicated = hour_count * others_count * others_count
    
    answer = (
        total_hour_count + \
            minute_count + \
                second_count
    ) - (
        second_minutue_dupliacated + \
            second_hour_dulicated + \
                minute_hour_duplicate
    ) + second_minute_hour_duplicated
    
    print(answer)
    
    
def other_solution() -> None:
    N: int = int(input())
    
    answer: int = 0
    for hour in range(N + 1):
        for minute in range(60):
            for second in range(60):
                if '3' in str(hour) + str(minute) + str(second):
                    answer += 1
                    
    print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["5"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "11475\n"
    
    
    test_example_case()
    