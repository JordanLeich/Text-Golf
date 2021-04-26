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
ai_hits = 0
user_wins = 0
ai_terrain_luck = 0
ai_club_choice = 0


def intro():  # This is an introduction function for the game that only plays once per game
    global user_hits, game_counter, terrain_luck, user_wins, ai_hits
    user_hits = 0
    ai_hits = 0
    print(colors.green + 'Welcome to Text Golf, made by Jordan Leich.\n' + colors.reset)
    time.sleep(1.5)
    print(colors.yellow + '''Important things to know!
1. If you are -10 yards or less from the hole, you are automatically counted as getting the ball in the hole!
2. The amount of yards you have to hit for and the yards hit by each club is always randomized each time!
3. If you are 50 yards or less away from the hole, it is impossible for you to hit the golf ball into a pond/sand bar!
4. There's a 13% percent chance that you will hit onto a pond/sand bar each time you hit!
5. When playing against an opponent, game speed and timing is increased greatly so that you can then take your turn!\n
''' + colors.reset)
    time.sleep(2)

    solo_or_ai_choice = input('Would you like to play Text Golf as a solo player or against an ai opponent? (solo or '
                              'ai): ')
    print()
    time.sleep(1)

    if solo_or_ai_choice.lower() == 'solo' or solo_or_ai_choice.lower() == 's':
        print(colors.green + 'You have selected a solo game...\n' + colors.reset)
        time.sleep(.500)
        game()

    elif solo_or_ai_choice.lower() == 'ai' or solo_or_ai_choice.lower() == 'a':
        print(colors.green + 'You have selected a game against an ai opponent...\n' + colors.reset)
        time.sleep(.500)
        ai_turn()

    else:
        print(colors.red + 'User input error found with game selection choice...\n' + colors.reset)
        time.sleep(1)
        intro()


def game():  # Main function of the game that is used for hitting and scoring
    global user_hits, game_counter, terrain_luck, ai_hits, user_wins
    hole_yards = random.randint(200, 500)
    print(colors.green + 'You enter the golf course and gets ready to hit...\n' + colors.reset)
    time.sleep(1.5)
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

    if ai_hits >= 1 and -10 <= hole_yards <= 0:
        ai_game_results()

    elif -10 <= hole_yards <= 0:
        results()

    else:
        print(colors.red + 'End of scoring error caught...\n' + colors.reset)
        time.sleep(1)
        restart()


def results():  # this function shows the end results of the game and allows the user to restart the game
    global ai_hits, user_hits, game_counter, user_wins
    print(colors.green + 'Well Played! You got the ball into the hole!\n' + colors.reset)
    time.sleep(1)
    game_counter += 1
    print('Games Played:', game_counter, '\n')
    time.sleep(1.5)

    if user_hits == 1:
        print(colors.blue + 'You earned a Ace, Hole in One! Outstanding Job!!!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 2:
        print(colors.green + 'You earned a Birdie, Very Nice Job!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 3:
        print(colors.green + 'You earned an Eagle, Pretty Good Job!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 4:
        print(colors.green + 'You earned an Double Eagle, Good Job!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 5:
        print(colors.yellow + 'You earned an Bogey, An Average Game!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 6:
        print(colors.yellow + 'You earned an Double Bogey, You Could Do Better!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits >= 7:
        print(colors.red + 'You earned an Triple Bogey, A Disappointing Game!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    restart()


def restart():  # allows the user to restart or end the game
    global ai_hits, user_hits, game_counter, user_wins
    user_restart = input('Would you like to restart (yes or no): ')
    print()
    time.sleep(1)

    if user_restart.lower() == 'y' or user_restart.lower() == 'yes':
        user_hits = 0
        ai_hits = 0
        print(colors.green + 'Restarting the game...' + colors.reset + '\n')
        time.sleep(1)
        intro()

    elif user_restart.lower() == 'n' or user_restart.lower() == 'no':
        end.end()

    else:
        print(colors.red + 'User Input Restart Error Found...' + colors.reset + '\n')
        time.sleep(1)
        restart()


def ai_turn():
    global ai_hits, ai_terrain_luck, game_counter, ai_club_choice
    print(colors.red + 'It is the opponents turn...\n' + colors.reset)
    time.sleep(.500)
    ai_hole_yards = random.randint(200, 500)
    print(colors.red + 'The opponent enters the golf course and gets ready to hit...\n' + colors.reset)
    time.sleep(.500)
    print('The opponents hole is an estimated', ai_hole_yards, 'yards away from themself.\n')
    time.sleep(.500)

    while ai_hole_yards > 0:
        ai_terrain_luck = random.randint(1, 15)
        print()
        time.sleep(1)

        if ai_hole_yards >= 150:
            ai_hits += 1
            ai_club_choice = '1'

        elif 120 <= ai_hole_yards <= 149:
            ai_hits += 1
            ai_club_choice = '2'

        elif 65 <= ai_hole_yards <= 119:
            ai_hits += 1
            ai_club_choice = '3'

        elif 30 <= ai_hole_yards <= 64:
            ai_hits += 1
            ai_club_choice = '4'

        elif 1 <= ai_hole_yards <= 29:
            ai_hits += 1
            ai_club_choice = '5'

        elif -50 <= ai_hole_yards <= -11:
            ai_hits += 1
            ai_club_choice = '5'

        else:
            print(colors.red + 'AI club choice error found...\n' + colors.reset)
            time.sleep(1)
            restart()

        if ai_terrain_luck == 5 and ai_hole_yards >= 70 and ai_club_choice == '1':
            ai_hit_yards = random.randint(150, 200)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a pond... The opponent will be set back 15 yards!\n' +
                  colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Opponents current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 5 and ai_hole_yards >= 70 and ai_club_choice == '2':
            ai_hit_yards = random.randint(105, 135)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a pond... Opponent will be set back 15 yards!\n' +
                colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Opponents current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 5 and ai_hole_yards >= 70 and ai_club_choice == '3':
            ai_hit_yards = random.randint(65, 100)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a pond... Opponent will be set back 15 yards!\n' +
                colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 5 and ai_hole_yards >= 70 and ai_club_choice == '4':
            ai_hit_yards = random.randint(30, 40)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a pond... Opponent will be set back 15 yards!\n' +
                colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 5 and ai_hole_yards >= 70 and ai_club_choice == '5':
            ai_hit_yards = random.randint(1, 20)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards += ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a pond... Opponent will be set back 15 yards!\n' +
                colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 6 and ai_hole_yards >= 70 and ai_club_choice == '1':
            ai_hit_yards = random.randint(150, 200)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... Opponent will be set back 15 '
                                  'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 6 and ai_hole_yards >= 70 and ai_club_choice == '2':
            ai_hit_yards = random.randint(105, 135)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... Opponent will be set back 15 yards!\n'
                + colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 6 and ai_hole_yards >= 70 and ai_club_choice == '3':
            ai_hit_yards = random.randint(65, 100)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... Opponent will be set back 15 yards!\n'
                + colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 6 and ai_hole_yards >= 70 and ai_club_choice == '4':
            ai_hit_yards = random.randint(30, 40)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... Opponent will be set back 15 yards!\n'
                + colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_terrain_luck == 6 and ai_hole_yards >= 70 and ai_club_choice == '5':
            ai_hit_yards = random.randint(1, 20)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print(
                colors.yellow + 'Uh-Oh! The golf ball landed in a sand bar... Opponent will be set back 15 yards!\n'
                + colors.reset)
            time.sleep(.500)
            ai_hole_yards += 15
            print('Current yards away from the hole now:', ai_hole_yards, '\n')

        elif ai_club_choice == '1':
            ai_hit_yards = random.randint(150, 200)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print('Yards away from hole:', ai_hole_yards, '\n')
            time.sleep(.500)

        elif ai_club_choice == '2':
            ai_hit_yards = random.randint(105, 135)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print('Yards away from hole:', ai_hole_yards, '\n')
            time.sleep(.500)

        elif ai_club_choice == '3':
            ai_hit_yards = random.randint(65, 100)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print('Yards away from hole:', ai_hole_yards, '\n')
            time.sleep(.500)

        elif ai_club_choice == '4':
            ai_hit_yards = random.randint(30, 40)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print('Yards away from hole:', ai_hole_yards, '\n')
            time.sleep(.500)

        elif ai_club_choice == '5' and 1 <= ai_hole_yards <= 10:
            ai_hit_yards = random.randint(1, 5)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print('Yards away from hole:', ai_hole_yards, '\n')
            time.sleep(.500)

        elif ai_club_choice == '5':
            ai_hit_yards = random.randint(1, 20)
            print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
            time.sleep(.500)
            ai_hole_yards -= ai_hit_yards
            print('Yards away from hole:', ai_hole_yards, '\n')
            time.sleep(.500)

        while ai_hole_yards < -10:  # while statement occurs when the user has hit the golf ball past -10 yards
            print(colors.red + 'Ouch! Opponent is too far away from the hole, keep swinging until the Opponent is '
                               'at least -10 yards away from the hole!\n' + colors.reset)
            time.sleep(.500)

            if ai_hole_yards >= 150:
                ai_club_choice = '1'
                ai_hits += 1

            elif 120 <= ai_hole_yards <= 149:
                ai_club_choice = '2'
                ai_hits += 1

            elif 65 <= ai_hole_yards <= 119:
                ai_club_choice = '3'
                ai_hits += 1

            elif 30 <= ai_hole_yards <= 64:
                ai_club_choice = '4'
                ai_hits += 1

            elif 1 <= ai_hole_yards <= 29:
                ai_club_choice = '5'
                ai_hits += 1

            elif -50 <= ai_hole_yards <= -11:
                ai_club_choice = '5'
                ai_hits += 1

            else:
                print(colors.red + 'AI club choice error found...\n' + colors.reset)
                time.sleep(1)
                restart()

            ai_hits += 1
            print()
            time.sleep(1)

            if ai_club_choice == '1':
                ai_hit_yards = random.randint(150, 200)
                print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(.500)
                ai_hole_yards += ai_hit_yards
                print('Yards away from hole:', ai_hole_yards, '\n')
                time.sleep(.500)

            elif ai_club_choice == '2':
                ai_hit_yards = random.randint(105, 135)
                print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(.500)
                ai_hole_yards += ai_hit_yards
                print('Yards away from hole:', ai_hole_yards, '\n')
                time.sleep(.500)

            elif ai_club_choice == '3':
                ai_hit_yards = random.randint(65, 100)
                print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(.500)
                ai_hole_yards += ai_hit_yards
                print('Yards away from hole:', ai_hole_yards, '\n')
                time.sleep(.500)

            elif ai_club_choice == '4':
                ai_hit_yards = random.randint(30, 40)
                print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(.500)
                ai_hole_yards += ai_hit_yards
                print('Yards away from hole:', ai_hole_yards, '\n')
                time.sleep(.500)

            elif ai_club_choice == '5' and -11 >= ai_hole_yards >= -20:
                ai_hit_yards = random.randint(1, 5)
                print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(.500)
                ai_hole_yards += ai_hit_yards
                print('Yards away from hole:', ai_hole_yards, '\n')
                time.sleep(.500)

            elif ai_club_choice == '5':
                ai_hit_yards = random.randint(1, 20)
                print(colors.red + 'Opponent hit the golf ball for', ai_hit_yards, 'yards!\n' + colors.reset)
                time.sleep(.500)
                ai_hole_yards += ai_hit_yards
                print('Yards away from hole:', ai_hole_yards, '\n')
                time.sleep(.500)

        if -10 <= ai_hole_yards <= 0:
            print(colors.yellow + 'Well Played! Opponent got the ball into the hole! Your turn will start...\n' + colors
                  .reset)
            time.sleep(2)
            game()


def ai_game_results():
    global ai_hits, user_hits, game_counter, user_wins
    time.sleep(1)
    game_counter += 1
    time.sleep(1.5)

    if user_hits == ai_hits:
        print(colors.yellow + 'A tie has been found between you and the opponent!\n' + colors.reset)
        time.sleep(2)
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 1 and user_hits > ai_hits:
        print(
            colors.blue + 'You earned a Ace, Hole in One! Outstanding Job!!! You have lost to the opponent due to '
                          'having more hit attempts than the opponent!\n',
            colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 1 and user_hits < ai_hits:
        print(colors.blue + 'You earned a Ace, Hole in One! Outstanding Job!!! You have won against the opponent due '
                            'to having less hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 2 and user_hits > ai_hits:
        print(colors.green + 'You earned a Birdie, Very Nice Job! You have lost to the opponent due to having more '
                             'hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 2 and user_hits < ai_hits:
        print(colors.green + 'You earned a Birdie, Very Nice Job! You have won against the opponent due to having more '
                             'hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 3 and user_hits > ai_hits:
        print(colors.green + 'You earned an Eagle, Pretty Good Job! You have lost to the opponent due to having more '
                             'hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 3 and user_hits < ai_hits:
        print(colors.green + 'You earned an Eagle, Pretty Good Job! You have won against the opponent due to having '
                             'more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 4 and user_hits > ai_hits:
        print(colors.green + 'You earned an Double Eagle, Good Job! You have lost to the opponent due to having more '
                             'hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 4 and user_hits < ai_hits:
        print(colors.green + 'You earned an Double Eagle, Good Job! You have won against the opponent due to having '
                             'more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 5 and user_hits > ai_hits:
        print(colors.yellow + 'You earned an Bogey, An Average Game! You have lost to the opponent due to having more '
                              'hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 5 and user_hits < ai_hits:
        print(colors.yellow + 'You earned an Bogey, An Average Game! You have won against the opponent due to having '
                              'more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 6 and user_hits > ai_hits:
        print(colors.yellow + 'You earned an Double Bogey, You Could Do Better! You have lost to the opponent due to '
                              'having more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits == 6 and user_hits < ai_hits:
        print(
            colors.yellow + 'You earned an Double Bogey, You Could Do Better! You have won against the opponent due '
                            'to having more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif user_hits >= 7 and user_hits > ai_hits:
        print(
            colors.red + 'You earned an Triple Bogey, A Disappointing Game! You have lost to the opponent due to '
                         'having more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins -= 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    elif 7 <= user_hits < ai_hits:
        print(
            colors.red + 'You earned an Triple Bogey, A Disappointing Game! You have won against the opponent due '
                         'to having more hit attempts than the opponent!\n', colors.reset)
        time.sleep(2)
        user_wins += 1
        print('Wincount:', user_wins, '\n')
        time.sleep(1)

    print('Games Played:', game_counter, '\n')
    restart()


intro()  # initiates the very beginning of the game
