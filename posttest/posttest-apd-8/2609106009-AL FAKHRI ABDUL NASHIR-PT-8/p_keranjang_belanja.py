import os
import inquirer
from prettytable import PrettyTable, ALL

import fail_or_succeed as cek
import setup_variables as setvar
import setup_list_produk as setlpr
import setup_pembayaran as setbayar

def keranjang_belanja(menu_utama_pengguna):
    os.system("cls")
    print("=" * 40)
    print("             KERANJANG BELANJA             ")
    print("=" * 40)
    if not setvar.list_keranjang_belanja:
        cek.tekan_kembali("Keranjang belanja kosong.")
        menu_utama_pengguna()
    else:
        tabel = PrettyTable()
        print("=" * 40)
        tabel.hrules = ALL
        tabel.field_names = ["Nama Produk", "Harga Produk", "Banyak Pesanan"]
        for produk in setvar.list_keranjang_belanja:
            tabel.add_row([produk, setvar.list_keranjang_belanja[produk][0], setvar.list_keranjang_belanja[produk][1]])
        tabel.add_autoindex("No")
        tabel.align["No"] = "l"
        print(tabel)
        print("=" * 40)
        opsi = [
            inquirer.List("Opsi Keranjang Belanja", message="Pilih Opsi", choices=["Beli Produk", "Beli Semua", "Hapus Produk", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        opsi_keranjang = jawaban["Opsi Keranjang Belanja"]
        if opsi_keranjang == "Beli Produk":
            beli_satu_produk(menu_utama_pengguna)
        elif opsi_keranjang == "Beli Semua":
            beli_semua_produk(menu_utama_pengguna)
        elif opsi_keranjang == "Hapus Produk":
            hapus_produk_keranjang(menu_utama_pengguna)
        elif opsi_keranjang == "Kembali":
            menu_utama_pengguna()

def beli_satu_produk(menu_utama_pengguna):
    os.system("cls")
    print("=" * 40)
    print("             KERANJANG BELANJA             ")
    print("=" * 40)
    tabel = PrettyTable()
    tabel.hrules = ALL
    tabel.field_names = ["Nama Produk", "Harga Produk", "Banyak Pesanan"]
    for produk in setvar.list_keranjang_belanja:
        tabel.add_row([produk, setvar.list_keranjang_belanja[produk][0], setvar.list_keranjang_belanja[produk][1]])
    tabel.add_autoindex("No")
    tabel.align["No"] = "l"
    print(tabel)
    print("=" * 40)
    global total_harga, pilih_produk_keranjang
    test_beli_keranjang_semua = False
    total_harga = 0
    pilih_produk_keranjang = input("Masukkan nama produk yang ingin dibayar: ")
    for produk in setvar.list_keranjang_belanja:
        if produk == pilih_produk_keranjang.strip():
            total_harga = int(setvar.list_keranjang_belanja[produk][0]) * int(setvar.list_keranjang_belanja[produk][1])
            jumlah_pesanan = int(setvar.list_keranjang_belanja[produk][0])
            for produk in setvar.list_produk["nama_produk"]:
                list_produk_test = setvar.list_produk["nama_produk"].index(produk)
                if setvar.list_produk["nama_produk"][list_produk_test] == pilih_produk_keranjang:
                    setbayar.proses_pembayaran_keranjang(menu_utama_pengguna, jumlah_pesanan, total_harga, test_beli_keranjang_semua)
            cek.tekan_kembali("Produk tidak ditemukan.")
            keranjang_belanja(menu_utama_pengguna)
            return False
        cek.tekan_kembali("Produk tidak ditemukan.")
        menu_utama_pengguna()

def beli_semua_produk(menu_utama_pengguna):
    global total_harga
    test_beli_keranjang_semua = True
    total_harga = 0
    os.system("cls")
    print("=" * 40)
    print("             KERANJANG BELANJA             ")
    print("=" * 40)
    for produk in setvar.list_keranjang_belanja:
        total_harga = int(setvar.list_keranjang_belanja[produk][0]) * int(setvar.list_keranjang_belanja[produk][1]) + int(total_harga)
    opsi = [
        inquirer.List("Opsi Beli Semua", message="Beli semua produk dari keranjang belanja?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    konfirmasi_pesanan = jawaban["Opsi Beli Semua"]
    if konfirmasi_pesanan == "Ya":
        os.system("cls")
        for produk in setvar.list_keranjang_belanja:
            banyak_pesanan = int(setvar.list_keranjang_belanja[produk][0])
            jumlah_pesanan = jumlah_pesanan + banyak_pesanan
        setbayar.proses_pembayaran_keranjang(menu_utama_pengguna, jumlah_pesanan, total_harga, test_beli_keranjang_semua)
    elif konfirmasi_pesanan == "Tidak":
        keranjang_belanja(menu_utama_pengguna)

def hapus_produk_keranjang(menu_utama_pengguna):
    while True:
        os.system("cls")
        print("=" * 40)
        print("             KERANJANG BELANJA             ")
        print("=" * 40)
        tabel = PrettyTable()
        tabel.hrules = ALL
        tabel.field_names = ["Nama Produk", "Harga Produk", "Banyak Pesanan"]
        for produk in setvar.list_keranjang_belanja:
            tabel.add_row([produk, setvar.list_keranjang_belanja[produk][0], setvar.list_keranjang_belanja[produk][1]])
        tabel.add_autoindex("No")
        tabel.align["No"] = "l"
        print(tabel)
        print("=" * 40)
        global pilih_produk_keranjang
        pilih_produk_keranjang = input("Masukkan nama produk yang ingin dihapus: ")
        for produk in setvar.list_produk["nama_produk"]:
            list_produk_test = setvar.list_produk["nama_produk"].index(produk)
            if setvar.list_produk["nama_produk"][list_produk_test] == pilih_produk_keranjang:
                indeks_list_produk = setvar.list_produk["nama_produk"].index(pilih_produk_keranjang)
                os.system("cls")
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
                tampilan_banyak_pesanan = setvar.list_keranjang_belanja[produk][1]
                tampilan_keseluruhan_harga = setvar.list_keranjang_belanja[produk][0]
                tabel.max_width["Informasi Produk"] = 30
                tabel.add_column("Klasifikasi", ["Nama Produk", "Harga Produk", "Kategori Produk", "Detail Produk", "Deskripsi Produk", "Kondisi Produk", "Stok Produk", "Berat Produk", "Detail Pengiriman", "Banyak Pesanan", "Keseluruhan Harga"])
                tabel.add_column("Informasi Produk", [tampilan_nama_produk, f"Rp{tampilan_harga_produk}", tampilan_kategori_produk, tampilan_detail_produk, tampilan_deskripsi_produk, tampilan_kondisi_produk, tampilan_stok_produk, tampilan_berat_produk, tampilan_detail_pengiriman, tampilan_banyak_pesanan, tampilan_keseluruhan_harga])
                tabel.align["Informasi Produk"] = "l"
                tabel.hrules = 1
                print(tabel)
                print("=" * 40)
            else:
                os.system("cls")
                cek.tekan_kembali("Produk tidak ditemukan.")
                keranjang_belanja(menu_utama_pengguna)
                return False
        for produk_keranjang in setvar.list_keranjang_belanja:
            if produk_keranjang == pilih_produk_keranjang:
                opsi = [
                    inquirer.List("Opsi Hapus Produk Keranjang Belanja", message="Hapus produk ini dari keranjang belanja?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                konfirmasi_hapus_produk_keranjang = jawaban["Opsi Hapus Produk Keranjang Belanja"]
                if konfirmasi_hapus_produk_keranjang == "Ya":
                    del setvar.list_keranjang_belanja[pilih_produk_keranjang]
                    os.system("cls")
                    cek.tekan_kembali("Produk berhasil dihapus!")
                    keranjang_belanja(menu_utama_pengguna)
                    return True
                elif konfirmasi_hapus_produk_keranjang == "Tidak":
                    keranjang_belanja(menu_utama_pengguna)
                    return True
