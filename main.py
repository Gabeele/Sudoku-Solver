import Sudoku as sdku

b = sdku.Board  # Creates a board object

b.print(b)     
b.generate(b, 2)    # Generates a board with a higest difficulty
b.print(b)
b.solve(b)          # Solves the board
b.print(b)