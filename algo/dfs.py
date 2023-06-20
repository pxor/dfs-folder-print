# Print tree like structure depending on depth
def tree_structure(depth):
    for _ in range(depth):
        print("-", end="")


# Depth First Search algo printing files
def dfs(graph, start, visited, depth, path):
    visited.add(start)
    path.append(start)

    tree_structure(depth)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            try:
                dfs(graph, neighbor, visited, depth + 1, path)
            except KeyError:
                pass

            path.pop()
