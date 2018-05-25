
# coding: utf-8

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[12]:


from IPython.display import clear_output

def display_board(board): 
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[2]:


def player_input():
    marker = ''
    player1 = ''
    player2 = ''
    while marker not in ['X', 'O']:
        marker = input("Please pick a marker 'X' or 'O':").upper()
    if marker == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return (player1, player2)


# **TEST Step 2:** run the function to make sure it returns the desired output

# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[3]:


def place_marker(board, marker, position):
    
    board[position] = marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[4]:


def win_check(board, mark):
    
    if mark == 'X':
        if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[3] == 'X' and board[5] == 'X' and board[7] == 'X') or (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or (board[7] == 'X' and board[8] == 'X' and board[9] == 'X'):
            return True
    if mark == 'O':
        if (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[3] == 'O' and board[5] == 'O' and board[7] == 'O') or (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or (board[7] == 'O' and board[8] == 'O' and board[9] == 'O'):
            return True


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[5]:


import random

def choose_first():
    return random.randint(0,1)


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[6]:


def space_check(board, position):
    
    return board[position] == ' '


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[7]:


def full_board_check(board):
    
    for i in board:
        if i == ' ':
            return False
    return True


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[8]:


def player_choice(board):
    
    position = int(input('Please choose your next position:'))
    while (position not in range(1, 10)) or space_check(board, position) == False:
        print('The position is invalid!')
        position = int(input('Please choose your next position:'))
    return position

    
        


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[9]:


def replay():
    replay = ' '
    while replay.upper() not in ['YES', 'NO']:
          replay = input("Do you want to play again? 'Yes' or 'No'")
    return replay.upper() == 'YES'
    


# In[10]:


def game_start():
    start = input("Do you want to start the game? 'Yes' or 'No'")
    


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


print('Welcome to Tic Tac Toe!')

while replay() == True:
    first_player_mark,second_player_mark = player_input()
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    first = choose_first()
    print('The first player is {first_player_mark}'.format(first_player_mark = first_player_mark))
    display_board(board)
    game_on = True
    while game_on == True:
        position = player_choice(board)
        place_marker(board, first_player_mark, position)
        display_board(board)
        if win_check(board, first_player_mark) == True:
            print('Player1 has won the game!')
            break
        elif full_board_check(board) == True:
            print('Draw')
            break
        else:
            position = player_choice(board)
            place_marker(board, second_player_mark, position)
            display_board(board)
            if win_check(board, second_player_mark) == True:
                print('Player2 has won the game!')
                break
            elif full_board_check(board) == True:
                print('Draw')
                break 
print('Game is over!')
      


# ## Good Job!
