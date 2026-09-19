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

total_bayar_dolar_amerika_serikat = 0.000056 * total_bayar
total_bayar_yuan_tiongkok = 0.00038 * total_bayar

print("Harga barang 1 =", barang_1)
print("Harga barang 2 =", barang_2)
print("Harga barang 3 =", barang_3)
print("Harga barang 4 =", barang_4)
print("Harga barang 5 =", barang_5)
print("Harga barang 6 =", barang_6)
print("List semua harga barang secara berurutan =", belanjaan)
print("Total pajak =", pajak)
print("Total pembayaran =", total_bayar)
print("Rata-rata pembayaran =", rata_rata)
print("Tiga digit terakhir nim =", nim)
print("Bolean antara nim dan rata-rata =", bolean)
print("Pembayaran dalam mata uang Dolar Amerika Serikat =", total_bayar_dolar_amerika_serikat, "USD")
print("Pembayaran dalam mata uang Yuan Tiongkok", total_bayar_yuan_tiongkok, "CNY")
print("Tampilan harga barang 1, barang 3, dan barang 5 secara berurutan =", belanjaan[0], belanjaan[2], belanjaan[4])