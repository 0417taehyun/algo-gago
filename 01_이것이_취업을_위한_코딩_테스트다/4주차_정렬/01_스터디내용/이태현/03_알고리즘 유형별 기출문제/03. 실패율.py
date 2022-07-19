def solution(N: int, stages: list[int]) -> list[int]:
    total_users: int = len(stages)
    failures: dict[int, int] = { stage: 0 for stage in range(1, N+1) }

    stages.sort()
    if not stages[0] > N:
        count: int = 0
        previous_stage: int = stages[0]

        for stage in stages:
            if stage > N:
                break

            elif stage == previous_stage:
                count += 1

            else:
                failures[previous_stage] = count / total_users

                previous_stage = stage
                total_users -= count
                count = 1

        failures[previous_stage] = count / total_users

    answer = [
        stage for stage, failure
        in sorted(failures.items(), key=lambda x: (-x[1], x[0]))
    ]

    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int | list[int]]] | list[int]] = [
        {
            "input": {"N": 5, "stages": [2, 1, 2, 6, 2, 4, 3, 3]},
            "output": [3, 4, 2, 1, 5],
        },
        {
            "input": {"N": 4, "stages": [4, 4, 4, 4, 4]},
            "output": [4, 1, 2, 3],
        },
        {
            "input": {"N": 1, "stages": [2]},
            "output": [1],
        }                
    ]
    for case in cases:
        assert case["output"] == solution(
            N=case["input"]["N"], stages=case["input"]["stages"]
        )
