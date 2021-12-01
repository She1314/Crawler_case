from matplotlib import pyplot as plt
a = range(2, 24, 2)
b = [15, 23, 18, 23, 24, 32, 30, 28, 22, 18, 15]
plt.figure(figsize=(20, 8), dpi=60)
plt.plot(a, b)
plt.show()