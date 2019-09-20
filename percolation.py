class QuickFind:
    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]
    def __str__(self):
        return f"Count: {self.count} matrix: {self.id}"

    def counts(self):
        return self.count

    def find(self, p):
        self.validate(p)
        return self.id[p]
    
    def validate(self, p):
        if p < 0 or p > self.count:
            raise Exception('not valid')
    
    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.find(p) == self.find(q)


    def union( self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        
        for index in self.id:
            if self.id[index] == pID:
                self.id[index] = qID
        self.count -= 1

class WeightedQuickUnionUF:
    def __init__(self, n):
        self.count = n
        self.parent = [x for x in range(n)]
        self.size = [1 for x in range(n)]
    def __str__(self):
        return f"Count: {self.count} parents: {self.parent} size: {self.size}"

    def find(self, p):
        while (p != self.parent[p]):
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return
        
        #weighted union, making smaller root point to the larger one
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]

        self.count -= 1


test = WeightedQuickUnionUF(10)

print(test)
test.union(2, 6)
test.union(7, 4)
test.union(5, 7)
test.union(6, 9)
print(test)

# class Percolation:
#     def __init__(self, n):
#         self.n = n
#         self.grid = [[[False] for x in range(1, n+1)] for y in range(1, n+1)]
#     def __str__(self):
#         return str(self.grid)
    
#     # # opens the site (row, col) if it is not open already
#     def open(self, row, col):
#         #connect south
#         if self.grid[row+1][col] and not connected(self.grid[row+1][col], self.grid[row][col]):
#             union(self.grid[row+1][col], self.grid[row][col])
#         #connect north
#         if self.grid[row-1][col] and not connected(self.grid[row-1][col], self.grid[row][col]):
#             union(self.grid[row-1][col], self.grid[row][col])
#         #connect east
#         if self.grid[row][col+1] and not connected(self.grid[row][col+1], self.grid[row][col]):
#             union(self.grid[row][col+1], self.grid[row][col])
#         #connect west
#         if self.grid[row][col-1] and not connected(self.grid[row][col-1], self.grid[row][col]):
#             union(self.grid[row][col-1], self.grid[row][col])

        
#     # # is the site (row, col) open?
#     def isOpen(self, row, col):
#         if self.grid[row][col] == True:
#             return True
#         else:
#             return False

#     # # is the site (row, col) full?
#     # def isFull(self, row, col):
        
#     # # returns the number of open sites
#     def numberOfOpenSites(self):
#         count = 0
#         for row in range(self.n):
#             for col in range(self.n):
#                 if self.grid[row][col] == True:
#                     count += 1

#         return count

#     # # does the system percolate?
#     # def percolates()

# perc = Percolation(10)

# perc.open(4,2)

# print(perc.numberOfOpenSites())
# print(perc)