products = []
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

		