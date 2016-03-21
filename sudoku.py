# -*- coding: utf-8 -*-

class Grid:
    def __init__(self,n,grid_size,initial_set):
        self.grid = [[0 for i in range(n+1)] for j in range(n+1)]
        self.valid = [[[x for x in range(1,n+1)] for i in range(n+1)] for j in range(n+1)]
        self.grid_size = grid_size
        self.size = n
        
        for tup in initial_set:
            self.grid[tup[0]][tup[1]] = tup[2]
            
        for row in range(n+1):
            for col in range(n+1):
                if row == 0 or col == 0:
                    self.valid[row][col] = []
                if self.grid[row][col] != 0:
                    self.valid[row][col] = []
                    current = self.grid[row][col]
                    self.update_valid(row,col,current)                               
                                                  
    def display_grid(self):
        n = self.size
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
        size = self.grid_size
        row = (row-1)//size
        col = (col-1)//size       
        
        return [(row+1)*size-size+1,(row+1)*size+1,(col+1)*size-size+1,(col+1)*size+1]              
        
    def display_valid(self):
        n = self.size
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
        n = self.size
        checkgrid_prev = checkgrid = None
        while not solved and flags < 100:
            self.naked_single()            
                       
            checkgrid = [[self.grid[i][j] for j in range(1,n+1)] for i in range(1,n+1)]
            if checkgrid_prev == checkgrid:
                print("Can't be solved...") #can't be solved with current methods
                break
            checkgrid_prev = checkgrid            

            if self.check_solution():
                solved = True
                    
            flags += 1 #caps number of iterations
            
        if not solved:
            print("Wasn't solved in allowed iterations")
            
    def naked_single(self):
        n = self.size
        for row in range(1,n+1):
            for col in range(1,n+1):
                if len(self.valid[row][col]) == 1:
                    value = self.valid[row][col][0]
                    self.grid[row][col] = value
                    self.update_valid(row,col,value)
                        
    def update_valid(self,row,col,current):
        n = self.size
        for i in range(1,n+1):
            if current in self.valid[row][i]:
                self.valid[row][i].remove(current)
            if current in self.valid[i][col]:
                self.valid[i][col].remove(current)
                
        sub = self.subgrid(row,col)
         
        for r in range(sub[0],sub[1]):
            for c in range(sub[2],sub[3]):
                if current in self.valid[r][c]:
                   self.valid[r][c].remove(current)
    
    def check_solution(self):
        gz = self.grid_size
        n = self.size
        
        #check rows for uniqueness
        for row in range(1,n+1):
            if len(self.grid[row]) != len(set(self.grid[row])):                
                return False
        #check columns
        for i in range(1,n+1):
            col = [r[i] for r in self.grid]
            if len(col) != len(set(col)):                
                return False
        #check subgrids
        for r in range(1,n,gz):
            for c in range(1,n,gz):
                subgrid = [self.grid[i][r:r+gz] for i in range(c,c+gz)]                
                subgrid = [num for row in subgrid for num in row]
                print(subgrid)
                if len(subgrid) != len(set(subgrid)):                    
                    return False        
        return True
        
initial = {(1,1,1),(3,1,2),(2,4,5),(3,4,3),(2,7,7),(3,7,8),(3,8,5),(2,9,1),
           (3,9,9),(6,2,7),(5,3,8),(4,4,2),(4,5,3),(6,5,6),(6,6,4),(5,7,9),
           (4,8,7),(7,1,8),(8,1,3),(7,2,1),(7,3,6),(8,3,4),(7,6,3),(8,6,6),
           (7,9,4),(9,9,3)} 
                   
g = Grid(9,3,initial)


