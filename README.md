# Sudoku Solver in Python 
This project focuses on generating valid Sodukos and solve them through recussion and the backtracking algorithm. 

![image](https://user-images.githubusercontent.com/59030389/181924543-3936e499-fbcf-4ca6-8478-c402082320e2.png)

## Description
Sudoku is a puzzle game in which missing numbers are speard throughout a 9 X 9 grid. The grid contains rows, columns, and smaller 3 X 3 grids; each of these may only contain numbers 1 - 9 with no duplications. The game is a logic based, combinational, number-placement puzzle. 

The goal for this project was to create a Sudoku board with no third-party libraries and solve it using the backtracking recursive alorithm. The application is ran through the console. 

### What is backtracking?
Backtracking is a general algorithm for solving recusrive problems. It focuses on building solutions incrementally and omitting the solutions that fail. In terms of Sudoku, the algorithm will attempt to place a number in each box one at a time, ensuring it is valid, and moving to the next box. If a number place does not work, it will recall the path it took and change to satify the conditions. 

## Getting Started
### Installing
With no thrid-party libraries it is easy to execute. Ensure Python3 is downloaded, obtain a release copy of the code and execute!

### Executing Program
Executing is simple and easy:
1. Download the release
2. Navigate to the Executable folder
3. run `Python main.py`

### Using the Program
The application focues on three main methods:
- `<Board>.print(<board>)` Prints the board to the console. Empty places are noted with a `.`.
- `<Board>.generate(<board>, <difficulty>` Generates a valid empty board. The difficulty spans from 0 - 2; 0 being easy.
- `<Board>.solve(<board>)` Solves the board using backtracking.

## Authors
Contributors' names and contact info

Gavin Abeele
[@GitHub](https://github.com/Gabeele)
[@LinkedIn](https://www.linkedin.com/in/gavinabeele/)

## Version History
* 1.0
   * See [commit change]() or See [release history]()
    * Initial Release

## License
This project is licensed under the Gavin Abeele License - see the LICENSE.MD file for details

## Acknowledgments
Inspiration, code snippets, etc.
* [Tech with Tim](https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/)
* [Kush on Medium](https://medium.com/codex/building-a-sudoku-solver-and-generator-in-python-1-3-f29d3ede6b23)
