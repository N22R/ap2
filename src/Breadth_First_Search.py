from collections import deque


def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    start = tuple(map(int, lines[0].strip().split(',')))
    end = tuple(map(int, lines[1].strip().split(',')))
    dimensions = tuple(map(int, lines[2].strip().split(',')))
    matrix = [list(map(int, line.strip().split())) for line in lines[3:]]
    return start, end, dimensions, matrix


def matrix_to_graph(matrix):
    graph = {}
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                neighbors = []
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 1:
                        neighbors.append((ni, nj))
                graph[(i, j)] = neighbors
    return graph


def bfs_shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return -1

    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)

    while queue:
        current, dist = queue.popleft()
        if current == end:
            return dist

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1


def main():
    input_file = "input.txt"
    start, end, dimensions, matrix = read_input(input_file)
    graph = matrix_to_graph(matrix)
    shortest_path = bfs_shortest_path(graph, start, end)

    output_file = "output.txt"
    with open(output_file, 'w') as file:
        file.write(str(shortest_path))


if __name__ == "__main__":
    main()