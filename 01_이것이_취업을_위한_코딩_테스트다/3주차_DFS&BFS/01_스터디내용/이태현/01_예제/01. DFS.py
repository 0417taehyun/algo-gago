def solution() -> None:
    def dfs(
        node: int,
        visited_info: list[bool],
        stack: list[int],
        graph: list[list[int]],
    ):
        visited_info[node] = True
        stack.append(node)

        adjacent_nodes: list[int] = graph[node]
        for adjacent_node in adjacent_nodes:
            if not visited_info[adjacent_node]:
                dfs(
                    node=adjacent_node,
                    visited_info=visited_info,
                    stack=stack,
                    graph=graph,
                )


    graph: list[list[int]] = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
    ]

    stack: list[int] = []
    visited_info: list[bool] = [False] * 9
    dfs(node=1, visited_info=visited_info, stack=stack, graph=graph)

    print(stack)


if __name__ == "__main__":
    solution()