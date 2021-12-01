# import random
# nums = [random.randint(10, 99) for i in range(10, 100)]
# statistics = {n: 0 for n in range(10)}
# num = 0
# print(statistics)
# for count, j in enumerate(nums):
#     for k in range(2, 11):
#         if j % k == random.randint(0, 9):
#             num = num + 1
#             if num % 10 == 0:
#                 print()
#             else:
#                 print(f"{j}", end=' ')


# 方法二:
import random


def fun():
    random_list = [random.randint(10, 99) for i in range(100)]
    statics = {n: 0 for n in range(10)}
    for index, x in enumerate(random_list):
        print(x, end=' ')
        statics[int(x % 10)] = statics[int(x % 10)] + 1
        if (index + 1) % 10 == 0:
            print()
    print(statics)
if __name__ == '__main__':
    fun()
