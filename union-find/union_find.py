class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in [0]*size]
    
    def find(self, x):
        while self.table[x] is not -1:
            x = self.table[x]
        return x

    def union(self, x, y):
        if self.table[y] <= self.table[x]:
            self.table[x] = y

if __name__ == '__main__':
    uf = UnionFind(10)
    print(uf.find(1))
    print(uf.table)
    uf.union(1, 2)
    print(uf.find(1))
    print(uf.table)