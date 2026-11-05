import os
from prettytable import PrettyTable, ALL

import fail_or_succeed as cek
import setup_variables as setvar

tabel = PrettyTable()

def test_list_produk(keterangan_menu):
    os.system("cls")
    print("=" * 40)
    print(keterangan_menu)
    print("=" * 40)
    list_produk_test = setvar.list_produk.get("nama_produk")
    if not list_produk_test:
        cek.tekan_kembali("Belum ada produk yang ditambahkan.")
        return False
    else:
        tabel = PrettyTable()
        tabel.hrules = ALL
        tabel.field_names = ["Nama Produk"]
        for produk in setvar.list_produk["nama_produk"]:
            tabel.add_row([produk])
        tabel.add_autoindex("No")
        tabel.align["No"] = "l"
        print(tabel)
        return True

def tampilan_produk(keterangan_menu, pilih_produk):
    os.system("cls")
    for produk in setvar.list_produk["nama_produk"]:
        list_produk_test = setvar.list_produk["nama_produk"].index(produk)
        if setvar.list_produk["nama_produk"][list_produk_test] == pilih_produk:
            global indeks_list_produk
            indeks_list_produk = setvar.list_produk["nama_produk"].index(pilih_produk)
            print("=" * 40)
            print(keterangan_menu)
            print("=" * 40)
            tabel.clear()
            tampilan_nama_produk = setvar.list_produk["nama_produk"][indeks_list_produk]
            tampilan_harga_produk = setvar.list_produk["harga_produk"][indeks_list_produk]
            tampilan_kategori_produk = setvar.list_produk["kategori_produk"][indeks_list_produk]
            tampilan_detail_produk = setvar.list_produk["detail_produk"][indeks_list_produk]
            tampilan_deskripsi_produk = setvar.list_produk["deskripsi_produk"][indeks_list_produk]
            tampilan_kondisi_produk = setvar.list_produk["kondisi_produk"][indeks_list_produk]
            tampilan_stok_produk = setvar.list_produk["stok_produk"][indeks_list_produk]
            tampilan_berat_produk = setvar.list_produk["berat_produk"][indeks_list_produk]
            tampilan_detail_pengiriman = setvar.list_produk["detail_pengiriman"][indeks_list_produk]
            tabel.max_width["Informasi Produk"] = 30
            tabel.add_column("Klasifikasi", ["Nama Produk", "Harga Produk", "Kategori Produk", "Detail Produk", "Deskripsi Produk", "Kondisi Produk", "Stok Produk", "Berat Produk", "Detail Pengiriman"])
            tabel.add_column("Informasi Produk", [tampilan_nama_produk, f"Rp{tampilan_harga_produk}", tampilan_kategori_produk, tampilan_detail_produk, tampilan_deskripsi_produk, tampilan_kondisi_produk, tampilan_stok_produk, tampilan_berat_produk, tampilan_detail_pengiriman])
            tabel.align["Informasi Produk"] = "l"
            tabel.hrules = 1
            print(tabel)
            return True
    os.system("cls")
    cek.tekan_kembali("Produk tidak ditemukan.")
    return False