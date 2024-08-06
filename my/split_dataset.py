import random

with open('../output/simple_table/gt.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
random.shuffle(lines)

train_len = int(len(lines) * 0.9)
train_list = lines[:train_len]
val_list = lines[train_len:]

# 保存结果
with open('../output/simple_table/train.txt', 'w', encoding='utf-8') as f:
    f.writelines(train_list)
with open('../output/simple_table/val.txt', 'w', encoding='utf-8') as f:
    f.writelines(val_list)
