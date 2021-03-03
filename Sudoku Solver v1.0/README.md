# Sudoku solver #

This sudoku solver will solve any solvable sudoku
through "smart" bruteforce by using recursion

*Small notes*:

-   This solver does not check if the base sudoku has illegal
      placement of values. If there are, it will probably just
      return False. Every failed solve I have had was due
      to me messing up the input.

-   There are also no checks whether the sudoku is legal when
      the funtion decides that it is finished solving.
      Since the funtion CANNOT make any illegal moves by itself, it will
      simply assume the board to be solved when all 81 values are filled in.

-   The solve() funtion will both print out and return
      the solved sudoku when finished. Pick whichever you like best
      and simply remove the other one

-   Oh yeah: There's probably a whole lot of room for optimization.

If you would like to add your own sudoku you
just have to make sure you follow the format of
sudoku[row][value] as seen in the top of the code.
Remember to fill gaps with 0s

Im prob gonna make some OCR stuff to import sudokus from
images / webcam feed in the future because it was fucking
painful adding every sudoku by hand when testing this script
