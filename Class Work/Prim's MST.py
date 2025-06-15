import heapq

def primsMST(graph, V):
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, vertex)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight

        # Add the edge to MST (except for starting vertex)
        if weight != 0:
            mst_edges.append((u, weight))

        for v, wt in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (wt, v))

    return total_cost, mst_edges

# Example usage
if __name__ == "__main__":
    V = 5  # Number of vertices
    # Adjacency list (u -> [(v, weight)])
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8)],
        4: [(1, 5), (2, 7)]
    }

    cost, edges = primsMST(graph, V)
    print("Total cost of MST:", cost)
    print("Edges in MST:")
    for u, w in edges:
        print(f"Vertex: {u}, Edge weight: {w}")
