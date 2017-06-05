# Andy Thai
# June 2017

# import statements
from player import Player
from simulation import run_simulation
from simulation import show_info


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
    p1_prob_a = 0.6
    p1_prob_b = 0.6
    p2_prob_a = 0.2
    p2_prob_b = 0.8

    # Number of iterations for each simulation
    num_turns = 3000

    # Debug variable, show all income changes if true, otherwise only last income ratio
    # Leave false if you don't know what you're doing
    debug = False

    ####################################################################################

    # Do NOT change these
    player1 = Player(1, 0,    0,      p1_prob_a, p1_prob_b)
    player2 = Player(2, mode, weight, p2_prob_a, p2_prob_b)
    player1.other_player = player2
    player2.other_player = player1
    return player1, player2, num_turns, debug


# main method
# In each trial, player 1 plays without paying attention to the partner
# Only player 2's behavior changes
def main():
    # Run independent matching trial
    print('\nMATCHING WITHOUT PARTNER DEPENDENCE')
    player1, player2, num_turns, debug = setup(0)
    m0_p1_a, m0_p1_b, m0_p2_a, m0_p2_b = run_simulation(player1, player2, num_turns, debug)
    show_info(player1, player2, num_turns)

    # Run weighted matching trial
    print('\nPLAYER 2 TAKES PLAYER 1\'S DECISIONS INTO ACCOUNT. WEIGHS OWN DECISIONS MORE')
    player1, player2, num_turns, debug = setup(1)
    m1_p1_a, m1_p1_b, m1_p2_a, m1_p2_b = run_simulation(player1, player2, num_turns, debug)
    show_info(player1, player2, num_turns)

    # Run unweighted matching trial
    print('\nPLAYER 2 TAKES PLAYER 1\'S DECISIONS INTO ACCOUNT. WEIGHS DECISIONS EQUALLY')
    player1, player2, num_turns, debug = setup(2)
    m2_p1_a, m2_p1_b, m2_p2_a, m2_p2_b = run_simulation(player1, player2, num_turns, debug)
    show_info(player1, player2, num_turns)

    # Prints out summary of income values
    print('\n\n***** SUMMARY (' + str(num_turns) + ' RUNS) *****')
    print('\t\tP2 true values:')
    print('\t\t\t' + 'a: ' + str(player2.prob_a / (player2.prob_a + player2.prob_b)))
    print('\t\t\t' + 'b: ' + str(player2.prob_b / (player2.prob_a + player2.prob_b)))
    print('\nTRIAL 1: Player 2 ignores Player 1\'s actions:')
    print('\tP2\'s Button A Income Rate: ' + str(round(m0_p2_a, 2)))
    print('\tP2\'s Button B Income Rate: ' + str(round(m0_p2_b, 2)))
    print('TRIAL 2: Player 2 weighs (' + str(player2.weight) + ') Player 1\'s actions:')
    print('\tP2\'s Button A Income Rate: ' + str(round(m1_p2_a, 2)))
    print('\tP2\'s Button B Income Rate: ' + str(round(m1_p2_b, 2)))
    print('TRIAL 3: Player 2 equally weighs Player 1\'s actions:')
    print('\tP2\'s Button A Income Rate: ' + str(round(m2_p2_a, 2)))
    print('\tP2\'s Button B Income Rate: ' + str(round(m2_p2_b, 2)))

    return


# Run main
if __name__ == "__main__":
    main()
