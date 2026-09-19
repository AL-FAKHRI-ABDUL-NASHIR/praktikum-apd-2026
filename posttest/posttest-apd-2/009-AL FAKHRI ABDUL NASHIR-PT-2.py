barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

belanjaan = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]

pajak = 0.15 * (barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6)
total_bayar = pajak + barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
rata_rata = total_bayar / len(belanjaan)

nim = 9
bolean = nim < rata_rata

total_bayar_dollar = 0.000056 * total_bayar
total_bayar_yuan = 0.00038 * total_bayar

print(barang_1)
print(barang_2)
print(barang_3)
print(barang_4)
print(barang_5)
print(barang_6)
print(belanjaan)
print(pajak)
print(total_bayar)
print(rata_rata)
print(nim)
print(bolean)
print(total_bayar_dollar)
print(total_bayar_yuan)