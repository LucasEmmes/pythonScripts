# Sudoku solver #

This sudoku solver will solve any solvable sudoku  
through "smart" bruteforce by using recursion  

If you would like to add your own sudoku you  
just have to make sure you follow the format of  
sudoku[row][value] as seen in sudoku_test.py  
Remember to fill gaps with 0s

I'd like to make some OCR stuff to import sudokus from  
images / webcam feed in the future, because it was fucking  
painful having to add sudokus by hand when testing this script

*NOTES*:

-   This solver does not check if the base sudoku has illegal  
      placement of values. If there are, it will probably just  
      return False. Every failed solve I have had was due  
      to me messing up when manually inputting numbers.

-   There are also no checks whether the sudoku is legal when  
      the funtion decides that it is finished solving.  
      Since the funtion CANNOT make any illegal moves by itself, it will  
      simply assume the board to be solved when all 81 values are filled in.

