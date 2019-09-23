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

    def validate(self, p):
        if p < 0 or p > self.count:
            raise Exception('not valid')
    
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


class Percolation:
    def __init__(self, n):
        self.grid = n*n
        self.n = n
        self.matrix = WeightedQuickUnionUF(n*n)
        self.flows = []

    def __str__(self):
        return str(self.matrix)
    
    def flowing(self, newSite, oldSite):
        for flow in self.flows:
                if oldSite in flow:
                    flow.append(newSite)

    # opens the site (row, col) if it is not open already
    def open(self, row, col):
        self.matrix.validate(row)
        self.matrix.validate(col)

        site = row*self.n + col

        #connect south
        if site + self.n < self.n*self.n:
            southSite= site + self.n
            if not self.matrix.connected(site, southSite) and row != self.n-1:
                self.matrix.union(site, southSite)
            self.flowing(site, southSite)

        #connect north
        if row != 0:
            northSite = site - self.n
            if not self.matrix.connected(site, northSite) and row != 0:
                self.matrix.union(site, northSite)
            self.flowing(site, northSite)

        #connect east
        if site + self.n < self.n*self.n and col != self.n-1:
            eastSite = site + 1
            if not self.matrix.connected(site, eastSite):
                self.matrix.union(site, eastSite)
            self.flowing(site, eastSite)

        #connect west
        if col != 0:
            westSite = site - 1
            if not self.matrix.connected(site, westSite):
                self.matrix.union(site, westSite)
            self.flowing(site, westSite)

        if site > 0 and site < self.n:
            newFlow = [site]
            self.flows.append(newFlow)

        
    # # is the site (row, col) open?
    def isOpen(self, row, col) -> bool:
        self.matrix.validate(row)
        self.matrix.validate(col)

        site = row*self.n + col

        #check south
        if self.matrix.connected(site, site + self.n) and row != self.n-1:
            return  True
        #check north
        if self.matrix.connected(site, site - self.n) and row != 0:
            return  True
        #check east
        if self.matrix.connected(site, site + 1) and col != self.n-1:
            return  True
        #check west
        if self.matrix.connected(site, site - 1) and col != 0:
            return  True


    # is the site (row, col) full?
    def isFull(self, row, col) -> bool:
        self.matrix.validate(row)
        self.matrix.validate(col)

        site = row*self.n + col

        for flow in self.flows:
            for flowSite in flow:
                if site == flowSite:
                    return True
        return False
        
        
    # # returns the number of open sites
    def numberOfOpenSites(self):
        counter = 0
        
        for row in range(self.n-1):
            for col in range(self.n-1):
                if self.isOpen(row, col):
                    counter += 1
        return counter

    # does the system percolate?
    def percolates(self):
        #check if any sites on the bottom row are full
        for col in range(self.n):
            if self.isFull(self.n-1, col):
                return True
        return False

perc = Percolation(5)

perc.open(0, 4)
perc.open(1, 4)
perc.open(2, 4)
perc.open(3, 4)
perc.open(4, 4)

print(perc.percolates())