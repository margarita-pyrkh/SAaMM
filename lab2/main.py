import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from generator import *
from tkinter import *
from variables import *


def show_results(root, distribution, y):
    expectation = find_expectation(distribution)
    dispersion = find_dispersion(distribution, expectation)
    standard_deviation = find_standard_deviation(dispersion)
    
    expectation_label = Label(root, text = "Мат. Ожидание: " + str(round(expectation, 3)), height = 1, width = 25, anchor = 'w').place(x = 10, y = y)
    dispersion_label = Label(root, text = "Дисперсия: " + str(round(dispersion, 3)), height = 1, width = 25, anchor = 'w').place(x = 10, y = y + 30)
    standard_deviation_label = Label(root, text = "Среднекв. отклонение: " + str(round(standard_deviation, 3)), height = 1, width = 25, anchor = 'w').place(x = 10, y = y + 60)

def show_chart(root, distribution, y):
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

    figure = Figure(figsize = (5, 3), dpi = 100)
    a = figure.add_subplot(111)
    a.bar(intervals, frequencies, barLength, color = '#90CAF9', edgecolor = '#1976D2')
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.show()
    canvas.get_tk_widget().place(x = 250, y = y)


def uniform_algorithm(root, a, b, numbersAmount):
    numbers = generate_numbers(A_VALUE, R_VALUE, M_VALYE, NUMBERS_AMOUNT)
    distribution = []
    for i in range(numbersAmount):
        x = a + (b - a) * numbers[i]
        distribution.append(x)
    show_chart(root, distribution, y = 10)
    show_results(root, distribution, y = 200)
    

# def gaussian_algorithm(root, ):
    

def initialize_window():
    root = Tk()
    root.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    
    scrollbar = Scrollbar(root)
    scrollbar.pack(side = RIGHT, fill = Y)

    uniform_distribution_label = Label(root, text = "Равномерное распределение").place(x = 10, y = 10)
    a_value_label = Label(root, text = "Параметр а").place(x = 10, y = 40)
    a_value_input = Entry(root, width = 10)
    a_value_input.place(x = 100, y = 40)
    
    b_value_label = Label(root, text = "Параметр b").place(x = 10, y = 70)
    b_value_input = Entry(root, width = 10)
    b_value_input.place(x = 100, y = 70)
    
    n_value_label = Label(root, text = "Количество").place(x = 10, y = 100)
    n_value_input = Entry(root, width = 10)
    n_value_input.place(x = 100, y = 100)
    
    uniform_button = Button(root, text = "Рассчитать", width = 19,
        command = lambda: uniform_algorithm(root, int(a_value_input.get()), int(b_value_input.get()), int(n_value_input.get())))
    uniform_button.place(x = 10, y = 130)

    root.mainloop()


def main():
    initialize_window();

if __name__ == "__main__":
    main()
