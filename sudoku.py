# -*- coding: utf-8 -*-

n = 4

class Grid:
    def __init__(self,n,grid_size,initial_set):
        self.grid = [[0 for i in range(n+1)] for j in range(n+1)]
        self.valid = [[[x for x in range(1,n+1)] for i in range(n+1)] for j in range(n+1)]
        self.grid_size = grid_size
        for tup in initial_set:
            self.grid[tup[0]][tup[1]] = tup[2]
            
        for row in range(n+1):
            for col in range(n+1):
                if row == 0 or col == 0:
                    self.valid[row][col] = []
                if self.grid[row][col] != 0:
                    self.valid[row][col] = []
                    current = self.grid[row][col]
                    for i in range(1,n+1):
                        if current in self.valid[row][i]:
                            self.valid[row][i].remove(current)
                        if current in self.valid[i][col]:
                            self.valid[i][col].remove(current)
                    
                    sub = self.subgrid(row,col)
                    for r in sub[0]:
                        for c in sub[1]:
                            if current in self.valid[r][c]:
                                self.valid[r][c].remove(current)                                
                                                    
                    
    def display_grid(self):
        for row in range(1,n+1):
            r = []
            
            for col in range(1,n+1):
                r.append(self.grid[row][col])
                if col % self.grid_size == 0 and col != n:
                    r.append('|')
            print(' '.join([str(x) for x in r]))
            if row % self.grid_size == 0 and row != n:
                print('-'*(2*n+1))
    
    def subgrid(self,row,col):
        row = (row-1)//self.grid_size
        col = (col-1)//self.grid_size
        grid_rows = [i for i in range((row+1)*2,(row+1)*2-self.grid_size,-1)]
        grid_cols = [i for i in range((col+1)*2,(col+1)*2-self.grid_size,-1)]
        
        return [grid_rows, grid_cols]
                
        
    def display_valid(self):
        for row in range(1,n+1):
            r = []
            
            for col in range(1,n+1):
                r.append(self.valid[row][col])
                if col % self.grid_size == 0 and col != n:
                    r.append('|')
            print(' '.join([str(x) for x in r]))
            if row % self.grid_size == 0 and row != n:
                print('-'*(2*n+1))
    
    def solve(self):
        solved = False
        flags = 0
        while not solved and flags < 100:
            for row in range(1,n+1):
                for col in range(1,n+1):
                    if len(self.valid[row][col]) == 1:
                        value = self.valid[row][col][0]
                        self.grid[row][col] = value
                        self.update_valid(row,col,value)
                        
            checkgrid = [[self.grid[i][j] for j in range(1,n+1)] for i in range(1,n+1)]
            solved = True
            for row in checkgrid:
                if 0 in row:
                    solved = False
                    
            flags += 1 #caps number of iterations
                        
    def update_valid(self,row,col,current):
        for i in range(1,n+1):
            if current in self.valid[row][i]:
                self.valid[row][i].remove(current)
            if current in self.valid[i][col]:
                self.valid[i][col].remove(current)
                
        sub = self.subgrid(row,col)
        for r in sub[0]:
            for c in sub[1]:
                if current in self.valid[r][c]:
                    self.valid[r][c].remove(current)
                    



