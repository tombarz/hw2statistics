# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
def W(h, u_h):
    result = 0
    if abs(u_h*h) <= h / 2:
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
    t = np.linspace(np.amin(x) - h, np.amax(x) + h,nums)
    j_array = []
    for item in t:
        j_array.append(J(item, h, x)/(h*x.size))
    plt.plot(t,j_array, label=lb)
    #plt.show()
    return j_array

def Q1_d(df):
    df_A = df.drop(df[df['school'] != 'A'].index).reset_index(drop=True)
    df_B = df.drop(df[df['school'] != 'B'].index).reset_index(drop=True)
    df_C = df.drop(df[df['school'] != 'C'].index).reset_index(drop=True)
    kernel_density(df_A["math"].to_numpy(), 10, 50,"A")
    kernel_density(df_B["math"].to_numpy(), 10, 50,"B")
    kernel_density(df_C["math"].to_numpy(), 10, 50,"C")

if __name__ == '__main__':
    #print(kernel_density(np.array([1, 2, 3, 4, 5]), 1 , 30))
    path = "C:\\Users\\tom_b\\Desktop\\University\\סטטיסטיקה למדעי המחשב\\מטלות\\pythonProject\\grades.csv"
    df = pd.read_csv(path)
    Q1_d(df)
    window_size = 0
    #  for i in range(1,10):
    #     plt.figure(i)
    #     kernel_density(df["math"].to_numpy(),i,50)
    plt.legend()
    plt.show()
