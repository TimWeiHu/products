import os

products = []

# 讀取檔案
if os.path.isfile('products.csv'):
    print('找到檔案')
    with open('products.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
           # name, price = 
            products.append(line.strip().split(','))
else:
    print('找不到檔案')

# 輸入新項目
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    p = [name, price]
    products.append(p)
print('---------------------')
# 印出所有項目
for p in products:
    print(p[0], '價格：', p[1])
# 寫入檔案
with open('products.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')