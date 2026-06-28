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


costs = {
    "a": 6,
    "b": 2,
    "fin": float("inf")
}

parents = {
    "start": None,
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []

node = find_lowest_cost_node(costs, processed)

while node:
    cost = costs[node]

    for neighbor, weight in graph[node].items():
        new_cost = cost + weight

        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node

    processed.append(node)
    node = find_lowest_cost_node(costs, processed)

path = []
current = "fin"

while current:
    path.append(current)
    current = parents[current]

path.reverse()

print("Shortest Cost:", costs["fin"])
print("Shortest Path:", " -> ".join(path))
