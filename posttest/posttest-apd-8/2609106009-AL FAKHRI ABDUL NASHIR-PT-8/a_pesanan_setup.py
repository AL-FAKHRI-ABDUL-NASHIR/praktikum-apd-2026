import os
import setup_variables as setvar

def terima_pengajuan_batal(pilih_produk):
    os.system("cls")
    for produk in setvar.list_pesanan["nama_produk"]:
        if produk == pilih_produk:
            indeks_list_pesanan = setvar.list_pesanan["nama_produk"].index(pilih_produk)
            indeks_list_produk = setvar.list_produk["nama_produk"].index(produk)
    setvar.list_produk["stok_produk"][indeks_list_produk] = int(setvar.list_produk["stok_produk"][indeks_list_produk]) + int(setvar.list_hasil_pemesanan["jumlah_pesanan"][indeks_list_pesanan])
    setvar.penyimpanan_uang_admin = int(setvar.penyimpanan_uang_admin) + int(setvar.list_hasil_pemesanan["kembalian"][indeks_list_pesanan]) - int(setvar.list_hasil_pemesanan["uang_bayar"][indeks_list_pesanan])
    del setvar.list_pesanan["nama_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["harga_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["kategori_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["detail_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["deskripsi_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["kondisi_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["stok_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["berat_produk"][indeks_list_pesanan]
    del setvar.list_pesanan["detail_pengiriman"][indeks_list_pesanan]
    del setvar.list_pesanan["status_pesanan"][indeks_list_pesanan]
    print("=" * 40)
    print("             MENU PESANAN             ")
    print("=" * 40)
    print(f"{setvar.list_pesanan["nama_pesanan"][indeks_list_pesanan]} : {setvar.list_pesanan["status_pesanan"][indeks_list_pesanan]}")
def tolak_pengajuan_batal(pilih_produk):
    os.system("cls")
    for produk in setvar.list_pesanan["nama_produk"]:
        if produk == pilih_produk:
            indeks_list_pesanan = setvar.list_pesanan["nama_produk"].index(pilih_produk)
    setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] = "Menunggu"
    print("=" * 40)
    print("             MENU PESANAN             ")
    print("=" * 40)
    print(f"{setvar.list_pesanan["nama_pesanan"][indeks_list_pesanan]} : {setvar.list_pesanan["status_pesanan"][indeks_list_pesanan]}")
def informasi_pesanan(pilih_produk):
    os.system("cls")
    for produk in setvar.list_pesanan["nama_produk"]:
        if produk == pilih_produk:
            indeks_list_pesanan = setvar.list_pesanan["nama_produk"].index(pilih_produk)
    print("=" * 40)
    print("             MENU PESANAN             ")
    print("=" * 40)
    print(f"{setvar.list_pesanan["nama_produk"][indeks_list_pesanan]} : {setvar.list_pesanan["status_pesanan"][indeks_list_pesanan]}")