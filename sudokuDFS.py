def build_grid(n,gz,initial):    
    grid = ['.' for i in range(n**2)]
    for tup in initial:
        row = tup[0] - 1
        col = tup[1] - 1
        index = row*n+col
        
        current = str(tup[2])
        grid[index] = current        
        
    return grid

def parse_puzzle(puzzle_string):
    return list(puzzle_string)

def build_adjacency_list(grid,n,gz):
    adjacent = {}
    for i in range(len(grid)):
        adjacent[i] = get_peers(i,n,gz)
        
    return adjacent
        
def display_grid(grid,n,gz):
    for i in range(n):
        r = []
        for j in range(i*n,i*n+n):
            if j % gz == 0 and j % n != 0:
                r.append('|')
            r.append(grid[j])
        if i % gz == 0 and i % n != 0:
            print('-'*(n*2+3))
        print(' '.join(r))
    print()

def get_peers(index,n,gz):
    row,col = divmod(index,n)
    subr = row//gz
    subc = col//gz
    subr = [subr*gz,subr*gz+gz]
    subc = [subc*gz,subc*gz+gz]       
    rc = {i for i in range(n**2) if (i%n == col or i//n == row or 
         (i//n in range(subr[0],subr[1]) and i%n in range(subc[0],subc[1])))}  
    return rc - {index}

def valid_move(grid,index,value,adjacent):
    connections = adjacent[index]    
    for peer in connections:        
        if grid[peer] == value:
            return False            
    return True

def solved(grid):
    return '.' not in grid


def get_next(grid):
    return grid.index('.')

def solve(grid,n,gz,adjacent):
    if solved(grid):
        display_grid(grid,9,3)
        return True
        
    next_square = get_next(grid)
    for k in range(1,n+1):
        value = str(k)
        if valid_move(grid,next_square,value,adjacent):
            grid[next_square] = value
            if solve(grid,n,gz,adjacent):
                return True
            else:
                grid[next_square] = '.'       
    
    return False  
        

h = parse_puzzle('.9..38...3.6..2.8.......9....96..5.41...2...'\
                            '66.2..93....4.......8.5..4.1...38..7.')

a = build_adjacency_list(h,9,3)
solve(h,9,3,a)