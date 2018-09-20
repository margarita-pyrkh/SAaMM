import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from functools import reduce
import math
from generator import *
from tkinter import *
from tkinter.ttk import *
from variables import *


def show_results(page, distribution):
    expectation = find_expectation(distribution)
    dispersion = find_dispersion(distribution, expectation)
    standard_deviation = find_standard_deviation(dispersion)
    
    expectation_label = Label(page, text = "Мат. Ожидание: " + str(round(expectation, 3)), width = 25, anchor = 'w').place(x = 10, y = 200)
    dispersion_label = Label(page, text = "Дисперсия: " + str(round(dispersion, 3)), width = 25, anchor = 'w').place(x = 10, y = 230)
    standard_deviation_label = Label(page, text = "Среднекв. отклонение: " + str(round(standard_deviation, 3)), width = 25, anchor = 'w').place(x = 10, y = 260)

def show_chart(page, distribution):
    minValue = min(distribution)
    maxValue = max(distribution)

    numbersRange = maxValue - minValue
    barLength = numbersRange / BARS_IN_CHART

    frequencies = []
    intervals = []
    minBoundary = minValue
    maxBoundary = minBoundary + barLength

    for i in range(BARS_IN_CHART):
        numbersInInterval = list(filter(lambda number: number >= minBoundary and number < maxBoundary, distribution))
        frequency = len(numbersInInterval) / len(distribution)
        frequencies.append(frequency)
        intervals.append(minBoundary)
        minBoundary += barLength
        maxBoundary += barLength

    figure = Figure(figsize = (5, 4), dpi = 100)
    a = figure.add_subplot(111)
    a.bar(intervals, frequencies, barLength, color = '#90CAF9', edgecolor = '#1976D2')
    canvas = FigureCanvasTkAgg(figure, page)
    canvas.show()
    canvas.get_tk_widget().place(x = 250, y = 10)


def uniform_algorithm(page, a, b, numbersAmount):
    numbers = generate_numbers(A_VALUE, R_VALUE, M_VALYE, numbersAmount)
    distribution = []
    for i in range(numbersAmount):
        x = a + (b - a) * numbers[i]
        distribution.append(x)
    show_chart(page, distribution)
    show_results(page, distribution)
    

def gaussian_algorithm(page, mx, sigma, numbersAmount):
    N = 6
    numbers = generate_numbers(A_VALUE, R_VALUE, M_VALYE, numbersAmount * N)
    distribution = []
    for i in range(numbersAmount):
        sub_numbers = numbers[i:i + N]
        print(sub_numbers)
        x = mx + sigma * math.sqrt(12 / numbersAmount) * reduce((lambda a, b: a + (b - numbersAmount / 2)), sub_numbers)
        distribution.append(x)
    show_chart(page, distribution)
    show_results(page, distribution)
    
    
def exponential_algorithm(page, lambdaValue, numbersAmount):
    return 0;

def initialize_window():
    root = Tk()
    root.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    
    notebook = Notebook(root)
    page1 = Frame(notebook, width = 850, height = 530)
    page2 = Frame(notebook, width = 850, height = 530)
    page3 = Frame(notebook, width = 850, height = 530)
    page4 = Frame(notebook, width = 850, height = 530)
    page5 = Frame(notebook, width = 850, height = 530)
    page6 = Frame(notebook, width = 850, height = 530)
    notebook.add(page1, text = "Равномерное")
    notebook.add(page2, text = "Гауссовское")
    notebook.add(page3, text = "Экспоненциальное")
    notebook.add(page4, text = "Гамма")
    notebook.add(page5, text = "Треугольное")
    notebook.add(page6, text = "Симпсона")
    notebook.pack()

    uniform_distribution_label = Label(page1, text = "Равномерное распределение").place(x = 10, y = 10)
    a_value_label = Label(page1, text = "Параметр а").place(x = 10, y = 40)
    a_value_input = Entry(page1, width = 10)
    a_value_input.place(x = 110, y = 40)
    
    b_value_label = Label(page1, text = "Параметр b").place(x = 10, y = 70)
    b_value_input = Entry(page1, width = 10)
    b_value_input.place(x = 110, y = 70)
    
    n_value_label = Label(page1, text = "Количество N").place(x = 10, y = 100)
    n_value_input = Entry(page1, width = 10)
    n_value_input.place(x = 110, y = 100)
    
    uniform_button = Button(page1, text = "Рассчитать", width = 19,
        command = lambda: uniform_algorithm(page1, int(a_value_input.get()), int(b_value_input.get()), int(n_value_input.get())))
    uniform_button.place(x = 10, y = 130)
    
    
    gaussian_distribution_label = Label(page2, text = "Гауссовское распределение").place(x = 10, y = 10)
    mx_value_label = Label(page2, text = "Параметр m(x)").place(x = 10, y = 40)
    mx_value_input = Entry(page2, width = 10)
    mx_value_input.place(x = 110, y = 40)
    
    sigma_label = Label(page2, text = "Параметр σ(x)").place(x = 10, y = 70)
    sigma_input = Entry(page2, width = 10)
    sigma_input.place(x = 110, y = 70)
    
    gaussian_n_label = Label(page2, text = "Количество N").place(x = 10, y = 100)
    gaussian_n_input = Entry(page2, width = 10)
    gaussian_n_input.place(x = 110, y = 100)
    
    gaussian_button = Button(page2, text = "Рассчитать", width = 19,
        command = lambda: gaussian_algorithm(page2, int(mx_value_input.get()), float(sigma_input.get()), int(gaussian_n_input.get())))
    gaussian_button.place(x = 10, y = 130)
    
    
    exponential_distribution_label = Label(page3, text = "Экспоненциальное распределение").place(x = 10, y = 10)
    lambda_value_label = Label(page3, text = "Параметр λ").place(x = 10, y = 40)
    lambda_value_input = Entry(page3, width = 10)
    lambda_value_input.place(x = 110, y = 40)
    
    exponential_n_label = Label(page3, text = "Количество N").place(x = 10, y = 70)
    exponential_n_input = Entry(page3, width = 10)
    exponential_n_input.place(x = 110, y = 70)
    
    exponential_button = Button(page3, text = "Рассчитать", width = 19,
        command = lambda: exponential_algorithm(page3, int(lambda_value_input.get()), float(exponential_n_input.get())))
    exponential_button.place(x = 10, y = 100)

    root.mainloop()


def main():
    initialize_window();

if __name__ == "__main__":
    main()
