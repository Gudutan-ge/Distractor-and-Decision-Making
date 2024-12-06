import numpy as np
import pandas as pd
import pygame

# 初始化 pygame
pygame.init()
# 设置屏幕尺寸
screen_width = 1200
screen_height = 900
image_width = 300
image_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("商品展示")
# 设置字体
font_path = "C:/Windows/Fonts/SimHei.ttf"
font = pygame.font.Font(font_path, 20)

# 读取 product 数据
product = pd.read_csv('products_data.csv')
# 读取每组的 trail2 和 trail3 数据
trail2 = pd.read_csv(f'trail_data/trail30_2.csv')
trail3 = pd.read_csv(f'trail_data/trail30_3.csv')

def assign_brand(category, brand_score):
    # 根据 category 和 brand_score 分配品牌和图片路径
    if category == 1:
        if 0 <= brand_score < 2:
            image_path = f"images/leshi.jpg"
        elif 2 <= brand_score < 4:
            image_path = f"images/shuyuan.jpg"
        elif 4 <= brand_score < 6:
            image_path = f"images/shanghaojia.jpg"
        elif 6 <= brand_score < 8:
            image_path = f"images/kebike.jpg"
        elif 8 <= brand_score <= 10:
            image_path = f"images/haoyouqu.jpg"
    elif category == 2:
        if 0 <= brand_score < 2:
            image_path = f"images/iphone.jpg"
        elif 2 <= brand_score < 4:
            image_path = f"images/huawei.jpg"
        elif 4 <= brand_score < 6:
            image_path = f"images/sanxing.jpg"
        elif 6 <= brand_score < 8:
            image_path = f"images/xiaomi.jpg"
        elif 8 <= brand_score <= 10:
            image_path = f"images/oppo.jpg"
    elif category == 3:
        if 0 <= brand_score < 2:
            image_path = f"images/mengniu.jpg"
        elif 2 <= brand_score < 4:
            image_path = f"images/yili.jpg"
        elif 4 <= brand_score < 6:
            image_path = f"images/guangming.jpg"
        elif 6 <= brand_score < 8:
            image_path = f"images/telunsu.jpg"
        elif 8 <= brand_score <= 10:
            image_path = f"images/sanyuan.jpg"
    elif category == 4:
        if 0 <= brand_score < 2:
            image_path = f"images/haifeisi.jpg"
        elif 2 <= brand_score < 4:
            image_path = f"images/panting.jpg"
        elif 4 <= brand_score < 6:
            image_path = f"images/shaxuan.jpg"
        elif 6 <= brand_score < 8:
            image_path = f"images/bawang.jpg"
        elif 8 <= brand_score <= 10:
            image_path = f"images/oulaiya.jpg"
    elif category == 5:
        if 0 <= brand_score < 2:
            image_path = f"images/nongfushanquan.jpg"
        elif 2 <= brand_score < 4:
            image_path = f"images/yibao.jpg"
        elif 4 <= brand_score < 6:
            image_path = f"images/baisuishan.jpg"
        elif 6 <= brand_score < 8:
            image_path = f"images/wahaha.jpg"
        elif 8 <= brand_score <= 10:
            image_path = f"images/kangshifu.jpg"
    # 返回品牌和图片路径
    return image_path

def assign_price(category, price_score):
    # 根据 price_score 的不同范围分配价格
    if category == 1:
        if 8 <= price_score <= 10:
            return np.random.uniform(5, 10)  # 在 5-10 元之间随机分布
        elif 6 <= price_score < 8:
            return np.random.uniform(10, 15)  # 在 10-15 元之间随机分布
        elif 4 <= price_score < 6:
            return np.random.uniform(3, 5)   # 在 3-5 元之间随机分布
        elif 2 <= price_score < 4:
            return np.random.uniform(15, 20)  # 在 15-20 元之间随机分布
        elif 0 <= price_score < 2:
            return np.random.uniform(20, 25)  # 在 20-25 元之间随机分布
    elif category == 2:
        if 8 <= price_score <= 10:
            return np.random.uniform(4000, 6000)  # 在 4000-6000 元之间随机分布
        elif 6 <= price_score < 8:
            return np.random.uniform(2000, 4000)  # 在 2000-4000 元之间随机分布
        elif 4 <= price_score < 6:
            return np.random.uniform(6000, 8000)  # 在 6000-8000 元之间随机分布
        elif 2 <= price_score < 4:
            return np.random.uniform(1000, 2000)  # 在 1000-2000 元之间随机分布
        elif 0 <= price_score < 2:
            return np.random.uniform(8000, 10000)  # 在 8000-10000 元之间随机分布
    elif category == 3:
        if 8 <= price_score <= 10:
            return np.random.uniform(3, 5)  # 在 3-5 元之间随机分布
        elif 6 <= price_score < 8:
            return np.random.uniform(5, 8)  # 在 5-8 元之间随机分布
        elif 4 <= price_score < 6:
            return np.random.uniform(2, 3)  # 在 2-3 元之间随机分布
        elif 2 <= price_score < 4:
            return np.random.uniform(8, 10)  # 在 8-10 元之间随机分布
        elif 0 <= price_score < 2:
            return np.random.uniform(10, 15)  # 在 10-15 元之间随机分布
    elif category == 4:
        if 8 <= price_score <= 10:
            return np.random.uniform(20, 40)  # 在 20-40 元之间随机分布
        elif 6 <= price_score < 8:
            return np.random.uniform(40, 60)  # 在 40-60 元之间随机分布
        elif 4 <= price_score < 6:
            return np.random.uniform(60, 80)  # 在 60-80 元之间随机分布
        elif 2 <= price_score < 4:
            return np.random.uniform(15, 20)  # 在 15-20 元之间随机分布
        elif 0 <= price_score < 2:
            return np.random.uniform(80, 100)  # 在 80-100 元之间随机分布
    elif category == 5:
        if 8 <= price_score <= 10:
            return 2  # 价格固定为 2 元
        elif 6 <= price_score < 8:
            return 3  # 价格固定为 3 元
        elif 4 <= price_score < 6:
            return np.random.uniform(3, 5)  # 在 3-5 元之间随机分布
        elif 2 <= price_score < 4:
            return np.random.uniform(0.5, 1)  # 在 0.5-1 元之间随机分布
        elif 0 <= price_score < 2:
            return np.random.uniform(5, 8)  # 在 5-8 元之间随机分布

def assign_quality(category, quality_score):
    # 根据 quality_score 的不同范围分配质量百分比
    if category == 1: # 薯片含油量
        if 0 <= quality_score < 2:
            return np.random.uniform(0.05, 0.10)  # 在 5%-10% 之间随机分布
        elif 2 <= quality_score < 4:
            return np.random.uniform(0.10, 0.15)  # 在 10%-15% 之间随机分布
        elif 4 <= quality_score < 6:
            return np.random.uniform(0.15, 0.20)  # 在 15%-20% 之间随机分布
        elif 6 <= quality_score < 8:
            return np.random.uniform(0.20, 0.30)  # 在 20%-30% 之间随机分布
        elif 8 <= quality_score <= 10:
            return np.random.uniform(0.30, 0.35)  # 在 30%-35% 之间随机分布
    elif category == 2: # 手机像素
        if 0 <= quality_score < 2:
            return 3200  # 3200w像素
        elif 2 <= quality_score < 4:
            return 6400  # 6400w像素
        elif 4 <= quality_score < 6:
            return 10000  # 1亿像素
        elif 6 <= quality_score < 8:
            return 16000  # 1.6亿像素
        elif 8 <= quality_score <= 10:
            return 16000  # 2亿像素
    elif category == 3: # 牛奶钙含量
        if 0 <= quality_score < 2:
            return 100  # 100mg/100ml
        elif 2 <= quality_score < 4:
            return 105  # 105mg/100ml
        elif 4 <= quality_score < 6:
            return 110  # 110mg/100ml
        elif 6 <= quality_score < 8:
            return 120  # 120mg/100ml
        elif 8 <= quality_score <= 10:
            return 125  # 125mg/100ml
    elif category == 4: # 洗发水有效物含量
        if 0 <= quality_score < 2:
            return 0.17  # 17%
        elif 2 <= quality_score < 4:
            return 0.2  # 20%
        elif 4 <= quality_score < 6:
            return 0.22  # 22%
        elif 6 <= quality_score < 8:
            return 0.24  # 24%
        elif 8 <= quality_score <= 10:
            return 0.27  # 27%
    elif category == 5: # 瓶装水总溶解固体
        if 0 <= quality_score < 2:
            return 125  # 125mg/L
        elif 2 <= quality_score < 4:
            return 100  # 100mg/L
        elif 4 <= quality_score < 6:
            return 20  # 20mg/L
        elif 6 <= quality_score < 8:
            return 50  # 50mg/L
        elif 8 <= quality_score <= 10:
            return 75  # 75mg/L

def display_image_with_text(category, image_path, position, price, quality):
    # 加载图片
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (image_width, image_height))  # 调整图片大小

    # 获取图片位置
    x, y = position
    
    # 在屏幕上绘制图片
    screen.blit(image, (x, y))

    # 在图片下方显示价格和质量信息
    if category == 1:
        price_text = font.render(f"价格: {int(price)} 元（大包 250g）", True, (0, 0, 0))
        quality_text = font.render(f"含油量: {int(price)}%", True, (0, 0, 0))
    elif category == 2:
        price_text = font.render(f"价格: {int(price)} 元/部", True, (0, 0, 0))
        if quality >= 10000:
            quality_text = font.render(f"像素: {quality / 10000:.1f} 亿", True, (0, 0, 0))
        elif quality < 10000:
            quality_text = font.render(f"像素: {quality} 万", True, (0, 0, 0))
    elif category == 3:
        price_text = font.render(f"价格: {int(price)} 元/盒", True, (0, 0, 0))
        quality_text = font.render(f"钙含量: {quality} mg/100ml", True, (0, 0, 0))
    elif category == 4:
        price_text = font.render(f"价格: {int(price)} 元/瓶", True, (0, 0, 0))
        quality_text = font.render(f"有效物含量: {int(price)}%", True, (0, 0, 0))
    elif category == 5:
        price_text = font.render(f"价格: {price:.1f} 元/瓶", True, (0, 0, 0))
        quality_text = font.render(f"总溶解固体: {quality} mg/L", True, (0, 0, 0))
    
    # 显示价格和质量
    screen.blit(price_text, (x, y + image_height))  # 文字位置在图片下方
    screen.blit(quality_text, (x, y + image_height + 25))  # 质量文字位置稍微下移

def display(num_choice, category, data):
    # 清空屏幕，准备绘制
    screen.fill((255, 255, 255))
    start_time = pygame.time.get_ticks()  # 记录实验开始的时间
    choice_made = False
    choice_time = 0  # 响应时间
    chosen_option = None  # 用户选择的选项

    if num_choice == 2:
        # 2个商品，左边和右边显示
        # 左边显示第一个商品
        display_image_with_text(category, data[0][0], (screen_width // 4 - image_width // 2, screen_height // 2 - image_height // 2), data[0][1], data[0][2])
        # 右边显示第二个商品
        display_image_with_text(category, data[1][0], (screen_width * 3 // 4 - image_width // 2, screen_height // 2 - image_height // 2), data[1][1], data[1][2])
    elif num_choice == 3:
        # 3个商品，等腰三角形排列
        # 中间显示第一个商品
        display_image_with_text(category, data[0][0], (screen_width // 2 - image_width // 2, screen_height // 3 - image_height // 2), data[0][1], data[0][2])
        # 左下方显示第二个商品
        display_image_with_text(category, data[1][0], (screen_width // 4 - image_width // 2, screen_height * 2 // 3 - image_height // 2), data[1][1], data[1][2])
        # 右下方显示第三个商品
        display_image_with_text(category, data[2][0], (screen_width * 3 // 4 - image_width // 2, screen_height * 2 // 3 - image_height // 2), data[2][1], data[2][2])
    
    # 更新屏幕显示
    pygame.display.flip()
    # 监听键盘事件
    while not choice_made:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if num_choice == 2:
                    # 对于 num_choice == 2，按下左或右箭头进行选择
                    if event.key == pygame.K_LEFT:  # 左箭头键
                        chosen_option = data[0][3]
                        choice_time = (pygame.time.get_ticks() - start_time) / 1000  # 计算响应时间（秒）
                        choice_made = True
                    elif event.key == pygame.K_RIGHT:  # 右箭头键
                        chosen_option = data[1][3]
                        choice_time = (pygame.time.get_ticks() - start_time) / 1000  # 计算响应时间（秒）
                        choice_made = True
                elif num_choice == 3:
                    # 对于 num_choice == 3，按下左、右或下箭头键进行选择
                    if event.key == pygame.K_LEFT:  # 左箭头键
                        chosen_option = data[1][3]
                        choice_time = (pygame.time.get_ticks() - start_time) / 1000  # 计算响应时间（秒）
                        choice_made = True
                    elif event.key == pygame.K_RIGHT:  # 右箭头键
                        chosen_option = data[2][3]
                        choice_time = (pygame.time.get_ticks() - start_time) / 1000  # 计算响应时间（秒）
                        choice_made = True
                    elif event.key == pygame.K_DOWN:  # 下箭头键选择中间选项
                        chosen_option = data[0][3]
                        choice_time = (pygame.time.get_ticks() - start_time) / 1000  # 计算响应时间（秒）
                        choice_made = True
    return chosen_option, choice_time

def data_create(category, num_choice, *item_ids):
    data = []
    for item_id in item_ids:
        brand_score = product.loc[product['item_id'] == item_id, 'brand_score'].values[0]
        price_score = product.loc[product['item_id'] == item_id, 'price_score'].values[0]
        quality_score = product.loc[product['item_id'] == item_id, 'quality_score'].values[0]
        # 根据 brand_score 分配品牌
        image_path = assign_brand(category, brand_score)
        # 根据 price_score 分配价格
        price = assign_price(category, price_score)
        # 根据 quality_score 分配质量
        quality = assign_quality(category, quality_score)
        data.append((image_path, price, quality, item_id))
        print(data)
    return display(num_choice, category, data)


def two_choice(category, item_id1, item_id2):
    return data_create(category, 2, item_id1, item_id2)

def tri_choice(category, item_id1, item_id2, item_id3):
    return data_create(category, 3, item_id1, item_id2, item_id3)

if __name__ == "__main__":
    # 遍历 trail2 中的每一行数据
    for index2, row2 in trail2.iterrows():
        # 获取当前行的商品编号
        category = row2['category']
        item_id1 = row2['item1']
        item_id2 = row2['item2']
        chosen_option, choice_time = two_choice(category, item_id1, item_id2)
        # 将 chosen_option 和 choice_time 写入 trail2 的新列
        trail2.at[index2, 'choice'] = chosen_option
        trail2.at[index2, 'rt'] = choice_time

    for index3, row3 in trail3.iterrows():
        # 获取当前行的商品编号
        category = row3['category']
        item_id1 = row3['item1']
        item_id2 = row3['item2']
        item_id3 = row3['item3']
        chosen_option, choice_time = tri_choice(category, item_id1, item_id2, item_id3)
        # 将 chosen_option 和 choice_time 写入 trail2 的新列
        trail3.at[index3, 'choice'] = chosen_option
        trail3.at[index3, 'rt'] = choice_time

    # 保存更新后的文件到 `data` 文件夹中
    trail2.to_csv(f'data/updated_trail30_2.csv', index=False)
    trail3.to_csv(f'data/updated_trail30_3.csv', index=False)