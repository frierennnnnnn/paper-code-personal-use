import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import MSTL

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 数据加载与预处理（保持不变）
data = pd.read_csv('data.csv', parse_dates=['timestamp'], index_col='timestamp')
data = data.resample('15T').asfreq()
data['V3'] = data['V3'].interpolate()

# 关键修改点：调整周期为奇数，并指定窗口参数
mstl = MSTL(
    data['V3'],
    periods=(97, 673),          # 日周期97（原96+1），周周期673（原672+1）
    windows=(11, 15),           # 季节性平滑窗口（必须为奇数，如11和15）
    lmbda=None,
    iterate=3                   # 鲁棒性迭代次数增加
)
mstl_result = mstl.fit()

# 可视化与分析代码（保持不变）
plt.figure(figsize=(14, 10))
plt.subplot(5, 1, 1)
plt.plot(mstl_result.observed)
plt.title('原始时间序列')

plt.subplot(5, 1, 2)
plt.plot(mstl_result.trend)
plt.title('趋势成分')

plt.subplot(5, 1, 3)
plt.plot(mstl_result.seasonal['seasonal_97'])  # 注意键名随周期改变
plt.title('日季节性成分 (周期=97)')

plt.subplot(5, 1, 4)
plt.plot(mstl_result.seasonal['seasonal_673'])
plt.title('周季节性成分 (周期=673)')

plt.subplot(5, 1, 5)
plt.plot(mstl_result.resid)
plt.title('残差成分')

plt.tight_layout()
plt.show()

# 成分强度计算（需同步修改键名）
def component_strength(resid, component):
    total_variance = (component + resid).var()
    return max(0, 1 - resid.var() / total_variance) if total_variance !=0 else 0

seasonal_day_strength = component_strength(
    mstl_result.resid,
    mstl_result.seasonal['seasonal_97']
)
seasonal_week_strength = component_strength(
    mstl_result.resid,
    mstl_result.seasonal['seasonal_673']
)
trend_strength = component_strength(
    mstl_result.resid,
    mstl_result.trend
)

print(f"\n[成分强度评估]")
print(f"日季节性强度: {seasonal_day_strength:.4f}")
print(f"周季节性强度: {seasonal_week_strength:.4f}")
print(f"趋势强度: {trend_strength:.4f}")