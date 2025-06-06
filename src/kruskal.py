class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


def kruskal(edges, n):
    uf = UnionFind(n)
    edges.sort()
    mst_weight = 0

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight

    return mst_weight


def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    matrix = []
    for line in lines:
        matrix.append(list(map(int, line.strip().split(','))))

    return matrix


if __name__ == "__main__":
    matrix = read_matrix("islands.csv")
    n = len(matrix)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], i, j))

    min_length = kruskal(edges, n)
    print(f"Мінімальна довжина підводних кабелів: {min_length}")