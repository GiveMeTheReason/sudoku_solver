# sudoku_solver
Script for solving sudoku (9x9, 16x16)

1. Launch python script
2. Enter the desk size (9 or 16)
3. Enter the initial desk
4. Get the solution (if there is one to exist)

Script outputs relatevly if there are more that one solution,
or solution does not exist.

Example input for initial 9x9 desk:
53--7----
6--195---
-98----6-
8---6---3
4--8-3--1
7---2---6
-6----28-
---419--5
----8--79

Where "-" means the empty cell. May be used any other symbol
instead of "-", except those which are used for desk filling.

The symbol set used to fill the 9x9 desk:
"123456789"

The symbol set used to fill the 16x16 desk:
"123456789ABCDEFG"
