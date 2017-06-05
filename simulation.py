# Andy Thai
# June 2017
import sys
import random
sys.stdout.flush()  # Force a flush to stdout


# Simulates player choices
def run_simulation(p1, p2, num_times, debug):
    # For loop to run through simulation
    for iteration in range(0, num_times):
        # Player 1 starts
        p1_matching_a, p1_matching_b = p1.calc_matching()       # Get matching ratios
        # These are normalized to 1

        if debug:                                               # Print entire log
            print('Income for P1\'s A: ' + str(p1_matching_a))
            print('Income for P1\'s B: ' + str(p1_matching_b))
        elif iteration == num_times - 1:                        # Only print at last iteration
            print('\nIncome for P1\'s A: ' + str(p1_matching_a))
            print('Income for P1\'s B: ' + str(p1_matching_b) + '\n')

        # Calculate what button the player should pick
        if random.random() < p1_matching_a:
            p1.pick_button('A')
            if debug:
                print('Player1 picked button A.\n')
        else:
            p1.pick_button('B')
            if debug:
                print('Player1 picked button B.\n')

        # Player 2 starts
        p2_matching_a, p2_matching_b = p2.calc_matching()

        if debug:
            print('Income for P2\'s A: ' + str(p2_matching_a))
            print('Income for P2\'s B: ' + str(p2_matching_b))
        elif iteration == num_times - 1:
            print('Income for P2\'s A: ' + str(p2_matching_a))
            print('Income for P2\'s B: ' + str(p2_matching_b) + '\n')

        if random.random() < p2_matching_a:
            p2.pick_button('A')
            if debug:
                print('Player2 picked button A.\n')
        else:
            p2.pick_button('B')
            if debug:
                print('Player2 picked button B.\n')
    return p1_matching_a, p1_matching_b, p2_matching_a, p2_matching_b


# Prints scores and information
def show_info(p1, p2, num_turns):
    # Compute for player 1
    print('****************** PLAYER 1 ******************')
    # Prints number of rewarded button choices / total button choices
    print('A choices (rewarded / total) : \t' + str(p1.score_a) + ' / ' + str(p1.times_picked_a) +
          '\t\t(result: ' + str(round(p1.score_a / p1.times_picked_a, 2)) +
          ' | true: ' + str(p1.prob_a) + ')')
    print('B choices (rewarded / total) : \t' + str(p1.score_b) + ' / ' + str(p1.times_picked_b) +
          '\t\t(result: ' + str(round(p1.score_b / p1.times_picked_b, 2)) +
          ' | true: ' + str(p1.prob_b) + ')')
    print('Total score : \t\t\t\t\t' + str(p1.score_total) + ' / ' + str(num_turns))
    # Compute for player 2
    print('\n****************** PLAYER 2 ******************')
    print('A choices (rewarded / total) : \t' + str(p2.score_a) + ' / ' + str(p2.times_picked_a) +
          '\t\t(result: ' + str(round(p2.score_a / p2.times_picked_a, 2)) +
          ' | true: ' + str(p2.prob_a) + ')')
    print('B choices (rewarded / total) : \t' + str(p2.score_b) + ' / ' + str(p2.times_picked_b) +
          '\t\t(result: ' + str(round(p2.score_b / p2.times_picked_b, 2)) +
          ' | true: ' + str(p2.prob_b) + ')')
    print('Total score: \t\t\t\t\t' + str(p2.score_total) + ' / ' + str(num_turns))
    return
