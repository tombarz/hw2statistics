from scipy.stats import poisson
from scipy.stats import geom
lamb = 20


# Q3_A_1
def smaller_then(small):
    i = 0
    while poisson.cdf(i, lamb) < small:
        i += 1
    return i


# Q3_A_1
def lerger_then(large):
    i = 0
    # Q3_A_2
    while poisson.cdf(i, lamb) < 1 - large:
        i += 1
    return i


if __name__ == '__main__':
    x = smaller_then(0.9)
    print("the index is : " + str(x) + " and the probability of a lower number is : " + str(poisson.cdf(x, lamb)))
    x = lerger_then(0.9)
    print("the index is : " + str(x - 1) + " and the probability of a larger number is : " + str(
        1 - poisson.cdf(x - 1, lamb)))

    first_q = smaller_then(0.25)
    last_q = lerger_then(0.25)
    IQR = poisson.cdf(last_q, lamb) - poisson.cdf(first_q, lamb)
    print("the IQR is : " + str(IQR))

    less_then_16 = poisson.cdf(16, lamb)
    print("the probability for up to 16 new sick people is : p = " + str(less_then_16))

    print("the expected value : " + str(1/less_then_16))

    start = 0
    while geom.cdf(start, less_then_16) < 0.5:
        start += 1
    end = 0
    while geom.cdf(end, less_then_16) < 0.75:
        end += 1
    print(geom.cdf(end, less_then_16) - geom.cdf(start, less_then_16))