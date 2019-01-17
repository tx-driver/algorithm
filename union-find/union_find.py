from collections import deque

class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in [0]*size]
    
    def find(self, x):
        stack = deque()

        while not self.table[x] in [-1, -2]:
            stack.append(x)
            x = self.table[x]

        for node in stack:
            self.table[node] = x

        return x

    def union(self, x, y):
        if self.table[y] <= self.table[x]:
            self.table[x] = y


if __name__ == '__main__':
    h, w = map(int, input().split())
    table = [list(input().rstrip()) for _ in [0]*w]

    uf = UnionFind(h*w)

    # Search table
    delta = [[1, 0], [0, 1]]
    for x in range(h):
        for y in range(w):
            if table[x][y] == '.':
                uf.table[x*w + y] = -2
                continue
            for dx, dy in delta:
                if 0 <= x + dx < h and 0 <= y + dy < w:
                    if table[x][y] == table[x+dx][y+dy]:
                        uf.union(x*w + y, (x+dx)*w + y + dy)
    
    print(uf.table)

    # Find and compress path
    for i in range(h*w):
        uf.find(i)
    
    print(uf.table)