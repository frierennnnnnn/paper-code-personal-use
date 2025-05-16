import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# 设置matplotlib支持中文
plt.rcParams['font.sans-serif'] = ['SimSun']  # 使用中文默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 加载数据集
data = pd.read_csv('data.csv')

# 假设V3列是我们要绘制的数据
v3data = data['V3'].values

# 定义每段的时间步长
stepsize = 96

# 创建图形和轴
fig, ax = plt.subplots()

# 遍历数据，每96个时间步画一条曲线
for i in range(0, len(v3data) - stepsize + 1, stepsize):
    # 提取每96个时间步的数据
    segment = v3data[i:i + stepsize]
    # 随机选择颜色
    color = random.choice(plt.cm.tab20.colors)
    # 绘制折线图，使用随机颜色
    ax.plot(segment, color=color)

# 设置横轴和纵轴标签，并调大字体大小
ax.set_xlabel('时间步', fontsize=14)
ax.set_ylabel('负荷（kW）', fontsize=14)

# 设置横轴的范围
ax.set_xlim(0, stepsize - 1)


# 调整数字大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 显示图形
plt.show()
