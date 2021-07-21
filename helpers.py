import colors
from os import system, name

def print_intro():
 colors.green
 print(colors.green + '     _______        _      _____       _  __ ' + colors.reset)
 print(colors.green + '    |__   __|      | |    / ____|     | |/ _|' + colors.reset)
 print(colors.green + '       | | _____  _| |_  | |  __  ___ | | |_ ' + colors.reset) 
 print(colors.green + '       | |/ _ \ \/ / __| | | |_ |/ _ \| |  _|' + colors.reset) 
 print(colors.green + '       | |  __/>  <| |_  | |__| | (_) | | |  ' + colors.reset) 
 print(colors.green + '       |_|\___/_/\_ \__|  \_____|\___/|_|_|    A game by Jordan Leich \n' + colors.reset) 
 colors.reset
                                          
                                          
def print_important():
        print(colors.yellow + '''Important Info:
1. If your ball lands -10 yards or less from the hole, it is counted as getting the ball in the hole!
2. The amount of yards you have to hit and the yards hit by each club is randomized!
3. If you are 50 yards or less away from the hole, you will not hit the golf ball into a pond/sand bar!
4. There's a 13% chance that you will hit onto a pond/sand bar (Unless <=50 yards from the hole)
5. When against an opponent, game speed and timing is increased greatly so that you can then take your turn!\n
''' + colors.reset)


# define our clear function
def clear_console():
    # windows systems
    if name == 'nt':
        _ = system('cls')
  
    # mac and linux systems
    else:
        _ = system('clear')