import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimSun']  # 使用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 设置全局字体大小
matplotlib.rcParams['font.size'] = 14  # 设置字体大小为14

# 创建一个DataFrame来存储湖南2018年每月的平均高温和低温数据
data = {
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
    "平均高温": [14, 10, 20, 25, 28, 29, 37, 36, 34, 25, 22, 13],  # 根据收集到的数据填写
    "平均低温": [8, 3, 10, 17, 19, 22, 27, 26, 24, 16, 12, 4]   # 根据收集到的数据填写
}

df = pd.DataFrame(data)

# 绘制曲线图
plt.figure(figsize=(10, 6))
plt.plot(df["月份"], df["平均高温"], label="平均高温", marker='o')
plt.plot(df["月份"], df["平均低温"], label="平均低温", marker='o')
plt.xlabel("月份")
plt.ylabel("温度 (°C)")
plt.legend()
plt.grid(True)
plt.show()
