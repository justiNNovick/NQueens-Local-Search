import random

def initialize_board(n):
    #we will initialize the board such that each column gets a queen placed in a random row
    board = []
    for i in range(n):
        board.append(-1)
    for col in range(n):  #we will preserve the structure of the output (index=column, value=row)
        board[col] = random.randint(0, n-1)
    return board

def count_conflicts_helper(board, col, row): #aiding the heuristics
    #count the number of conflicts at a given coordinates
    #will be used to help find the best place to move to and which queen should be moved in the first place 
    conflicts = 0
    for c in range(len(board)):
        if c == col: #it is assumed there is only one queen in each column so we don't have to consider
            continue
        if (board[c] == row) or (board[c] - c) == (row - col) or (board[c] + c) == (row + col): #csp rules copied
            conflicts += 1 #we will increment conflicts for each csp violation
    return conflicts

def find_most_conflicted_helper(board):
    #this function will decide which column/queen we move at each iteration
    max_conflicts = -1
    most_conflicted_cols = []
    for col in range(len(board)):
        row = board[col] #will give us the number representing how many rows down the queen is
        conflicts = count_conflicts_helper(board, col, row) 
        if conflicts == max_conflicts:  #keep track of those that are tied
            most_conflicted_cols.append(col)
        elif conflicts > max_conflicts: #in the case we find a new maximum, we scrap the old list, update the max, and start new list with new max
            max_conflicts = conflicts 
            most_conflicted_cols = [col] #must scrap old list because now we only care about what is tied with the new max
    decision = random.choice(most_conflicted_cols) #if it is a tie, pick amongst them at random
    return decision #pick at random between ties

def solve_n_queens(n, max_iterations=1000, random_restarts=50): #random restarts are bounded to make sure it won't run forever
    board = initialize_board(n)
    for i in range(max_iterations):
        column = find_most_conflicted_helper(board)
        if count_conflicts_helper(board, column, board[column]) == 0:
            return board
        min_conflicts = len(board)
        second_min_conflict = 1+len(board) #this variable will set up the option for non-greedy picking... initialized it to unrealistic value
        best_rows = []
        for row in range(len(board)): #loop employs the same logic as find_most_conflicted_helper, except we are finding the min instead
            conflicts = count_conflicts_helper(board, column, row)
            if conflicts == min_conflicts:
                best_rows.append(row)
            elif conflicts < min_conflicts:
                second_min_conflict = min_conflicts
                min_conflicts = conflicts
                best_rows = [row]
        if second_min_conflict == 1 + len(board): #condition is true if second best option was never found
            board[column] = random.choice(best_rows)
        else:
            if random.random() < 0.95:  # 95% probability we pick the most greedily attractive position
                board[column] = random.choice(best_rows)
            else:  
                board[column] = second_min_conflict #5% of the time we'll pick the second most greedily attractive position
    else:
        if random_restarts==0:
            return ["Could not find the solution"] #to make sure it doesn't run forever
        return solve_n_queens(n, max_iterations, random_restarts=random_restarts-1)  # random restart if max_iterations reached


n = int(input("Pick a value for n: "))
solution = solve_n_queens(n)
print(solution)
