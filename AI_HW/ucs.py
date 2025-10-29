import heapq

def ucs(start, goal, graph):
    
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        
        if node == goal:
            return cost, path  
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    
    return float("inf"), []  



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'
cost, path = ucs(start, goal, graph)
print("Lowest cost:", cost)
print("Path:", path)
