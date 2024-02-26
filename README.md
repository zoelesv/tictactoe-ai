# Tic-tac-toe
| ![Image 1](/src/play.png) | ![Image 2](/src/ai.png) |
|:---------------------:|:---------------------:|
## About
This app implements an AI using Minimax algorithm to play Tic-Tac-Toe optimally with an user.

## Files
- tictactoe.py - all of the logic for playing the game, and for making optimal moves
- runner.py - pygame graphical interface

## Instruction
```pip install -r requirements.txt```


```python runner.py```

## Specifications:
- S₀: Initial state (in our case, an empty 3X3 board)
- Players(s): a function that, given a state s, returns which player’s turn it is (X or O).
- Actions(s): a function that, given a state s, return all the legal moves in this state (what spots are free on the board).
- Result(s, a): a function that, given a state s and action a, returns a new state. This is the board that resulted from performing the action a on state s (making a move in the game).
- Terminal(s): a function that, given a state s, checks whether this is the last step in the game, i.e. if someone won or there is a tie. Returns True if the game has ended, False otherwise.
- Utility(s): a function that, given a terminal state s, returns the utility value of the state: -1, 0, or 1.
- Minimax function: using minimax algorith to search for the best optimal moves
    ![Image 4](/src/state.png)
    - Minimax represents winning conditions as (-1) for one side and (+1) for the other side
    ![Image 3](/src/minmax.png)
    - Given a state s, the function considers all the possible values of Future States
        - MAX picks action a in ACTIONS(s) that produces highest value of MIN-VALUE(RESULT(s, a))
        - MIN picks action a in ACTIONS(s) that produces smallest value of MAX-VALUE(RESULT(s, a))
