def count_paths(i, j, grid, H, W, memo):
    if j == W - 1:
        return 1 if i == 0 or i == H - 1 else 0

    if (i, j) in memo:
        return memo[(i, j)]

    total_paths = 0

    if j + 1 < W:
        total_paths += count_paths(i, j + 1, grid, H, W, memo)

    for c in range(j + 1, W):
        for r in range(H):
            if c == j + 1 and r == i:
                continue
            if grid[r][c] == grid[i][j]:
                total_paths += count_paths(r, c, grid, H, W, memo)

    memo[(i, j)] = total_paths
    return total_paths

def find_all_paths(grid):
    H = len(grid)
    W = len(grid[0])
    memo = {}
    total_paths = 0

    for i in range(H):
        total_paths += count_paths(i, 0, grid, H, W, memo)

    return total_paths

if __name__ == '__main__':
    with open("ijones.in", "r", encoding="utf-8") as f:
        content = f.read().split()
    W = int(content[0])
    H = int(content[1])
    grid = []
    index = 2
    for _ in range(H):
        grid.append(list(content[index]))
        index += 1

    result = find_all_paths(grid)

    with open("ijones.out", "w", encoding="utf-8") as f:
        f.write(str(result) + "\n")