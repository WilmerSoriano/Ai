
Name: Wilmer Soriano
ID: 1001885481

Python verison 3.10.12

Strucuture of the Code:
   NOTE: 
   * My code is not design for all error checking. My code will assume user will:
         - input the correct variables as argument(<num-red> <num-blue> <version> <first-player>)
         - input the correct amount to remove (either 1 or 2 marbels)
         - input the correct color (red or blue)
      If any incorrecet input was take, please restart the game. Program assume user know how to play.

   1 Library:
   * sys library is used only to handle arguments

   2 Global variables:
   * MAX and MIN will serve as Infinite for MinMax

   7 functions + 1 main:
   * Main:
      will handle user arguments and determine if user/computer goes first.
   *settingUp:
      will display the setting for nim_game and launch the game with desire version of the game (1 for misere and
      0 for standard version)
   *nim_game:
      will remain in the loop until conditions are met, it'll switch between human and computer,
      If human will go to human function otherwise go to computer, generate possible moves and go to
      computer function.
      If condition-loop, are met go to endGame function
   *humanTurn:
      will display a mini interface for player and ask question about the move they'll like to take
      once all question have been answer, return the number of marbel (for red and blue) and next player
      turn to play (which nim_game function will handle)
   *possibleMoves:
      will handle and check if the number of marbel is allowed to be take.(eg. Pick 2 red marbels,
      pick 2 blue marbels, pick 1 red marbel, pick 1 blue marbel) and return those 4 possible option.
   *computerTurn:
      display a boarder for the user to see the next part (which indicates computer turn). (4 option were already
      generated before entering the function)
      Enters the for-loop to determine the best outcome out of the 4 possibles moves. Inside the loop, determine
      which color goes first and prepare to send to MinMax_AlphaBeta function to return result outcome.
      Once it return, compare the result outcome and see if it better or worst to previous result.
      Once exiting the for-loop, update computer best choice with current game and display computer choice, with
      end statement and return number of marbel and human turn next.
   *MinMax_AlphaBeta:
      will first and always check if terminal condition has been met, if it has, return the total score, determine if
      the game is standard or misere version and return based on if its good for computer or bad move for computer.
      If not terminal then generate all 4 possible moves for this option. Check if its MAX or MIN Turn.
      If MAX turn then set up the best as -infinite and enter a loop to see the best outcome for this option. 
      Peform the MinMax and Alpha-Beta Prunning. Recurse itself, this time switching between True or False for Min
      or Max player. Once hit the terminal end, return the score, and (if Max or Min) evaluate if its the best option 
      , save the best option as Alpha and prune as needed. (Vise versa for Min). Keeps going until all option have hit
      terminal which will return back to computerTurn function and evaluate best option of the 4.
   *endGame:
      If the game ends (meaning the while-loop has hit zero for either red or blue), display the result
      based on the game version and also display who has won with loser gaining or losing points.

How to run:
   NOTE: Code will run ACS Omega!

   *Go to directory containing this file: red_blue_nim.py

   *On Linux terminal: python3 red_blue_nim.py <num-red> <num-blue> <version> <first-player> 
      -Where:
         <num-red> <num-blue> is any number of your choice for both
         <version> can either be left blank, standard or misere
         <first-player> can either be left blank, human, or computer

   *On window terminal: python red_blue_nim.py <num-red> <num-blue> <version> <first-player>
      -Where:
         <num-red> <num-blue> is any number of your choice for both
         <version> can either be left blank, standard or misere
         <first-player> can either be left blank, human, or computer

   (*Same concept on Omega)

   Example on Window Terminal (Where I leave [version] and [player] blank):

   C:\Users\example> python red_blue_nim.py 10 8

   |===============================|
   | Setting up your Nim-Game...   |
   | Pile: 10 marbel and 8 marbel. |
   | Version: standard             |
   | First turn: computer          |
   |===============================|

   ...etc...