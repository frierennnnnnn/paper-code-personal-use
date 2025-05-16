import numpy as np
import pandas as pd
from relieff import RReliefF

# 1. 准备数据
data = pd.read_csv('test.csv')
X = data[['V1','V2','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','Temperature(F)', 'Dew Point(F)', 'Humidity(%)', 'Wind Speed(mph)', 'Wind Gust(mph)', 'Pressure(in)', 'Condition_Cloudy', 'Condition_Extreme', 'Condition_Fair', 'Condition_Other', 'Condition_Rain']].values
y = data['V3'].values
print("X:", X)
print("y:", y)

# 2. 运行 RReliefF 算法，假设 T2M_toc 是离散变量
categorical_features = [0, 1, 3, 7, 10, 13, 19, 21, 22, 23, 24, 25]  # 离散变量的列索引
W_A, Wtrack, iTrack = RReliefF(X, y, weight_track=True, categorical_features=categorical_features)

print("特征权重 W_A:", W_A)
print("权重变化轨迹 Wtrack:", Wtrack)
print("样本索引 iTrack:", iTrack)

# 3. 将结果保存到 CSV 文件中
# 保存特征权重
W_A_df = pd.DataFrame(W_A, columns=['Weight'])
W_A_df.to_csv('feature_weights.csv', index=False)

# 保存权重变化轨迹
Wtrack_df = pd.DataFrame(Wtrack, columns=[f'Weight_Change_{i}' for i in range(Wtrack.shape[1])])
Wtrack_df.to_csv('weight_changes.csv', index=False)

# 保存样本索引
iTrack_df = pd.DataFrame(iTrack, columns=['Sample_Index'])
iTrack_df.to_csv('sample_indices.csv', index=False)
