# Andy Thai
# June 2017

# import statements
from player import Player
from simulation import run_simulation
from simulation import show_info
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# SETTINGS (Only change options here)
# mode; 0: no weight, 1: unequal weight, 2: equal weight
def setup(mode):
    # CHANGE these

    # How much weight to place on partner's actions for mode 1
    # Weight is player1 * (1 - weight) + player2 * (weight)
    # Lower means player 2 plays less attention to player 1
    # Value should be between 0.0 and 1.0
    weight = 0.25

    # Probabilities of reward for each button (a, b) for each player (p1, p2)
    # Values should be between 0.0 and 1.0
    p1_prob_a = 0.2
    p1_prob_b = 0.8
    p2_prob_a = 0.2
    p2_prob_b = 0.8

    # Number of iterations for each simulation
    num_turns = 1000

    # Debug variable, show all income changes if true, otherwise only last income ratio
    # Leave false if you don't know what you're doing
    debug = False

    ####################################################################################

    # Do NOT change these
    player1 = Player(1, 0, 0, p1_prob_a, p1_prob_b)
    player2 = Player(2, mode, weight, p2_prob_a, p2_prob_b)
    player1.other_player = player2
    player2.other_player = player1
    return player1, player2, num_turns, debug


# main method
# In each trial, player 1 plays without paying attention to the partner
# Only player 2's behavior changes
def main():
    # Points for graphing data
    points_g2_a = []
    points_g2_b = []
    points_g3 = [(0, 0)]

    # Run independent matching trial
    print('\nMATCHING WITHOUT PARTNER DEPENDENCE')
    player1, player2, num_turns, debug = setup(0)
    m0_p1_a, m0_p1_b, m0_p2_a, m0_p2_b = run_simulation(player1, player2, num_turns, debug,
                                                        points_g2_a, points_g2_b, 0)
    show_info(player1, player2, num_turns)

    ''' GRAPH SETUP '''

    # Set up graph 1a
    plt.figure(1)
    plt.title('Probability of choosing A as a function\nPlayer 1 (0.6, 0.6)')
    plt.xlabel('Fractional income of A')
    plt.ylabel('Ratio for A choices')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    t1_patch = mpatches.Patch(color='red', label='Independent')
    t2_patch = mpatches.Patch(color='blue', label=str(player2.weight) + ' Weighting')
    t3_patch = mpatches.Patch(color='green', label='Joint')
    plt.legend(handles=[t1_patch, t2_patch, t3_patch])

    # Set up graph 1b
    plt.figure(2)
    plt.title('Probability of choosing A as a function\nPlayer 1 (0.2, 0.8)')
    plt.xlabel('Fractional income of A')
    plt.ylabel('Ratio for A choices')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    t1_patch = mpatches.Patch(color='red', label='Independent')
    t2_patch = mpatches.Patch(color='blue', label=str(player2.weight) + ' Weighting')
    t3_patch = mpatches.Patch(color='green', label='Joint')
    plt.legend(handles=[t1_patch, t2_patch, t3_patch])

    # Set up graph 2a
    plt.figure(3)
    plt.title('Change in Income over time for Player 2, A' +
              '\nPlayer 1 (' + str(player1.prob_a) + ', ' + str(player1.prob_b) + '); ' +
              'Player 2 (' + str(player2.prob_a) + ', ' + str(player2.prob_b) + ')')
    plt.xlabel('Time')
    plt.ylabel('Income')
    plt.xlim(0, num_turns)
    plt.ylim(0, 1)
    t1_patch = mpatches.Patch(color='red', label='Independent')
    t2_patch = mpatches.Patch(color='blue', label=str(player2.weight) + ' Weighting')
    t3_patch = mpatches.Patch(color='green', label='Joint Decision History')
    true_patch = mpatches.Patch(color='black', label='P(A)/[P(A) + P(B)]: '
                                                     + str(player2.prob_a / (player2.prob_a + player2.prob_b)))
    plt.legend(handles=[t1_patch, t2_patch, t3_patch, true_patch])

    # Set up graph 2b
    plt.figure(4)
    plt.title('Change in income over time for Player 2, B' +
              '\nPlayer 1 (' + str(player1.prob_a) + ', ' + str(player1.prob_b) + '); ' +
              'Player 2 (' + str(player2.prob_a) + ', ' + str(player2.prob_b) + ')')
    plt.xlabel('Time')
    plt.ylabel('Income')
    plt.xlim(0, num_turns)
    plt.ylim(0, 1)
    t1_patch = mpatches.Patch(color='red', label='Independent')
    t2_patch = mpatches.Patch(color='blue', label=str(player2.weight) + ' Weighting')
    t3_patch = mpatches.Patch(color='green', label='Joint')
    true_patch = mpatches.Patch(color='black', label='P(B)/[P(A) + P(B)]: ' +
                                                     str(player2.prob_b / (player2.prob_a + player2.prob_b)))
    plt.legend(handles=[t1_patch, t2_patch, t3_patch, true_patch])

    # Set up graph 3
    plt.figure(5)
    plt.title('Cumulative choices' +
              '\nPlayer 1 (' + str(player1.prob_a) + ', ' + str(player1.prob_b) + '); ' +
              'Player 2 (' + str(player2.prob_a) + ', ' + str(player2.prob_b) + ')')
    plt.xlabel('Cumulative A choices')
    plt.ylabel('Cumulative B choices')
    t1_patch = mpatches.Patch(color='red', label='Independent')
    t2_patch = mpatches.Patch(color='blue', label=str(player2.weight) + ' Weighting')
    t3_patch = mpatches.Patch(color='green', label='Joint')
    slope_patch = mpatches.Patch(color='black', label='y = x')
    plt.legend(handles=[t1_patch, t2_patch, t3_patch, slope_patch])
    plt.plot(range(0, num_turns), range(0, num_turns), color='black', linewidth=3)

    ''' FEED DATA INTO GRAPHS '''

    # 2a
    plt.figure(3)
    plt.plot([point[1] for point in points_g2_a], [point[0] for point in points_g2_a], color='red', linewidth=2)
    plt.hlines(player2.prob_a / (player2.prob_a + player2.prob_b), 0, num_turns, colors='black', linewidth=4)
    points_g2_a = []    # Reset

    # 2b
    plt.figure(4)
    plt.plot([point[1] for point in points_g2_b], [point[0] for point in points_g2_b], color='red', linewidth=2)
    plt.hlines(player2.prob_b / (player2.prob_a + player2.prob_b), 0, num_turns, colors='black', linewidth=4)
    points_g2_b = []  # Reset

    # Get choices for 3
    for i in range(2, len(player2.history)):
        if player2.history[i][0] == 'A':
            points_g3.append((points_g3[-1][0] + 1, points_g3[-1][1]))
        else:
            points_g3.append((points_g3[-1][0], points_g3[-1][1] + 1))

    # 3
    plt.figure(5)
    graph3_max_x = max(point[0] for point in points_g3)
    graph3_max_y = max(point[1] for point in points_g3)
    plt.plot([point[0] for point in points_g3], [point[1] for point in points_g3], color='red')
    points_g3 = [(0, 0)]

    # 1a
    graph1_points = []
    iterations = np.linspace(0.0, 1.0, num=21)
    plt.figure(1)
    # Trial 1
    for step in iterations:
        player1 = Player(1, 0, 0, 0.6, 0.6)
        player2 = Player(2, 0, 0.25, step, 1.0 - step)
        player1.other_player = player2
        player2.other_player = player1
        run_simulation(player1, player2, num_turns, debug, [], [], 1)
        fractional_income = player2.prob_a / (player2.prob_a + player2.prob_b)
        prob_choice = player2.times_picked_a / (player2.times_picked_a + player2.times_picked_b)
        graph1_points.append((fractional_income, prob_choice))
    plt.plot([point[0] for point in graph1_points], [point[1] for point in graph1_points], color='red')
    # Trial 2
    graph1_points = []
    for step in iterations:
        player1 = Player(1, 0, 0, 0.6, 0.6)
        player2 = Player(2, 1, 0.25, step, 1.0 - step)
        player1.other_player = player2
        player2.other_player = player1
        run_simulation(player1, player2, num_turns, debug, [], [], 1)
        fractional_income = player2.prob_a / (player2.prob_a + player2.prob_b)
        prob_choice = player2.times_picked_a / (player2.times_picked_a + player2.times_picked_b)
        graph1_points.append((fractional_income, prob_choice))
    plt.plot([point[0] for point in graph1_points], [point[1] for point in graph1_points], color='blue')
    # Trial 3
    graph1_points = []
    for step in iterations:
        player1 = Player(1, 0, 0, 0.6, 0.6)
        player2 = Player(2, 2, 0.25, step, 1.0 - step)
        player1.other_player = player2
        player2.other_player = player1
        run_simulation(player1, player2, num_turns, debug, [], [], 1)
        fractional_income = player2.prob_a / (player2.prob_a + player2.prob_b)
        prob_choice = player2.times_picked_a / (player2.times_picked_a + player2.times_picked_b)
        graph1_points.append((fractional_income, prob_choice))
    plt.plot([point[0] for point in graph1_points], [point[1] for point in graph1_points], color='green')

    # 1b
    graph1_points = []
    plt.figure(2)
    # Trial 1
    for step in iterations:
        player1 = Player(1, 0, 0, 0.2, 0.8)
        player2 = Player(2, 0, 0.25, step, 1.0 - step)
        player1.other_player = player2
        player2.other_player = player1
        run_simulation(player1, player2, num_turns, debug, [], [], 1)
        fractional_income = player2.prob_a / (player2.prob_a + player2.prob_b)
        prob_choice = player2.times_picked_a / (player2.times_picked_a + player2.times_picked_b)
        graph1_points.append((fractional_income, prob_choice))
    plt.plot([point[0] for point in graph1_points], [point[1] for point in graph1_points], color='red')
    # Trial 2
    graph1_points = []
    for step in iterations:
        player1 = Player(1, 0, 0, 0.2, 0.8)
        player2 = Player(2, 1, 0.25, step, 1.0 - step)
        player1.other_player = player2
        player2.other_player = player1
        run_simulation(player1, player2, num_turns, debug, [], [], 1)
        fractional_income = player2.prob_a / (player2.prob_a + player2.prob_b)
        prob_choice = player2.times_picked_a / (player2.times_picked_a + player2.times_picked_b)
        graph1_points.append((fractional_income, prob_choice))
    plt.plot([point[0] for point in graph1_points], [point[1] for point in graph1_points], color='blue')
    # Trial 3
    graph1_points = []
    for step in iterations:
        player1 = Player(1, 0, 0, 0.2, 0.8)
        player2 = Player(2, 2, 0.25, step, 1.0 - step)
        player1.other_player = player2
        player2.other_player = player1
        run_simulation(player1, player2, num_turns, debug, [], [], 1)
        fractional_income = player2.prob_a / (player2.prob_a + player2.prob_b)
        prob_choice = player2.times_picked_a / (player2.times_picked_a + player2.times_picked_b)
        graph1_points.append((fractional_income, prob_choice))
    plt.plot([point[0] for point in graph1_points], [point[1] for point in graph1_points], color='green')

    # Run weighted matching trial
    print('\nPLAYER 2 TAKES PLAYER 1\'S DECISIONS INTO ACCOUNT. WEIGHS OWN DECISIONS MORE')
    print(str(player2.weight))
    player1, player2, num_turns, debug = setup(1)
    m1_p1_a, m1_p1_b, m1_p2_a, m1_p2_b = run_simulation(player1, player2, num_turns, debug, points_g2_a, points_g2_b, 0)
    show_info(player1, player2, num_turns)

    ''' FEED DATA INTO GRAPHS '''

    # 2a
    plt.figure(3)
    plt.plot([point[1] for point in points_g2_a], [point[0] for point in points_g2_a], color='blue', linewidth=2)
    points_g2_a = []

    # 2b
    plt.figure(4)
    plt.plot([point[1] for point in points_g2_b], [point[0] for point in points_g2_b], color='blue', linewidth=2)
    points_g2_b = []

    # Get choices for 3
    for i in range(2, len(player2.history)):
        if player2.history[i][0] == 'A':
            points_g3.append((points_g3[-1][0] + 1, points_g3[-1][1]))
        else:
            points_g3.append((points_g3[-1][0], points_g3[-1][1] + 1))

    # 3
    plt.figure(5)
    graph3_max_x_2 = max(point[0] for point in points_g3)
    graph3_max_x = max(graph3_max_x_2, graph3_max_x)
    graph3_max_y_2 = max(point[1] for point in points_g3)
    graph3_max_y = max(graph3_max_y_2, graph3_max_y)
    plt.plot([point[0] for point in points_g3], [point[1] for point in points_g3], color='blue')
    points_g3 = [(0, 0)]

    # Run unweighted matching trial
    print('\nPLAYER 2 JOINTLY TAKES PLAYER 1\'S DECISIONS INTO ACCOUNT.')
    player1, player2, num_turns, debug = setup(2)
    m2_p1_a, m2_p1_b, m2_p2_a, m2_p2_b = run_simulation(player1, player2, num_turns, debug, points_g2_a, points_g2_b, 0)
    show_info(player1, player2, num_turns)

    ''' FEED DATA INTO GRAPHS '''

    # 2a
    plt.figure(3)
    plt.plot([point[1] for point in points_g2_a], [point[0] for point in points_g2_a], color='green', linewidth=2)

    # 2b
    plt.figure(4)
    plt.plot([point[1] for point in points_g2_b], [point[0] for point in points_g2_b], color='green', linewidth=2)

    # Get choices for 3
    for i in range(2, len(player2.history)):
        if player2.history[i][0] == 'A':
            points_g3.append((points_g3[-1][0] + 1, points_g3[-1][1]))
        else:
            points_g3.append((points_g3[-1][0], points_g3[-1][1] + 1))

    # 3
    plt.figure(5)
    graph3_max_x_2 = max(point[0] for point in points_g3)
    graph3_max_x = max(graph3_max_x_2, graph3_max_x)
    graph3_max_y_2 = max(point[1] for point in points_g3)
    graph3_max_y = max(graph3_max_y_2, graph3_max_y)
    plt.plot([point[0] for point in points_g3], [point[1] for point in points_g3], color='green')
    plt.xlim(0, graph3_max_x)
    plt.ylim(0, graph3_max_y)

    # Prints out summary of income values
    print('\n\n***** SUMMARY (' + str(num_turns) + ' RUNS) *****')
    print('\t\tP2 true values:')
    print('\t\t\t' + 'a: ' + str(player2.prob_a / (player2.prob_a + player2.prob_b)))
    print('\t\t\t' + 'b: ' + str(player2.prob_b / (player2.prob_a + player2.prob_b)))
    print('\nTRIAL 1: Player 2 ignores Player 1\'s actions:')
    print('\tP2\'s Button A Income Rate: ' + str(round(m0_p2_a, 2)))
    print('\tP2\'s Button B Income Rate: ' + str(round(m0_p2_b, 2)))
    if player2.weight < 0.5:
        keyword = 'less'
    else:
        keyword = 'more'
    print('TRIAL 2: Player 2 weighs (' + str(player2.weight) + ') Player 1\'s actions ' + keyword)
    print('\tP2\'s Button A Income Rate: ' + str(round(m1_p2_a, 2)))
    print('\tP2\'s Button B Income Rate: ' + str(round(m1_p2_b, 2)))
    print('TRIAL 3: Player 2 jointly uses Player 1\'s actions:')
    print('\tP2\'s Button A Income Rate: ' + str(round(m2_p2_a, 2)))
    print('\tP2\'s Button B Income Rate: ' + str(round(m2_p2_b, 2)))

    # Show plots
    plt.show(1)
    plt.show(2)
    plt.show(3)
    plt.show(4)
    plt.show(5)

    return


# Run main
if __name__ == "__main__":
    main()
