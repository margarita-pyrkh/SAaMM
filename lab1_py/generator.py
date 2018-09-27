from functools import reduce
import statistics as stat
import math


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
    

def find_period(numbers):
    compareValue = numbers[len(numbers) - 1]
    firstIndex = numbers.index(compareValue)
    try:
        secondIndex = numbers.index(compareValue, firstIndex + 1)
    except ValueError:
        return len(numbers) - firstIndex
    return secondIndex - firstIndex
    
    
def find_aperiodic_interval(numbers, period):
    for i in range(len(numbers)):
        if i + period < len(numbers):
            if numbers[i] == numbers[i + period]:
                return i + period
        else:
            return period    
            
def find_indirect_indications(numbers):
    count = 0;
    for i in range(0, len(numbers), 2):
        if math.pow(numbers[i], 2) + math.pow(numbers[i + 1], 2) < 1 :
            count += 1;
    return count * 2 / len(numbers)