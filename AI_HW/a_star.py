import heapq


def a_star(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [start])]  
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        print(f"Visiting: {node} (g={g}, h={heuristic[node]}, f={f})")

        if node == goal:
            return g, path  

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))

    return float("inf"), []  


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}


start = 'A'
goal = 'F'

total_cost, path = a_star(graph, start, goal, heuristic)


print("\nPath   found:", " → ".join(path))
print("Total Cost:", total_cost)
