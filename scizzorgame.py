#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import getpass
player_1_name=input('Player 1. Give me Your name: ')
player_2_name=input('Player 2. Give me Your name: ')
while True:
    #Each player choose an item hidden by getpass
    
    player1=getpass.getpass("%s, Please set the number: n. Nozyczki p. Papier k. Kamien. Twój wybór to : " % player_1_name).lower()
    player2=getpass.getpass("%s, Please set the number: n. Nozyczki p. Papier k. Kamien. Twój wybór to : " % player_2_name).lower()
    
    #Create a tuple from results
    choice = (player1,player2)
    
    #Defining winnig choices list of tuples for player1 and player2
    win_player_1=[('p','k'),('k','n'), ('n','p')]
    win_player_2=[('k','p'),('n','k'), ('p','n')]
    
    #Definig draw situation list of tuples from player input
    draw=[('k','k'), ('p','p'), ('n','n')]
    
    #Printing player's choice to the board
    print(choice)
    
    #Checking the winner
    if choice in win_player_1:
        print(player_1_name + ' is a winer')
        continue
    elif choice in win_player_2:
        print(player_2_name + ' is a winer')
        continue
    elif choice in draw:
        print('DRAW, make Your choice again')
        continue
    else:
        print('INVALID INPUT')
        break

