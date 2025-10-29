import heapq


def greedy_bfs(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]  
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)
        print(f"Visiting: {node} (h={h})")

        if node == goal:
            return path  

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 3,
    'G': 0
}

start = 'A'
goal = 'G'

path = greedy_bfs(graph, start, goal, heuristic)


if path:
    print("\n Path found:", " → ".join(path))
else:
    print("\ No path found!")
