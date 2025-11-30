def add_edge(graph, u, v, bidirectional=True):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    if bidirectional:
        graph[v].append(u)


def dfs(graph, current, goal, visited, path):
    visited.add(current)
    path.append(current)

    if current == goal:
        return True

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, path):
                return True

    path.pop()
    return False


def main():
    print("=== DFS Path Finder ===")
    graph = {}

    n_edges = int(input("Enter number of edges: "))
    print("Enter edges in the format: u v")

    for _ in range(n_edges):
        u, v = input().split()
        add_edge(graph, u, v)

    print("\nGraph:")
    for node, nbrs in graph.items():
        print(f"{node}: {nbrs}")

    start = input("\nEnter start node: ").strip()
    goal = input("Enter goal node: ").strip()

    visited = set()
    path = []

    if start not in graph or goal not in graph:
        print("Start or goal node does not exist in graph.")
        return

    found = dfs(graph, start, goal, visited, path)

    if found:
        print("\nPath found using DFS:")
        print(" -> ".join(path))
    else:
        print(f"\nNo path found from {start} to {goal}.")


main()