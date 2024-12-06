import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 读取产品数据
product = pd.read_csv('products_data.csv')

# 读取 data 文件夹下的 30 组数据
data_folder = 'data'

# 创建一个空列表用于存储结果
results1 = [] # 存储accuracy相关结果
results2 = [] # 存储efficiency相关结果
results3 = [] # 存储target相关结果

# 遍历每组实验
for i in range(1, 31):
    # 定义文件路径
    trail2_file = os.path.join(data_folder, f'updated_trail{i}_2.csv')
    trail3_file = os.path.join(data_folder, f'updated_trail{i}_3.csv')
    
    # 读取 CSV 文件
    if os.path.exists(trail2_file) and os.path.exists(trail3_file):
        trail2 = pd.read_csv(trail2_file)
        trail3 = pd.read_csv(trail3_file)
    
    # 遍历 trail2 中的每一行数据
    for index2, row2 in trail2.iterrows():
        # 获取当前行的商品编号
        item_id1 = row2['item1']
        item_id2 = row2['item2']
        # 获取当前行的反应时间
        rt2 = row2['rt']
        # 从 product 数据框中找到对应商品的价值
        value1 = product.loc[product['item_id'] == item_id1, 'value'].values[0]
        value2 = product.loc[product['item_id'] == item_id2, 'value'].values[0]
        # 计算两者的价值差
        abs_diff = abs(value1 - value2)
        # 在 trail3 中找到对应的 item3
        trail3_match = trail3[((trail3['item1'] == item_id1) & (trail3['item2'] == item_id2))]
        # 遍历 trail3_match 中的每一条三元选择
        for index3, row3 in trail3_match.iterrows():
            # 获取当前行的商品编号
            item_id3 = row3['item3']
            # 获取当前行的反应时间
            rt3 = row3['rt']
            # 从 product 数据框中找到对应商品的价值
            value3 = product.loc[product['item_id'] == item_id3, 'value'].values[0]
            # 对 item3 进行价值归一化
            norm_value3 = 2 * value3 / (value1 + value2)
            # 计算 accuracy: 如果三元选项与二元选项一致则 accuracy 为 1，否则为 0
            accuracy = 1 if row3['choice'] == row2['choice'] else 0
            # 计算 efficiency: 三元与二元时间选择差 / 二元选择时间
            efficiency = (rt3 - rt2) / rt2
            # 计算 terget_choice: 如果三元选项在 target 范围一致则为 1，否则为 0
            terget_choice = 1 if row3['choice'] != item_id3 else 0
            # 存储结果
            results1.append({
                'value_diff': abs_diff,
                'n_value3': norm_value3,
                'accuracy': accuracy
            })
            results2.append({
                'n_value3': norm_value3,
                'efficiency': efficiency
            })
            results3.append({
                'target_choice': terget_choice,
                'n_value3': norm_value3,
            })

#---------------------------------------------------------------------------------------------#
# 绘制 accuracy 曲线
#---------------------------------------------------------------------------------------------#

# Logistic 函数
def logistic(x, a, b, c):
    return c / (1 + np.exp(-(x - a) / b))

# 将结果转换为 DataFrame
results1_df = pd.DataFrame(results1)
# 分组范围
bins = np.linspace(results1_df['n_value3'].min(), results1_df['n_value3'].max(), 5)
# 为每个范围绘制拟合曲线
for i in range(len(bins) - 1):
    # 分组端点
    bin_start = bins[i]
    bin_end = bins[i + 1]
    # 筛选出该范围内的 n_value3 数据
    bin_data = results1_df[(results1_df['n_value3'] > bin_start) & (results1_df['n_value3'] <= bin_end)]
    # 使用 Logistic 函数拟合
    popt, _ = curve_fit(logistic, bin_data['value_diff'], bin_data['accuracy'], p0=[0, 1, 1])
    # 绘制拟合曲线
    x_new = np.linspace(min(bin_data['value_diff']), max(bin_data['value_diff']), 100)
    y_new = logistic(x_new, *popt)
    plt.plot(x_new, y_new, label=f'distracter value(norm): [{bin_start:.2f}, {bin_end:.2f}]')
# 添加图例
plt.legend()
plt.xlabel('Target Value Difference')
plt.ylabel('Accuracy')
plt.title('Context-dependent choice curves')
plt.show()

#---------------------------------------------------------------------------------------------#
# 绘制 efficiency 曲线
#---------------------------------------------------------------------------------------------#

# 将结果转换为 DataFrame
results2_df = pd.DataFrame(results2)
# 分组范围
bins = np.linspace(results2_df['n_value3'].min(), results2_df['n_value3'].max(), 7)
# 分组，计算每组的平均 efficiency
results2_df['n_value3'] = pd.cut(results2_df['n_value3'], bins=bins)
grouped = results2_df.groupby('n_value3')['efficiency'].mean().reset_index()
# 提取每个组的区间起始点和 efficiency 平均值
group_centers = [group.left + (group.right - group.left) / 2 for group in grouped['n_value3']]
avg_efficiency = grouped['efficiency']
# 绘制结果
plt.plot(group_centers, avg_efficiency, marker='o', color='b', label='Extra Time((RT_3opt - RT_2opt) / RT_2opt)')
plt.xlabel('distracter value(norm)')
plt.ylabel('Extra Time')
plt.title('effect on choice efficiency')
plt.grid(True)
plt.legend()
plt.show()

#---------------------------------------------------------------------------------------------#
# 绘制 taaget_choice 曲线
#---------------------------------------------------------------------------------------------#

# 将结果转换为 DataFrame
results3_df = pd.DataFrame(results3)
# 分组范围
bins = np.linspace(results3_df['n_value3'].min(), results3_df['n_value3'].max(), 6)
# 分组，计算每组的平均 taaget_choice
results3_df['n_value3'] = pd.cut(results3_df['n_value3'], bins=bins)
grouped = results3_df.groupby('n_value3')['target_choice'].mean().reset_index()
# 提取每个组的区间起始点和 taaget_choice 平均值
group_centers = [group.left + (group.right - group.left) / 2 for group in grouped['n_value3']]
avg_target_choice = grouped['target_choice']
# 绘制结果
plt.plot(group_centers, avg_target_choice, marker='o', color='b', label='Target Choice')
plt.xlabel('distracter value(norm)')
plt.ylabel('Target Choice')
plt.title('Choice behavior varies with distracter value')
plt.grid(True)
plt.legend()
plt.show()

#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#