import math
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def W(h, u_h):
    result = 0
    if abs(u_h * h) <= h / 2:
        result = 1 / h + 1 / h * math.cos((2 * math.pi * u_h))
    return result


def J(a, h, x):
    _x = np.subtract(x, a)
    _x = np.divide(_x, h)
    sum_of_obs = 0
    for obs in _x:
        sum_of_obs += W(h, obs)
    return sum_of_obs


def kernel_density(x, h, nums, lb):
    t = np.linspace(np.amin(x) - h, np.amax(x) + h, nums)
    j_array = []
    for item in t:
        j_array.append(J(item, h, x) / (h * x.shape[0]))
    plt.plot(t, j_array, label=lb)
    return j_array


def Q1_d(df, lesson):
    df_A = df.drop(df[df['school'] != 'A'].index).reset_index(drop=True)
    df_B = df.drop(df[df['school'] != 'B'].index).reset_index(drop=True)
    df_C = df.drop(df[df['school'] != 'C'].index).reset_index(drop=True)
    kernel_density(df_A[lesson].to_numpy(), 10, 50, "School A")
    kernel_density(df_B[lesson].to_numpy(), 10, 50, "School B")
    kernel_density(df_C[lesson].to_numpy(), 10, 50, "School C")
    plot_details(lesson)


def Q1_b_test():
    #     test some variables to see witch value is best for plot
    for i in range(1, 10):
        plt.figure(i)
        kernel_density(df["math"].to_numpy(), i, 50)


def Q1_e(lesson):
    plt.figure(2)
    kernel_density(df[lesson].to_numpy(), 10, 50, "All Schools")
    plot_details( "All Schools " + lesson)

    plt.figure(3)
    Q1_d(df, lesson)


def plot_details(lesson):
    plt.title("Distribution By School For : " + lesson)
    plt.ylabel("% students")
    plt.xlabel("grade")
    plt.legend()


if __name__ == '__main__':
    lesson = "math"
    path = "C:\\Users\\Elad\\PycharmProjects\\hw2statistics\\grades.csv"
    df = pd.read_csv(path)

    plt.figure(0)
    kernel_density(df[lesson].to_numpy(), 10, 50, "All Schools ")
    plot_details("All Schools " + lesson)

    plt.figure(1)
    Q1_d(df, lesson)
    plot_details( lesson)

    lesson = "gym"
    Q1_e(lesson)
    plt.show()
