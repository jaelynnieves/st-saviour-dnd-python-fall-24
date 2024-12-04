import time
import random 
from tav import Tav
from draw import draw_d20, draw_d4, draw_d6

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    name =   input('Name: ')
    role =   input('Role: ')
  
    print('NEW YORK STRUGGLES')
    player = Tav(name, role)
    player.print_character_sheet()

print_dramatic_text('Adventure starts in New York City ') 
  
r = random.randint(1,6)  
draw_d6(r)

if r == 1 or r ==2 or r ==3:
    pigeon = '\U0001F426' 
    print(' You are on your way to work ')
    print(pigeon + ' when a pigeon flies down toward you and attacks you ')
    print('roll required: 6')
    roll = random.randint(1,20)
    draw_d20(roll)
    
    roll = random.randint(1,20)
    if roll == 6:
        print_dramatic_text("WINNER")
        print_dramatic_text("YOU MAY GO ON")
    else:
        print_dramatic_text("FAIL!! BOOOOOO")
    
if r == 4 or r == 5: 
    rat = '\U0001F400'
    print('as you are waiting for the train ')
    print(rat + ' a rat runs towards you ')
    print('roll requires: 11')
    roll = random.randint(1,20)
    draw_d20(roll)

   
    print_dramatic_text("Would you like some help? y/n?")
    choice = input('Choice: ') 
    if choice == "yes": 
        draw_d20(roll)
        
    if roll == 11:
        print_dramatic_text("WINNER")
        print_dramatic_text("You may go on")
    else:
        print_dramatic_text("FAIL!! RAT WINS!!")
        print_dramatic_text("YOU 0 Rat 1") 
    
if r == 6:
    man = '\U0001F468'
    print('as you are walking down the block')
    print(man + ' a homeless man appears!')
    print_dramatic_text( " THIS IS THE BIGGEST, THE MEANEST, THE HARDEST OPPONENT EVER")
    print('roll required: 18')
    roll = random.randint(1,20)
    draw_d20(roll)
        
    print_dramatic_text("Would you like some help? y/n?")
    choice = input('Choice: ')
    roll= random.randint(1,4)

    if choice == "yes":
        draw_d4(roll)

    if roll == 18:
        print_dramatic_text("WINNER!!")
        print_dramatic_text("You continue on and make it into the train station")
    else:
        print_dramatic_text("FAIL!! HOMELESS MAN GETS YOU")

