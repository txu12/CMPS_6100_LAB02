"""
CMPS 6100  Lab 2
Author: Tiancheng.Xu
"""
import random
print("Game Start")
f = open("Space Station.txt","rt")
content = f.readlines()
Room_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Map = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Monster = random.choice(Room_list)
Portkey = random.choice(Room_list)

Room_dict = {0:[1,2,3,4],
             1:[0,5],
             2:[0,6],
             3:[0,7],
             4:[0,8],
             5:[1,13,14],
             6:[2],
             7:[3,15,16],
             8:[4],
             9:[13],
             10:[14],
             11:[15],
             12:[16],
             13:[5,9],
             14:[5,10],
             15:[7,11],
             16:[7,12]}

def player_move(num):
    print(content[num + 2])
    print("Rooms adjacent to the current room are: ")
    print(Room_dict.get(num))
    while True:
        try:
            next_room = int(input("Choose the next room you want to explore: "))
            if next_room in Room_dict.get(num):
                return next_room
            else:
                print("You cannot go there now, please choose again: ")
        except ValueError:
            print("Invalid input, please enter a valid number.")           
    
def monster_move(num):
    next_move = random.choice(Room_dict.get(num))   
    return next_move 

player_initial = player_move(0)
monster_initial = Monster

while True:
    player_initial = player_move(player_initial)
    monster_initial = monster_move(monster_initial)
    if player_initial == Portkey and player_initial != monster_initial:
        print("You find the portkey which teleports you away to a safe place, you win.")
        break
    elif player_initial == monster_initial:
        print("You are cought by the monster, you lose.")
        break
         
f.close