import Sudoku as sdku

b = sdku.Board

b.print(b)
b.generate(b, 2)
b.print(b)
b.solve(b)
b.print(b)