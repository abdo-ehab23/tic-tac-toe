import os
def instructions():
    print('''
          Hello to tic tac toe game!
          each player in his turn will choose a number from(1:9)
          to select positin on the board.
          player 1 alwaus start first
          
          this is the table you will play on and the positions arranged like
          the layout of a phone keypad :)
          By default, player 1 goes first.
          '''
         )   
    print_table(range(1,10),0)

def print_table(lst,num):
    if num!=0 :
        os.system("clear")
        lst1 = [None]*9
        for i,item in enumerate(lst):
            if isinstance(item, int):
                lst1[i]=" "
            else:
                lst1[i]=item
    else:
        lst1=list(lst)            
    
    print ("   |     |   ")
    print (" "+str(lst1[0])+" " +"|"+"  "+str(lst1[1])+"  "+"|"+" "+str(lst1[2]))
    print ("   |     |   ")
    print("--------------")
    print ("   |     |   ")
    print (" "+str(lst1[3])+" " +"|"+"  "+str(lst1[4])+"  "+"|"+" "+str(lst1[5]))
    print ("   |     |   ")
    print("--------------")
    print ("   |     |   ")
    print (" "+str(lst1[6])+" " +"|"+"  "+str(lst1[7])+"  "+"|"+" "+str(lst1[8]))
    print ("   |     |   ")

def check_win(lst):
    if lst[0]==lst[1] and lst[1]==lst[2]:
        return True
    elif lst[3]==lst[4] and lst[4]==lst[5]:
        return True
    elif lst[6]==lst[7] and lst[7]==lst[8]:
        return True
    elif lst[0]==lst[3] and lst[3]==lst[6]:
        return True
    elif lst[1]==lst[4] and lst[4]==lst[7]:
        return True
    elif lst[2]==lst[5] and lst[5]==lst[8]:
        return True
    elif lst[0]==lst[4] and lst[4]==lst[8]:
        return True
    elif lst[2]==lst[4] and lst[4]==lst[6]:
        return True
    else :
        return False
    
def player1_turn(num):
    return num%2==0
def player_turn(num):
    if player1_turn(num):
        print("playe 1 turn")
        return 1
    else:
        print("playe 2 turn")   
        return 2 

def input_choice(choosed_lst):
    choice=int(input("Enter a number between(1,9) but be sure that the position is free!!"))
    while choice in choosed_lst:
        print("the positin is busy!! choose again!")
        choice=int(input("Enter a number between(1,9) but be sure that the position is free!!"))
    return choice

def check_draw(x):
    if x==9:
        print("the match ended in a draw!")
        return 1
    else : 
        return 0

def play_again():
    answer=input("would you like to continue playing?(y/n)")
    if answer=='y':
       return 1
    elif answer=='n':
       return 0
        

#start the program
instructions()
x=0   #this variable able us to know which player will play next
x_or_o=""
lst=[1,2,3,4,5,6,7,8,9]
choosed_lst=[]
keep_playing=1
while keep_playing:
    temp1=player_turn(x) 
    if temp1==1:
        x_or_o="x"
    elif temp1==2:
        x_or_o="o"
    temp2=input_choice(choosed_lst)-1 
    lst[temp2]=x_or_o
    x+=1
    print_table(lst,x)
    choosed_lst.append(temp2+1)
    if check_win(lst):
            if temp1==1:
                print("player 1 win!!")
            elif temp1==2:
                 print("player 2 win!!")
            keep_playing=0 #break the loop
            if play_again():
                keep_playing=1
                x_or_o=""
                lst=[1,2,3,4,5,6,7,8,9]
                choosed_lst=[]
                x=0
                print_table(range(1,10),0)
            else:
                print("end of the game :)")    
    if check_draw(x):
        keep_playing=0 #break the loop
        if play_again():
                keep_playing=1
                x_or_o=""
                lst=[1,2,3,4,5,6,7,8,9]
                choosed_lst=[]
                x=0
                print_table(range(1,10),0)
        else:
                print("end of the game :)")    
