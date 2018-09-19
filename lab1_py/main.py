import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from generator import *
from tkinter import *
from variables import *


def show_chart(root, numbers):
    minValue = min(numbers)
    maxValue = max(numbers)
    
    numbersRange = maxValue - minValue
    barLength = numbersRange / BARS_IN_CHART
    
    frequencies = []
    intervals = []
    minBoundary = minValue
    maxBoundary = minBoundary + barLength
    
    for i in range(BARS_IN_CHART):
        numbersInInterval = list(filter(lambda number: number >= minBoundary and number < maxBoundary, numbers))
        frequency = len(numbersInInterval) / len(numbers)
        frequencies.append(frequency)
        intervals.append(minBoundary)
        minBoundary += barLength
        maxBoundary += barLength
    
    figure = Figure(figsize = (6, 4), dpi = 100)
    a = figure.add_subplot(111)
    a.bar(intervals, frequencies, barLength, color = '#90CAF9', edgecolor = '#1976D2')
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.show()
    canvas.get_tk_widget().place(x = 200, y = 10)


def start_algorithm(root, a, r, m, numbersAmount):
    numbers = generate_numbers(a, r, m, numbersAmount)
    print(numbers)
    
    expectation = find_expectation(numbers)
    dispersion = find_dispersion(numbers, expectation)
    standard_deviation = find_standard_deviation(dispersion)
    period = find_period(numbers)
    aperiodic_interval = find_aperiodic_interval(numbers, period)
    
    show_chart(root, numbers)
    
    expectation_label = Label(root, text = "Мат. Ожидание: " + str(round(expectation, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 420)
    dispersion_label = Label(root, text = "Дисперсия: " + str(round(dispersion, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 440)
    standard_deviation_label = Label(root, text = "Среднеквадратическое отклонение: " + str(round(standard_deviation, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 460)
    period_label = Label(root, text = "Период: " + str(round(period, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 480)
    aperiodic_interval_label = Label(root, text = "Длина отрезка апериодичности: " + str(round(aperiodic_interval, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 500)

def initialize_window():
    root = Tk()
    root.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

    a_value_label = Label(root, text = "Параметр а").place(x = 10, y = 10)
    a_value_input = Entry(root)
    a_value_input.place(x = 10, y = 30)
    
    r_value_label = Label(root, text = "Параметр r").place(x = 10, y = 60)
    r_value_input = Entry(root)
    r_value_input.place(x = 10, y = 80)
    
    m_value_label = Label(root, text = "Параметр m").place(x = 10, y = 110)
    m_value_input = Entry(root)
    m_value_input.place(x = 10, y = 130)
    
    n_value_label = Label(root, text = "Количество чисел").place(x = 10, y = 160)
    n_value_input = Entry(root)
    n_value_input.place(x = 10, y = 180)
    
    start_button = Button(root, text = "Начать", width = 10,
        command = lambda: start_algorithm(root, int(a_value_input.get()), int(r_value_input.get()), int(m_value_input.get()), int(n_value_input.get())))
    start_button.place(x = 10, y = 210)

    root.mainloop()


def main():
    initialize_window();

if __name__ == "__main__":
    main()
