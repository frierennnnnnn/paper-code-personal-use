import pandas as pd
from scipy.stats import pearsonr, spearmanr

# 读取CSV文件
df = pd.read_csv('test.csv')

# 获取除了V3列之外的所有列
columns = [col for col in df.columns if col != 'V3']

# 初始化结果字典
results = {
    'Pearson': {},
    'Spearman': {}
}

# 计算每列与V3列的相关系数
for col in columns:
    # 计算Pearson相关系数
    pearson_corr, _ = pearsonr(df['V3'], df[col])
    results['Pearson'][col] = pearson_corr

    # 计算Spearman相关系数
    spearman_corr, _ = spearmanr(df['V3'], df[col])
    results['Spearman'][col] = spearman_corr

# 对结果进行排序
sorted_pearson = sorted(results['Pearson'].items(), key=lambda x: x[1], reverse=True)
sorted_spearman = sorted(results['Spearman'].items(), key=lambda x: x[1], reverse=True)

# 打印结果
print("Pearson Correlation Coefficients (Sorted):")
for col, corr in sorted_pearson:
    print(f"{col}: {corr:.4f}")

print("\nSpearman Correlation Coefficients (Sorted):")
for col, corr in sorted_spearman:
    print(f"{col}: {corr:.4f}")
