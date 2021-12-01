from matplotlib import pyplot as plt
from matplotlib import font_manager

my_foot = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STFANGSO.TTF')
x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
plt.figure(figsize=(20, 8), dpi=60)
plt.plot(x, y)

_x_labels = [f"{i}岁" for i in x]
plt.xticks(x, _x_labels, rotation=45, fontproperties=my_foot)

plt.xlabel("year(岁)", fontproperties=my_foot)
plt.grid()
plt.show()
