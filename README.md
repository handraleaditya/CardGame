## SAP coding challenge Card Game (Private Repo)
Author : Aditya Handrale  
email : handraleaditya@gmail.com 

This repo is contains the solution for SAP Programming Challenge : Card Game in python. It emulates a simple two player card game.

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


      _____  ____  ____          __   ____  ____   ___         ____   ____  ___ ___    ___
     / ___/ /    T|    \        /  ] /    T|    \ |   \       /    T /    T|   T   T  /  _]
    (   \_ Y  o  ||  o  )      /  / Y  o  ||  D  )|    \     Y   __jY  o  || _   _ | /  [_
     \__  T|     ||   _/      /  /  |     ||    / |  D  Y    |  T  ||     ||  \_/  |Y    _]
     /  \ ||  _  ||  |       /   \_ |  _  ||    \ |     |    |  l_ ||  _  ||   |   ||   [_
     \    ||  |  ||  |       \     ||  |  ||  .  Y|     |    |     ||  |  ||   |   ||     T
      \___jl__j__jl__j        \____jl__j__jl__j\_jl_____j    l___,_jl__j__jl___j___jl_____j

Copyright © 2024 Aditya Handrale


#################################
# Welcome to the SAP Card Game! #
#################################

Please enter player 1 Name : Aditya
Please enter player 2 Name : Sap_employee


ADITYA [Player 1] draws a 2! [Score : 20]
SAP_EMPLOYEE [Player 2] draws a 4! [Score : 20]
SAP_EMPLOYEE wins this round!

ADITYA [Player 1] draws a 3! [Score : 19]
SAP_EMPLOYEE [Player 2] draws a 10! [Score : 21]
SAP_EMPLOYEE wins this round!

ADITYA [Player 1] draws a 7! [Score : 18]
SAP_EMPLOYEE [Player 2] draws a 6! [Score : 22]
ADITYA wins this round!

...

ADITYA [Player 1] draws a 1! [Score : 37]
SAP_EMPLOYEE [Player 2] draws a 1! [Score : 3]
Its a tie! No winner this round
Resolving the tie...
ADITYA [Player 1] draws a 8!
SAP_EMPLOYEE [Player 2] draws a 1!
ADITYA [Player 1] wins the tiebreaker, and recieves the last 4 cards!

ADITYA [Player 1] draws a 4! [Score : 39]
SAP_EMPLOYEE [Player 2] draws a 2! [Score : 1]
ADITYA wins this round!

SAP_EMPLOYEE [Player 2] exhausted their cards and is unable to draw any more cards, Game Over!

Final scores:
ADITYA Score : 40
SAP_EMPLOYEE Score : 0
[Player 1] ADITYA wins the game!


      ____   ____  __    __  ____   __
     /    T /    T|  T__T  T|    \ |  T
    Y   __jY   __j|  |  |  ||  o  )|  |
    |  T  ||  T  ||  |  |  ||   _/ |__j
    |  l_ ||  l_ |l  `  '  !|  |    __
    |     ||     | \      / |  |   |  T
    l___,_jl___,_j  \_/\_/  l__j   l__j

```