import matplotlib
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontManager

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)


# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

matplotlib.matplotlib_fname()

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# 设置图标标题并给坐标轴系上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("-值", fontsize=24)
ax.set_ylabel("值的平方", fontsize=24)

# 设置刻度标记的大小
ax.tick_params(axis="both", labelsize=14)

plt.show()
