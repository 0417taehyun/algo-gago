def solution() -> None:
    from collections import deque
    
    
    def bfs(
        node: int,
        visited_info: list[int],
        queue: list[int],
        result: list[int],
        graph: list[list[int]],
    ) -> None:
        visited_info[node] = True
        while queue:
            current_node: int = queue.popleft()         
            result.append(current_node)
            for adjacent_node in graph[current_node]:
                if not visited_info[adjacent_node]:
                    queue.append(adjacent_node)
                    visited_info[adjacent_node] = True
                
        
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
    visited_info: list[bool] = [False] * 9
    result: list[int] = []
    queue: deque = deque([1])
    
    bfs(
        node=1,
        visited_info=visited_info,
        queue=queue,
        result=result,
        graph=graph
    )
    print(result)
    

if __name__ == "__main__":
    solution()
    