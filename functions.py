from data import *

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e


def find_extrem_x():
    extremum_x = []
    for i in np.arange(range_start, range_end, step):
        if np.abs(f(i-step)) < np.abs(f(i)) > np.abs(f(i+step)):
            extremum_x.append(i)
    return extremum_x


def find_extrem_y(x):
    extremum_y = []
    for i in range(len(x)):
        extremum_y.append(f(x[i]))
    return extremum_y


def get_roots(x):
    roots = []
    for i in np.arange(x[0],x[len(x)-1],step):
        if np.abs(f(i-step)) > np.abs(f(i)) < np.abs(f(i+step)):
            roots.append(i)
    return roots


def print_exrem(x,y):

    for i in range(1,len(x)):
        plt.plot(x[i], y[i], 'gx', markersize=8,markeredgewidth=1)
    plt.plot(x[0], y[0], 'gx', label = 'Экстремумы', markersize=8,markeredgewidth=1)


def print_roots(roots):
    for i in range(1, len(roots)):
        plt.plot(roots[i], 0, 'ro', markersize=8)
    plt.plot(roots[0], 0, 'ro', label='Корни уравнения', markersize=8)


def prin_function():
    x_up_positive = []
    x_up_negative = []
    x_down_positive = []
    x_down_negative = []
    for i in np.arange(range_start, range_end, step):

        if np.abs(f(i - step)) < np.abs(f(i)) < np.abs(f(i + step)) and f(i) > 0:
            x_up_negative = []
            x_up_positive.append(i)
            x_up_pos = np.array(x_up_positive)
            plt.plot(x_up_pos, f(x_up_pos), 'r')

        elif np.abs(f(i - step)) > np.abs(f(i)) > np.abs(f(i + step)) and f(i) > 0:
            x_up_positive = []
            x_down_positive.append(i)
            x_dw_pos = np.array(x_down_positive)
            plt.plot(x_dw_pos, f(x_dw_pos), 'b')
        elif np.abs(f(i - step)) < np.abs(f(i)) < np.abs(f(i + step)) and f(i) < 0:
            x_down_positive = []
            x_down_negative.append(i)
            x_dw_neg = np.array(x_down_negative)
            plt.plot(x_dw_neg, f(x_dw_neg), '--b')
        elif np.abs(f(i - step)) > np.abs(f(i)) > np.abs(f(i + step)) and f(i) < 0:
            x_down_negative = []
            x_up_negative.append(i)
            x_up_neg = np.array(x_up_negative)
            plt.plot(x_up_neg, f(x_up_neg), '--r')

    # Здесь костыльнем для записи Легенды

    plt.plot(x_up_pos[0], f(x_up_pos[0]), 'r', label='Функция возрастает и больше нуля')
    plt.plot(x_dw_pos[0], f(x_dw_pos[0]), 'b', label='Функция убывает и больше нуля')
    plt.plot(x_dw_neg[0], f(x_dw_neg[0]), '--b', label='Функция убывает и меньше нуля')
    plt.plot(x_up_neg[0], f(x_up_neg[0]), '--r', label='Функция возрастает и меньше нуля')