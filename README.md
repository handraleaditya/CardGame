## Card Game 
Author : Aditya Handrale  
email : handraleaditya@gmail.com 

This repo is contains Card Game in python. It emulates a simple two player card game, a fun, personal project that ensures best practices and serves as a demonstration of my coding style.

#### Rules
Players draw 20 cards each from a shuffled deck of cards. The shuffled deck (Fisher-Yates algorithm) contains 1 to 10 numbered cards with 4 duplicates each (40 cards total).
Players have a draw pile and discard pile, players draw a card from the draw pile, compare it.
higher value wins and winner puts the two cards (one that belonged to them + losers card) in their discard pile. Onto the next round.
If both values are same, keep doing another round until someone wins, and winner gets all the previous cards. 
If draw pile is over, shuffle discard pile and put it into draw pile. Once one player runs out of draw pile, game ends.  

### How to run
1. Create a python virtual environment (optional)  
`python -m venv venv`
2. Activate the virtual environment using  
`./venv/Scripts/activate` (Windows)
3. Install required dependancies  
`pip install -r requirements.txt` or `pip install art`
4. Run the game using   
`python card_game.py`
5. Run the tests using
`python tests.py`  

#### Dependancies
- Python 3+
- art (https://pypi.org/project/art/)

#### Sample output

```



    __   ____  ____   ___         ____   ____  ___ ___    ___
   /  ] /    T|    \ |   \       /    T /    T|   T   T  /  _]
  /  / Y  o  ||  D  )|    \     Y   __jY  o  || _   _ | /  [_
 /  /  |     ||    / |  D  Y    |  T  ||     ||  \_/  |Y    _]
/   \_ |  _  ||    \ |     |    |  l_ ||  _  ||   |   ||   [_
\     ||  |  ||  .  Y|     |    |     ||  |  ||   |   ||     T
 \____jl__j__jl__j\_jl_____j    l___,_jl__j__jl___j___jl_____j


Copyright © 2024 Aditya Handrale

#################################
# Welcome to the Card Game! #
#################################

Please enter player 1 Name : Adi
Please enter player 2 Name : noob_player


NOOB_PLAYER [Player 1] draws a 10! [Score : 20]
ADI [Player 2] draws a 5! [Score : 20]
NOOB_PLAYER wins this round!

NOOB_PLAYER [Player 1] draws a 7! [Score : 21]
ADI [Player 2] draws a 8! [Score : 19]
ADI wins this round!

NOOB_PLAYER [Player 1] draws a 4! [Score : 20]
ADI [Player 2] draws a 2! [Score : 20]
NOOB_PLAYER wins this round!

NOOB_PLAYER [Player 1] draws a 7! [Score : 21]
ADI [Player 2] draws a 10! [Score : 19]
ADI wins this round!

NOOB_PLAYER [Player 1] draws a 1! [Score : 20]
ADI [Player 2] draws a 1! [Score : 20]
Its a tie! No winner this round
Resolving the tie...
NOOB_PLAYER [Player 1] draws a 4!
ADI [Player 2] draws a 7!
ADI [Player 2] wins the tiebreaker, and recieves the last 4 cards!


...

ADI [Player 1] draws a 4! [Score : 35]
NOOB_PLAYER [Player 2] draws a 4! [Score : 5]
Its a tie! No winner this round
Resolving the tie...
ADI [Player 1] draws a 5!
NOOB_PLAYER [Player 2] draws a 1!
ADI [Player 1] wins the tiebreaker, and recieves the last 4 cards!

ADI [Player 1] draws a 8! [Score : 37]
NOOB_PLAYER [Player 2] draws a 1! [Score : 3]
ADI wins this round!

ADI [Player 1] draws a 7! [Score : 38]
NOOB_PLAYER [Player 2] draws a 6! [Score : 2]
ADI wins this round!

ADI [Player 1] draws a 10! [Score : 39]
NOOB_PLAYER [Player 2] draws a 10! [Score : 1]
Its a tie! No winner this round
Resolving the tie...
NOOB_PLAYER [Player 2] exhausted their cards and is unable to draw any more cards, Game Over!

Final scores:
ADI Score : 39
NOOB_PLAYER Score : 1
[Player 1] ADI wins the game!


      ____   ____  __    __  ____   __
     /    T /    T|  T__T  T|    \ |  T
    Y   __jY   __j|  |  |  ||  o  )|  |
    |  T  ||  T  ||  |  |  ||   _/ |__j
    |  l_ ||  l_ |l  `  '  !|  |    __
    |     ||     | \      / |  |   |  T
    l___,_jl___,_j  \_/\_/  l__j   l__j


```
