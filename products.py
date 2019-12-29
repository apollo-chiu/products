#先讀取舊檔
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		line = line.encode('utf-8').decode('utf-8-sig')
		name, price = line.strip().split(',')
		products.append([name, price])

print(products)


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

		