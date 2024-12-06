import pandas as pd
import numpy as np

params_init = {
    "K": 4,            # 减小增益
    "sigma_H": 2.5,    # 减小半饱和常数
    "w": 1,          # 稍微减小抑制权重
    "sigma_fixed": 0.2,  # 适度减小固定噪声
    "S": 0.1          # 减小比例噪声
}

# 模型计算放电率
def compute_firing_rate(values, params):
    V_sum = np.sum(values)
    firing_rates = [params["K"] * V / (params["sigma_H"] + params["w"] * V_sum) for V in values]
    return np.array(firing_rates)

# 加入噪声
def add_noise(firing_rates, params):
    fixed_noise = np.random.normal(0, params["sigma_fixed"], size=firing_rates.shape)
    scaled_noise = np.random.normal(0, params["S"] * firing_rates)
    return firing_rates + fixed_noise + scaled_noise

# 模拟选择
def simulate_choice(values, params):
    firing_rates = compute_firing_rate(values, params)
    noisy_rates = add_noise(firing_rates, params)
    return np.argmax(noisy_rates)

# 数据加载
def load_data(product_path, traildata_path):
    product = pd.read_csv(product_path)
    trialdata = pd.read_csv(traildata_path)
    data = []
    item = []
    for _, row in trialdata.iterrows():
        # 获取当前行的商品编号 category,trial,item1,item2,item3,choice
        item_id1 = row['item1']
        item_id2 = row['item2']
        item_id3 = row['item3']
        value1 = product.loc[product['item_id'] == item_id1, 'value'].values[0]
        value2 = product.loc[product['item_id'] == item_id2, 'value'].values[0]
        value3 = product.loc[product['item_id'] == item_id3, 'value'].values[0]
        data.append({
            'value1': value1,
            'value2': value2,
            'value3': value3,
        })
        item.append({
            'item_id1': item_id1,
            'item_id2': item_id2,
            'item_id3': item_id3,
        })
        data_df = pd.DataFrame(data)
        item_df = pd.DataFrame(item)
    return data_df, item_df

# 主函数
if __name__ == "__main__":
    for i in range(1, 31):
        # 加载实验数据，假设CSV文件格式：[V1, V2, V3, p1, p2, p3]
        data, item = load_data("products_data.csv", f"trail_data/trail{i}_3.csv")
        # 对每一组数据运行 simulate_choice
        experiment_data = pd.read_csv(f'trail_data/trail{i}_3.csv')
        for j in range(len(experiment_data)):
            result = simulate_choice(data.iloc[j].values, params_init)
            experiment_data.at[j, 'choice'] = item.iloc[j][f'item_id{result + 1}']
        experiment_data.to_csv(f'model_data/updated_trail{i}_3.csv', index=False)