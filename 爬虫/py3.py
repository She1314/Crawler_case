def test(num):
    if num == 1:
        return 1
    else:
        return num * test(num - 1)


if __name__ == '__main__':
    sum = 0
    for i in range(1, 20):
        sum += test(i)
    print(sum)
