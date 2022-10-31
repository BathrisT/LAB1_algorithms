import gc
import random
import time
import timeit

from alg1_bin_search import bin_search
from alg2_linear_search import linear_search
from alg3_exp_search import exp_search

def create_matrix(x, fill_type=1):
    n = 2**13
    m = 2**x
    matrix = None
    if fill_type == 1:
        matrix = [[((n//m*i + j) * 2) for j in range(n)] for i in range(m)]
    elif fill_type == 2:
        #matrix = [[((n // m * i * j) * 2) for j in range(n)] for i in range(m)]
        matrix = [[(n * i * j * 2 / m) for j in range(n)] for i in range(m)]
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def timeit_and_exec(func, args: list = list()):
    gc.disable()
    t = time.time_ns()
    ans = func(args[0], args[1])
    t2 = time.time_ns() - t
    gc.enable()
    return {"execution_time": t2,
            "function": func.__name__,
            "answer": ans}

def timeit_and_exec_v2(func, args: list = list()):
    c = globals().copy()
    c['args'] = args
    t = timeit.timeit(f"{func.__name__}(*args)", globals=c)
    print(t)
    return {"execution_time": t,
            "function": func.__name__}


def get_median_execution_time_of_function(func, args, repeat=150):
    s = 0
    d = 0
    for i in range(repeat):
        t = timeit_and_exec(func, args)['execution_time']
        if t != 0:
            s += t
            d += 1
    if d == 0: d = 1
    return s//d

def get_median_search_time_in_matrix_by_algorithms(matrix_size, matrix_type=1):
    N = 2 ** matrix_size
    matrix = create_matrix(matrix_size, fill_type=matrix_type)
    if matrix_type == 1: target = 2 * N + 1
    elif matrix_type == 2: target = 16 * N + 1
    bin_search_time = get_median_execution_time_of_function(bin_search, [matrix, target])
    linear_search_time = get_median_execution_time_of_function(linear_search, [matrix, target])
    exp_search_time = get_median_execution_time_of_function(exp_search, [matrix, target])
    return {
        "bin_search_time": bin_search_time,
        "linear_search_time": linear_search_time,
        "exp_search_time": exp_search_time
    }

def check_correctness_of_algorithms():
    matrix_size = 13
    matrix_type = 2
    N = 2 ** matrix_size
    matrix = create_matrix(matrix_size, fill_type=matrix_type)
    print(len(matrix), len(matrix[0]))
    while True:
        target = random.choice(random.choice(matrix[12:]))+random.randint(0, 1)+1
        bin_search_ans = timeit_and_exec(bin_search, [matrix, target])['answer']
        linear_search_ans = timeit_and_exec(linear_search, [matrix, target])['answer']
        exp_search_ans = timeit_and_exec(exp_search, [matrix, target])['answer']
        if bin_search_ans == linear_search_ans == exp_search_ans:
            print(f"TARGET {target} OK! ANS: {exp_search_ans}")
        else:
            print(f"\n\nERROR: TARGET {target} ANS1: {bin_search_ans} ANS2: {linear_search_ans} ANS3: {exp_search_ans}\n\n")

if __name__ == '__main__':
    #check_correctness_of_algorithms()
    f = open("data.txt", "w+")
    s = "ROWS\tBINARY\tLINEAR\tEXP1\tEXP2\tEXP1/EXP2\n"
    for i in range(1, 14):
        timings = get_median_search_time_in_matrix_by_algorithms(i)
        timings2 = get_median_search_time_in_matrix_by_algorithms(i, 2)
        print(f"Matrix generation 2^{i} x 2^13\n"
              f"BINARY SEARCH: {timings['bin_search_time']}\n"
              f"LINEAR SEARCH: {timings['linear_search_time']}\n"
              f"  EXP1 SEARCH: {timings['exp_search_time']}\n"
              f"  EXP2 SEARCH: {timings2['exp_search_time']}\n")
        s += f"2^{i}\t{timings['bin_search_time']}\t{timings['linear_search_time']}\t{timings['exp_search_time']}\t{timings2['exp_search_time']}\t"
        if float(timings2['exp_search_time']) == 0: s += "0" + "\n"
        else: s += "\n"
    f.write(s.replace(".", ","))
    f.close()