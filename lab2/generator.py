from functools import reduce
import statistics as stat
import math
from variables import *


def generate_numbers(a, r, m, numbersAmount):
    numbers = []
    for i in range(numbersAmount):
        rNew = (a * r) % m
        x = rNew / m
        r = rNew 
        numbers.append(x)
    return numbers

    
def find_expectation(numbers):
    # sum = reduce((lambda a, b: a + b), numbers)
    # return sum / len(numbers)
    return stat.mean(numbers)

    
def find_dispersion(numbers, m):
    # sum = reduce((lambda a, b: a + (b - m)*(b - m)), numbers)
    # return sum / len(numbers)
    return stat.variance(numbers)

    
def find_standard_deviation(dispersion):
    return math.sqrt(dispersion)
    

def uniform_distribution(a, b, numbersAmount):
    numbers = generate_numbers(A_VALUE, R_VALUE, M_VALYE, numbersAmount)
    distribution = []
    for i in range(numbersAmount):
        x = a + (b - a) * numbers[i]
        distribution.append(x)
    return distribution
            
            