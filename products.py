import os

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            products.append(line.strip().split(','))
    return products

# 輸入新項目
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        price = int(price)
        p = [name, price]
        products.append(p)
    print('---------------------')
    return products

# 印出所有項目
def print_products(products):
    for p in products:
        print(p[0], '價格：', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()