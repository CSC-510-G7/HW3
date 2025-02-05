"""This module contains an implementation of DFS to detect a cycle in a directed graph."""

def _dfs(node, graph, visited):
    """Helper function to perform a depth-first search on a component in the graph."""
    if node in visited:
        return True
    visited.add(node)

    for neighbor in graph[node]:
        if _dfs(neighbor, graph, visited):
            return True

    return False


def has_cycle(graph):
    """Returns True if the graph has a cycle, False otherwise."""
    # Initialize the set of visited nodes.
    visited = set()
    # Iterate over all nodes in the graph.
    for node in graph:
        # If the node has not been visited, call the DFS helper function.
        if node not in visited:
            if _dfs(node, graph, visited):
                return True
    return False


if __name__ == "__main__":
    print(has_cycle({0: [1], 1: [0]}) is True)
    print(has_cycle({0: [1], 1: [2], 2: [0]}) is True)
    print(has_cycle({0: [1], 1: [2], 2: []}) is False)
    print(has_cycle({0: [1], 1: [2], 2: [3], 3: [1]}) is True)
    print(has_cycle({0: [1], 1: [2], 2: [3], 3: []}) is False)
    print(has_cycle({0: [1], 1: [2], 2: [3], 3: [4], 4: [2]}) is True)
    print(has_cycle({0: [1], 1: [2], 2: [3], 3: [4], 4: []}) is False)
    print(has_cycle({0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: [3]}) is True)
    print(has_cycle({0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: []}) is False)
