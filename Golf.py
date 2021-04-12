# Made by Jordan Leich on 4/11/21, Last Updated on 4/11/21


# imports
import colors
import random
import end
import restart
import time

# globals
user_hits = 0


def game():
    global user_hits
    print(colors.green + 'Welcome to Text Golf, made by Jordan Leich.\n' + colors.reset)
    time.sleep(1.5)
    print('''Important things to know!
1. If you are -10 yards or less from the hole, you are automatically counted as getting the ball in the hole!
2. The amount of yards you have to hit for and the yards hit by each club is always randomized each time!\n''')
    time.sleep(3)
    hole_yards = random.randint(200, 500)
    print('You enter the golf course and get ready to hit...\n')
    time.sleep(1)
    print('Your hole is an estimated ', hole_yards, ' yards away from you.\n')
    time.sleep(1)

    while hole_yards > 0:
        user_club_choice = input('''1. Driver Club (150+ Yards)
2. 9 Iron Club (Around 120 Yards)
3. Wedge Club (65 to 100 Yards)
4. Putter Club (1 to 20 Yards)
5. Restart Game
6. End Game
        
Which golf club number would you like to pick: ''')
        user_hits += 1
        print()
        time.sleep(1)

        if user_club_choice == '1':
            user_hit_yards = random.randint(150, 200)
            print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole: ', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '2':
            user_hit_yards = random.randint(105, 135)
            print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole: ', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '3':
            user_hit_yards = random.randint(65, 100)
            print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole: ', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '4':
            user_hit_yards = random.randint(1, 20)
            print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
            time.sleep(1)
            hole_yards -= user_hit_yards
            print('Yards away from hole: ', hole_yards, '\n')
            time.sleep(1)

        elif user_club_choice == '5':
            restart.restart()

        elif user_club_choice == '6':
            end.end()

        else:
            print(colors.red + 'User Input Error Found...\n' + colors.reset)
            restart.restart()

        while hole_yards < -10:
            time.sleep(1)

            print(colors.red + 'Ouch! You are too far away from the hole, keep swinging until you are at least -10 '
                               'yards away from the hole!\n' + colors.reset)
            time.sleep(1)
            user_club_choice = input('''1. Driver Club (150+ Yards)
2. 9 Iron Club (Around 120 Yards)
3. Wedge Club (65 to 100 Yards)
4. Putter Club (1 to 20 Yards)
6. End Game

Which golf club number would you like to pick: ''')
            user_hits += 1
            print()
            time.sleep(1)

            if user_club_choice == '1':
                user_hit_yards = random.randint(150, 200)
                print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole: ', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '2':
                user_hit_yards = random.randint(105, 135)
                print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole: ', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '3':
                user_hit_yards = random.randint(65, 100)
                print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole: ', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '4':
                user_hit_yards = random.randint(1, 20)
                print(colors.green + 'You hit the golf ball for ', user_hit_yards, ' yards!\n' + colors.reset)
                time.sleep(1)
                hole_yards += user_hit_yards
                print('Yards away from hole: ', hole_yards, '\n')
                time.sleep(1)

            elif user_club_choice == '5':
                restart.restart()

            elif user_club_choice == '6':
                end.end()

            else:
                print(colors.red + 'User Input Error Found...\n' + colors.reset)
                restart.restart()

        if -10 <= hole_yards <= 0:
            results()


def results():
    print(colors.green + 'Well Played! You got the ball into the hole!\n' + colors.red)
    time.sleep(1.5)

    if user_hits == 1:
        print(colors.green + 'You earned a Ace, Hole in One! Outstanding Job!!!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    elif user_hits == 2:
        print(colors.green + 'You earned a Birdie, Very Nice Job!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    elif user_hits == 3:
        print(colors.green + 'You earned an Eagle, Pretty Good Job!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    elif user_hits == 4:
        print(colors.green + 'You earned an Double Eagle, Good Job!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    elif user_hits == 5:
        print(colors.yellow + 'You earned an Bogey, An Average Game!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    elif user_hits == 6:
        print(colors.yellow + 'You earned an Double Bogey, You Could Do Better!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    elif user_hits >= 7:
        print(colors.red + 'You earned an Triple Bogey, A Disappointing Game!\n', colors.reset)
        time.sleep(2)
        restart.restart()


game()
