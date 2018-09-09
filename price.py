def format_price(price):
	price = int(price)
	return 'Цена: ' + str(price) + ' руб.'
display_prise = format_price(56.24)
print(display_prise)