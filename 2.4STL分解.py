import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 设置中文字体为宋体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据集
data = pd.read_csv('data.csv')

# 提取V3列作为负荷序列
load_series = data['V3']

# 设置滞后阶数
lag = 96*3

# 绘制ACF图
plt.figure(figsize=(14, 7))
ax1 = plt.subplot(211)
plot_acf(load_series, lags=lag, ax=ax1, markerfacecolor='blue', linestyle='--', color='blue')
plt.title('自相关函数 (ACF)', fontsize=16)
plt.xlabel('滞后阶数', fontsize=16)
plt.ylabel('自相关系数', fontsize=16)

# 绘制PACF图
ax2 = plt.subplot(212)
plot_pacf(load_series, lags=lag, ax=ax2, markerfacecolor='red', color='red')
plt.title('偏自相关函数 (PACF)', fontsize=16)
plt.xlabel('滞后阶数', fontsize=16)
plt.ylabel('偏自相关系数', fontsize=16)

# 显示图表
plt.tight_layout()
plt.show()
