def dls(node, target, depth, adj):
    if node == target:
        return True
    if depth <= 0:
        return False
    
    for child in adj[node]:
        if dls(child, target, depth - 1, adj):
            return True
    return False



adj = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

start = 1
target = 5
limit = 2  

found = dls(start, target, limit, adj)
print("Target found:", found)
