n = int(input('Uma distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dc = n * 10
cm = n * 100
mm = n * 1000

print(f'A medida {n} em metros corresponde: ')
print(f'Quilômetro: {km}km\nHectômetro: {hm}hm')
print(f'Decâmetro: {dam}dam\nDecímetro: {dc}dc')
print(f'Centímetro: {cm}cm\nMilímetro: {mm}mm')