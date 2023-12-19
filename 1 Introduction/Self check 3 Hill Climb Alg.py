# Self-check 3

import random


strset = 'abcdefghijklmnopqrstuvwxyz '

def random_28():
    return ''.join([random.choice(strset) for _ in range(28)])

# print(random_27())


def score_func(test):
    goal = "methinks it is like a weasel" # len(goal) = 28
    score = 0
    i = 0
    for _ in test:
        if _ == goal[i]:
            score += 1
    return(score)
    
def tries_1000():
    high_score = 0
    high_string = ''
    for i in range(1000):
        rand_str = random_28()
        if score_func(rand_str) > high_score:
            high_string = rand_str
    print(f'Score: {score_func(rand_str)}, String: {high_string}')

import string

def hill_climb_alg(test):
    goal = "methinks it is like a weasel"
    strset = string.ascii_lowercase + ' '
    itr = 0

    while test != goal:
        new_test = list(test)
        for i, char in enumerate(test):
            if char != goal[i]:
                new_test[i] = random.choice(strset)
        test = ''.join(new_test)
        itr += 1
    
    return itr

def random_28():
    strset = string.ascii_lowercase + ' '
    return ''.join(random.choice(strset) for _ in range(28))

rand_string = random_28()
print(hill_climb_alg(rand_string))
