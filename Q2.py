import math

import numpy as np


def alfa_avg(data, alfa):
    n = len(data)
    n_alfa = math.ceil(n * alfa)
    summ = sum(data[n_alfa:n - n_alfa])
    # for i in range(n_alfa, n - n_alfa):
    #     summ += data[i]
    return summ / (n - 2 * n_alfa)


# test = (69 + 84 + 88 + 92) / 4
# data2 = [1, 2, 4, 4, 5, 6, 7, 8]

def Q2(data):
    n = len(data)
    avarage = sum(data) / n
    print("Q2_a sol is : " + str(avarage))

    data.sort()
    print(data)

    alfa_avg1 = alfa_avg(data, 0.2)

    print("Q2_b sol is : " + str(alfa_avg1))

    median = data[math.ceil(0.5 * n) - 1]
    print("Q2_c sol is : " + str(median))

    p65 = data[math.ceil(0.65 * n) - 1]
    print("Q2_d sol is : " + str(p65))


if __name__ == '__main__':
    data_a = [100, 84, 88, 96, 0, 69, 38, 92]
    data_b = [100, 84, 88, 96, 0, 69, 38, 200]
    print("q2 a \n")
    Q2(data_a)
    print("q2 b \n")
    Q2(data_b)