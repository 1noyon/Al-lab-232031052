import heapq


def is_solvable(state):
    inv = 0
    arr = [x for x in state if x != 0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0


def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  
    x, y = divmod(idx, 3)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors


def solve_puzzle(start, goal):
    if not is_solvable(start):
        return None
    
    pq = [(0, start, [])]  
    visited = set()
    
    while pq:
        cost, state, path = heapq.heappop(pq)
        
        if state == goal:
            return path + [state]
        
        if state in visited:
            continue
        visited.add(state)
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + 1, neighbor, path + [state]))
    
    return None


start = (1, 2, 3,
         4, 0, 5,
         7, 8, 6)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = solve_puzzle(start, goal)

if solution:
    print("Steps to solve:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("Puzzle is unsolvable")
