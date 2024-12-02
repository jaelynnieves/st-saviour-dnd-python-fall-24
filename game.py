import time
import random 
from tav import Tav
from draw import draw_d20, draw_d4, draw_d6

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

    r = random.randint(1,6)
    generate_monster
    if r == 1 or r ==2 or r ==3:
       pigeon = '\U0001F426' 
       print(' You are on your way to work ')
       print(pigeon + ' when a pigeon flies down toward you')
       print('roll required: 6')
       roll = random.randint(1,20)
       draw_d20(roll)
       return 6
    
    if roll == 6:
        print_dramatic_text("WINNER")
        print_dramatic_text("You continue on and make it into the train station")
    else:
        print_dramatic_text("FAIL!!")
    
    if r == 4 or r == 5: 
        rat = '\U0001F400'
        print('as you are waiting for the train')
        print(rat + ' a rat runs towards you ')
        print('roll requires: 11')
        r = random.randint(1,20)
        draw_d20(roll)
        return 11
   
    print_dramatic_text("Would you like some help? y/n?")
    choice = input('Choice: ')
    if choice == "yes":
        advantage = draw_d20(roll)
        return advantage 
        
   
    if roll == 11:
        print_dramatic_text("WINNER")
    else:
        print_dramatic_text("You may continue onto the train cart")
        print_dramatic_text("FAIL!! RAT WINS!!")
        print_dramatic_text("YOU 0 Rat 1")
    
    if r == 6:
        man = '\U0001F468'
        print('as you are walking down the block')
        print(man + ' a homeless man appears!')
        print_dramatic_text( " THIS IS THE BIGGEST, THE MEANEST, THE HARDEST OPPONENT EVER")
        print('roll required: 18')
        r = random.randint(1,20)
        draw_d20(roll)
        return 18 
    print_dramatic_text("Would you like some help? y/n?")
    choice = input('Choice: ')
    if choice == "yes":
        guidance = draw_d4
        return guidance 
    
    if roll == 18:
        print_dramatic_text("WINNER!!")
        print_dramatic_text("You continue on and make it into the train station")
    else:
        print_dramatic_text("FAIL!! HOMELESS MAN GETS YOU")

    
    print_dramatic_text('Adventure starts in New York City ')

    if __name__ == '__main__':
        name =   input('Name: ')
        role =   input('Role: ')
  
    print('NEW YORK STRUGGLES')
    player = Tav(name, role)
    player.print_character_sheet()

    def generate_monster() -> int:
     return generate_monster()
