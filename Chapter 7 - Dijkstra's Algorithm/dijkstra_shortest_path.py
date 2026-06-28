"""
Problem: Shortest Path in a Weighted Graph (Dijkstra's Algorithm)

Time Complexity : O(V²)
Space Complexity: O(V)

Author: Aryan Patel
"""
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_node = None

    for node, cost in costs.items():
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_node = node

    return lowest_node


def dijkstra(graph, start, end):
    costs = {node: float("inf") for node in graph}
    parents = {node: None for node in graph}

    for neighbor, weight in graph[start].items():
        costs[neighbor] = weight
        parents[neighbor] = start

    processed = set()

    node = find_lowest_cost_node(costs, processed)

    while node:
        current_cost = costs[node]

        for neighbor, weight in graph[node].items():
            new_cost = current_cost + weight

            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.add(node)
        node = find_lowest_cost_node(costs, processed)

    path = []
    current = end

    while current:
        path.append(current)
        current = parents[current]

    return costs[end], path[::-1]


cost, path = dijkstra(graph, "start", "fin")

print("Shortest Cost:", cost)
print("Shortest Path:", " -> ".join(path))
