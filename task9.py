# Pеализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time
def randomize(min, max):
    num = int(time.time_ns()/2000000)
    print(num)
    # while num > max:
    #     num /= max
    return int(num%max)

print(randomize(1,15))
print(randomize(1,20))
print(randomize(1,70))
print(randomize(1,22))








