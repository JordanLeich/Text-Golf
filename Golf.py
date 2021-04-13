# Made by Jordan Leich on 4/11/21, Last Updated on 4/11/21


# imports
import colors
import random
import end
import time

# globals
user_hits = 0
game_counter = 0
terrain_luck = 0


def intro():  # This is an introduction function for the game that only plays once per game
    global user_hits, game_counter, terrain_luck
    print(colors.green + 'Welcome to Text Golf, made by Jordan Leich.\n' + colors.reset)
    time.sleep(1.5)
    print(colors.yellow + '''Important things to know!
1. If you are -10 yards or less from the hole, you are automatically counted as getting the ball in the hole!
2. The amount of yards you have to hit for and the yards hit by each club is always randomized each time!
3. If you are 50 yards or less away from the hole, it is impossible for you to hit the golf ball into a pond/sand bar!
4. There's a 13% percent chance that you will hit onto a pond/sand bar each time you hit!\n''' + colors.reset)
    time.sleep(2)
    game()


def game():  # Main function of the game that is used for hitting and scoring
    global user_hits, game_counter, terrain_luck
    hole_yards = random.randint(200, 500)
    print('You enter the golf course and get ready to hit...\n')
    time.sleep(1)
    print('Your hole is an estimated', hole_yards, 'yards away from you.\n')
    time.sleep(1)

    while hole_yards > 0:
        user_club_choice = input('''1. Driver Club (150+ Yards)
2. 9 Iron Club (Around 120 Yards)
3. Wedge Club (65 to 100 Yards)
4. Putter Club (Harder hit, 30 to 40 Yards)
5. Putter Club (1 to 20 Yards)
6. Restart Game
7. End Game
        
Which golf club number would you like to pick: ''')
        user_hits += 1
        terrain_luck = random.randint(1, 15)
        print()
        time.sleep(1)

        if terrain_luck == 5 and hole_yards >= 70 and user_club_choice == '1':
            user_hit_yards = random.randint(150, 200)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a pond... You will be set back 15 yards!\n' + colors.
                  reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 5 and hole_yards >= 70 and user_club_choice == '2':
            user_hit_yards = random.randint(105, 135)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a pond... You will be set back 15 yards!\n' + colors.
                  reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 5 and hole_yards >= 70 and user_club_choice == '3':
            user_hit_yards = random.randint(65, 100)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a pond... You will be set back 15 yards!\n' + colors.
                  reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 5 and hole_yards >= 70 and user_club_choice == '4':
            user_hit_yards = random.randint(30, 40)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a pond... You will be set back 15 yards!\n' + colors.
                  reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 5 and hole_yards >= 70 and user_club_choice == '5':
            user_hit_yards = random.randint(1, 20)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards += user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a pond... You will be set back 15 yards!\n' + colors.
                  reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 6 and hole_yards >= 70 and user_club_choice == '1':
            user_hit_yards = random.randint(150, 200)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... You will be set back 15 yards!\n' +
                  colors.reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 6 and hole_yards >= 70 and user_club_choice == '2':
            user_hit_yards = random.randint(105, 135)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... You will be set back 15 yards!\n' +
                  colors.reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 6 and hole_yards >= 70 and user_club_choice == '3':
            user_hit_yards = random.randint(65, 100)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... You will be set back 15 yards!\n' +
                  colors.reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 6 and hole_yards >= 70 and user_club_choice == '4':
            user_hit_yards = random.randint(30, 40)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... You will be set back 15 yards!\n' +
                  colors.reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif terrain_luck == 6 and hole_yards >= 70 and user_club_choice == '5':
            user_hit_yards = random.randint(1, 20)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... You will be set back 15 yards!\n' +
                  colors.reset)
            time.sleep(1.5)
            hole_yards += 15
            print('Current yards away from the hole now:', hole_yards, '\n')

        elif user_club_choice == '1':
            user_hit_yards = random.randint(150, 200)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole:', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '2':
            user_hit_yards = random.randint(105, 135)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole:', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '3':
            user_hit_yards = random.randint(65, 100)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole:', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '4':
            user_hit_yards = random.randint(30, 40)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole:', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '5' and 1 <= hole_yards <= 10:
            user_hit_yards = random.randint(1, 5)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole:', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '5':
            user_hit_yards = random.randint(1, 20)
            print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole:', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '6':
            restart()

        elif user_club_choice == '7':
            end.end()

        else:
            print(colors.red + 'User Input Error Found...\n' + colors.reset)
            restart()

        while hole_yards < -10:  # while statement occurs when the user has hit the golf ball past -10 yards
            print(colors.red + 'Ouch! You are too far away from the hole, keep swinging until you are at least -10 '
                               'yards away from the hole!\n' + colors.reset)
            time.sleep(1)
            user_club_choice = input('''1. Driver Club (150+ Yards)
2. 9 Iron Club (Around 120 Yards)
3. Wedge Club (65 to 100 Yards)
4. Putter Club (Harder hit, 30 to 40 Yards)
5. Putter Club (1 to 20 Yards)
6. Restart Game
7. End Game

Which golf club number would you like to pick: ''')
            user_hits += 1
            print()
            time.sleep(1)

            if user_club_choice == '1':
                user_hit_yards = random.randint(150, 200)
                print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole:', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '2':
                user_hit_yards = random.randint(105, 135)
                print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole:', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '3':
                user_hit_yards = random.randint(65, 100)
                print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole:', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '4':
                user_hit_yards = random.randint(30, 40)
                print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole:', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '5' and -11 >= hole_yards >= -20:
                user_hit_yards = random.randint(1, 5)
                print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole:', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '5':
                user_hit_yards = random.randint(1, 20)
                print(colors.green + 'You hit the golf ball for', user_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole:', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '6':
                restart()

            elif user_club_choice == '7':
                end.end()

            else:
                print(colors.red + 'User Input Error Found...\n' + colors.reset)
                restart()

        if -10 <= hole_yards <= 0:
            results()


def results():  # this function shows the end results of the game and allows the user to restart the game
    global user_hits, game_counter
    print(colors.green + 'Well Played! You got the ball into the hole!\n' + colors.reset)
    time.sleep(1)
    game_counter += 1
    print('Games Played:', game_counter, '\n')
    time.sleep(1.5)

    if user_hits == 1:
        print(colors.blue + 'You earned a Ace, Hole in One! Outstanding Job!!!\n', colors.reset)
        time.sleep(2)
        restart()

    elif user_hits == 2:
        print(colors.green + 'You earned a Birdie, Very Nice Job!\n', colors.reset)
        time.sleep(2)
        restart()

    elif user_hits == 3:
        print(colors.green + 'You earned an Eagle, Pretty Good Job!\n', colors.reset)
        time.sleep(2)
        restart()

    elif user_hits == 4:
        print(colors.green + 'You earned an Double Eagle, Good Job!\n', colors.reset)
        time.sleep(2)
        restart()

    elif user_hits == 5:
        print(colors.yellow + 'You earned an Bogey, An Average Game!\n', colors.reset)
        time.sleep(2)
        restart()

    elif user_hits == 6:
        print(colors.yellow + 'You earned an Double Bogey, You Could Do Better!\n', colors.reset)
        time.sleep(2)
        restart()

    elif user_hits >= 7:
        print(colors.red + 'You earned an Triple Bogey, A Disappointing Game!\n', colors.reset)
        time.sleep(2)
        restart()


def restart():  # allows the user to restart or end the game
    global user_hits, game_counter
    user_restart = input('Would you like to restart (yes or no): ')
    print()
    time.sleep(1)

    if user_restart.lower() == 'y' or user_restart.lower() == 'yes':
        user_hits = 0
        print(colors.green + 'Restarting the game...' + colors.reset + '\n')
        time.sleep(1)
        game()

    elif user_restart.lower() == 'n' or user_restart.lower() == 'no':
        end.end()

    else:
        print(colors.red + 'User Input Restart Error Found...' + colors.reset + '\n')
        time.sleep(1)
        restart()


intro()  # initiates the very beginning of the game
