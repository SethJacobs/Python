
import math


def euler(n):
    result = n

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:

            while n % i == 0:
                n = int(n / i)
            result = result - int(result / i)
    if n != 1:
        result = result - int(result / n)
    return result


