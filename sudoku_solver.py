import json

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    # Check if 'num' is already in the current row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check if 'num' is already in the current column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if 'num' is in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Undo the move (backtrack)

    return False

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def main():
    # Example Sudoku puzzle (0 means empty cell)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Here's the Sudoku puzzle:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nHere's the solved Sudoku puzzle:")
        print_grid(grid)
    else:
        print("Oops! No solution exists.")

if __name__ == "__main__":
    main()
