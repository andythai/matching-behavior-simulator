# Andy Thai
# June 2017
import random


# Class to hold player information and functions
class Player:
    # Constructor
    def __init__(self, p, m, w, prob_button_a, prob_button_b):
        self.player = p
        # mode:
        # 0: no weight
        # 1: unequal weighting
        # 2: equal weighting
        self.mode = m
        # How much weight to put on partner's actions
        self.weight = w
        self.prob_a = prob_button_a
        self.prob_b = prob_button_b
        self.score_a = 0
        self.score_b = 0
        self.score_total = 0
        self.times_picked_a = 0
        self.times_picked_b = 0
        self.history = [('A', True), ('B', True), ('A', False), ('B', False)]
        self.other_player = None

    # Calculate matching ratios
    def calc_matching(self):
        # Calculate ratios
        if self.mode == 0:      # Only factors own actions
            a_ratio = (self.score_a + 1) / (self.times_picked_a + 2)
            b_ratio = (self.score_b + 1) / (self.times_picked_b + 2)
        elif self.mode == 1:    # Factors partner's actions based on a weight
            a_ratio = (self.score_a * (1 - self.weight) + self.other_player.score_a * self.weight + 2) / \
                      (self.times_picked_a * (1 - self.weight) + self.other_player.times_picked_a * self.weight + 4)
            b_ratio = (self.score_b * (1 - self.weight) + self.other_player.score_b * self.weight + 2) / \
                      (self.times_picked_b * (1 - self.weight) + self.other_player.times_picked_b * self.weight + 4)
        elif self.mode == 2:    # Factors partner's action equally
            a_ratio = (self.score_a * 0.5 + self.other_player.score_a * 0.5 + 2) / \
                      (self.times_picked_a * 0.5 + self.other_player.times_picked_a * 0.5 + 4)
            b_ratio = (self.score_b * 0.5 + self.other_player.score_b * 0.5 + 2) / \
                      (self.times_picked_b * 0.5 + self.other_player.times_picked_b * 0.5 + 4)

        matching_a = a_ratio / (a_ratio + b_ratio)
        matching_b = b_ratio / (a_ratio + b_ratio)
        # Return normalized ratio for probabilistic choices
        return matching_a, matching_b

    # Player picks a button
    def pick_button(self, button):
        # Choose button A
        if button == 'A':
            self.times_picked_a = self.times_picked_a + 1
            if random.random() < self.prob_a:
                self.score_a = self.score_a + 1
                self.score_total = self.score_total + 1
                self.history.append(('A', True))
            else:
                self.history.append(('A', False))
        # Choose button B
        else:
            self.times_picked_b = self.times_picked_b + 1
            if random.random() < self.prob_b:
                self.score_b = self.score_b + 1
                self.score_total = self.score_total + 1
                self.history.append(('B', True))
            else:
                self.history.append(('B', False))
        return
