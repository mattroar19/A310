# -*- coding: utf-8 -*-

from itertools import product

# --------------------------------------------------
# Helper function to compute probability
# --------------------------------------------------
def compute_event_probability(event_condition, sample_space):
    successful_outcomes = 0
    total_weight = 0

    # Case 1: weighted sample space stored as a dictionary
    if isinstance(sample_space, dict):
        for outcome, weight in sample_space.items():
            total_weight += weight
            if event_condition(outcome):
                successful_outcomes += weight

    # Case 2: regular sample space stored as a list/set/tuple
    else:
        for outcome in sample_space:
            total_weight += 1
            if event_condition(outcome):
                successful_outcomes += 1

    return successful_outcomes / total_weight


# --------------------------------------------------
# 1(a) Sample space for a fair coin
# --------------------------------------------------
sample_space = {'Heads', 'Tails'}
print("Fair coin sample space:", sample_space)


# --------------------------------------------------
# 1(b) Weighted sample space for a biased coin
# Tails occurs 3 times more often than Heads
# --------------------------------------------------
weighted_sample_space = {'Tails': 3, 'Heads': 1}
print("Biased coin weighted sample space:", weighted_sample_space)


# --------------------------------------------------
# 1(c) Calculate probability of each elementary event
# --------------------------------------------------
def is_heads(outcome):
    return outcome == 'Heads'

def is_tails(outcome):
    return outcome == 'Tails'

event_conditions = [is_heads, is_tails]

for event_condition in event_conditions:
    prob = compute_event_probability(event_condition, weighted_sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name}' is {prob}")


# --------------------------------------------------
# 2. Four fair coins: probability of exactly 2 heads
# --------------------------------------------------
four_coin_sample_space = list(product(['Heads', 'Tails'], repeat=4))

def is_balanced(outcome):
    return outcome.count("Heads") == 2

prob = compute_event_probability(is_balanced, four_coin_sample_space)
print(f"Probability of exactly 2 heads in 4 flips is {prob}")


# --------------------------------------------------
# 3. Eight die rolls sum to 28
# --------------------------------------------------
die_sample_space = list(product([1, 2, 3, 4, 5, 6], repeat=8))

def has_sum_of_28(outcome):
    return sum(outcome) == 28

prob = compute_event_probability(has_sum_of_28, die_sample_space)
print(f"8 rolls sum to 28 with a probability of {prob}")


# --------------------------------------------------
# 4. Eight die rolls sum between 14 and 24 inclusive
# --------------------------------------------------
def is_in_interval(number, minimum, maximum):
    return minimum <= number <= maximum

prob = compute_event_probability(
    lambda x: is_in_interval(sum(x), 14, 24),
    die_sample_space
)
print(f"Probability that 8 rolls sum to between 14 and 24 is {prob}")


# --------------------------------------------------
# 5. Probability that 10 fair coin flips do NOT produce 3 to 7 heads
# --------------------------------------------------
ten_coin_sample_space = list(product(['Heads', 'Tails'], repeat=10))

prob = compute_event_probability(
    lambda x: not is_in_interval(x.count("Heads"), 3, 7),
    ten_coin_sample_space
)
print(f"Probability that 10 flips do NOT produce between 3 and 7 heads is {prob}")


# --------------------------------------------------
# 6. Probability that 20 fair coin flips do NOT produce 5 to 15 heads
# --------------------------------------------------
twenty_coin_sample_space = list(product(['Heads', 'Tails'], repeat=20))

prob = compute_event_probability(
    lambda x: not is_in_interval(x.count("Heads"), 5, 15),
    twenty_coin_sample_space
)
print(f"Probability that 20 flips do NOT produce between 5 and 15 heads is {prob}")
