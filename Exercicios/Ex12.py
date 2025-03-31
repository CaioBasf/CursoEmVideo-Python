Din = float(input('Qual é o preço do produto? '))
Des = Din - (Din/100 *5)
print(f'O produto que custava R${Din}, na promoção com 5% de desconto vai custar R${Des:.2f}')
