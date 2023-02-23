import random
import numpy as np
import prairielearn as pl

def gen_random_list(list_length, min_range, max_range):
    input_list = set()
    while len(input_list) < list_length:
        input_list.add(random.randint(min_range, max_range + 1))
    return random.sample(list(input_list), len(input_list))

def gen_list(list_length, min_range, max_range):
    randomized = gen_random_list(list_length, min_range, max_range)
    max_k = calculate_k(randomized)
    return (randomized, max_k)

def calculate_k(input_list):
    sorted_input_dict = dict()
    for i, value in enumerate(sorted(input_list)):
        sorted_input_dict[value] = i
    max_k = 0
    for i in range(len(input_list)):
        max_k = max(max_k, abs(i - sorted_input_dict[input_list[i]]))
    return max_k

def gen_list_k(list_length, min_range, max_range, goal_k):
    input_list, cur_k = gen_list(list_length, min_range, max_range)    
    while cur_k != goal_k:
        input_list, cur_k = gen_list(list_length, min_range, max_range)
    return input_list


def grade(data):
    q2_answer = data["submitted_answers"]["OutputList2"]["_value"][0]
    sorted_q2_k = calculate_k(q2_answer)
    if sorted_q2_k <= int(data["params"]["k_2"]):
        data["partial_scores"]["OutputList2"]["score"] = 1
    else:
        data["partial_scores"]["OutputList2"]["score"] = 0

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    list_length = 6
    min_range, max_range = 0, 10
    goal_k = 3

    input_list = gen_list_k(list_length, min_range, max_range, goal_k)
    
    data["params"]["input_list_1"] = str(input_list)
    data["params"]["k_1"] = str(goal_k)

    # Put the sum into data['correct_answers']
    
    #for part 1 of this question
    mat = np.array(sorted(input_list)).reshape((1,len(input_list)))
    data["correct_answers"]["OutputList1"] = pl.to_json(mat)
    
    #for part 2 os this question
    random_length_2 = random.randint(4, 7)
    random_k_2 = random.randint(0, random_length_2 - 2)

    data["params"]["input_list_2_length"] = str(random_length_2)
    data["params"]["k_2"] = str(random_k_2)

    mat2 = np.random.random((1,random_length_2))
    data["correct_answers"]["OutputList2"] = pl.to_json(mat2)
    
    #for part 3
    input_list_3 = gen_random_list(list_length, min_range, max_range)
    data["params"]["input_list_3"] = str(input_list_3)
    data["correct_answers"]["Output3"] = calculate_k(input_list_3)
