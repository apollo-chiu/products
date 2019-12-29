#先讀取舊檔
import os #載入作業系統模組
#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			line = line.encode('utf-8').decode('utf-8-sig') #去除ufeff碼
			if '商品名稱,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
else:
	print('找不到檔案....')

#新增 商品名稱 價格
while 1:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	products.append([name, price])
# print(products[0][0], products[0][1])	
for d in products:
	print(d[0], '的價格是', d[1])

with open('products.csv', 'w', encoding='utf-8') as f:

	f.write('商品名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

		