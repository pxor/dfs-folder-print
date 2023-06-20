# Print tree like structure depending on depth
def tree_structure(depth):
    for _ in range(depth):
        print("--", end="")


# Depth First Search algo printing files
def dfs(graph, start_node):
    visited = set()
    stack = [(start_node, 0)]

    while stack:
        current_node, depth = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            tree_structure(depth)
            print(current_node)
            try:
                for n in graph[current_node]:
                    if n not in visited:
                        stack.append((n, depth + 1))
            except KeyError:
                pass
