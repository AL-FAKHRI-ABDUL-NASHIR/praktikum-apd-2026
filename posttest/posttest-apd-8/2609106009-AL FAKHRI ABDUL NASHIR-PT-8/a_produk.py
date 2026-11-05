import os
import inquirer

import fail_or_succeed as cek
import setup_variables as setvar
import setup_list_produk as setlpr
import a_produk_setup as aproset

def menu_produk(menu_utama_admin):
    os.system("cls")
    print("=" * 40)
    print("               MENU PRODUK               ")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Pilih Menu Produk", message="Pilih Menu", choices=["Daftar Produk", "Tambah Produk", "Hapus Produk", "Kembali"])
    ]
    jawaban = inquirer.prompt(opsi)
    pilih_menu_produk = jawaban["Opsi Pilih Menu Produk"]
    if pilih_menu_produk == "Daftar Produk":
        daftar_produk(menu_utama_admin)
    elif pilih_menu_produk == "Tambah Produk":
        tambah_produk(menu_utama_admin)
    elif pilih_menu_produk == "Hapus Produk":
        hapus_produk(menu_utama_admin)
    elif pilih_menu_produk == "Kembali":
        menu_utama_admin()


def daftar_produk(menu_utama_admin):
    status_produk = setlpr.test_list_produk("             DAFTAR PRODUK             ")
    if not status_produk:
        menu_produk(menu_utama_admin)
    else:
        global pilih_produk
        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
        status_produk = setlpr.tampilan_produk("             DAFTAR PRODUK             ", pilih_produk)
        if status_produk:
            setlpr.tampilan_produk("             DAFTAR PRODUK             ", pilih_produk)
            print("=" * 40)
            opsi = [
                inquirer.List("Opsi Pilih Daftar Produk", message="Pilih Opsi", choices=["Kembali Ke Menu Produk", "Kembali Ke Daftar Produk"])
            ]
            jawaban = inquirer.prompt(opsi)
            pilih_daftar_produk = jawaban["Opsi Pilih Daftar Produk"]
            if pilih_daftar_produk == "Kembali Ke Menu Produk":
                menu_produk(menu_utama_admin)
            elif pilih_daftar_produk == "Kembali Ke Daftar Produk":
                daftar_produk(menu_utama_admin)
        else:
            menu_produk(menu_utama_admin)

def tambah_produk(menu_utama_admin):
    global nama_produk, harga_produk, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, stok_produk, berat_produk, detail_pengiriman, test_harga, test_harga_selesai, test_stok, test_stok_selesai, test_berat, test_berat_selesai
    nama_produk = None
    test_harga = None
    harga_produk = None
    test_harga_selesai = None
    kategori_produk = None
    detail_produk = None
    deskripsi_produk = None
    kondisi_produk = None
    test_stok = None
    stok_produk = None
    test_stok_selesai = None
    test_berat = None
    berat_produk = None
    test_berat_selesai = None
    os.system("cls")
    print("=" * 40)
    print("             TAMBAH PRODUK             ")
    print("=" * 40)
    print("=" * 40)
    print("            INFORMASI PRODUK            ")
    print("=" * 40)
    nama_produk = input("Masukkan Nama Produk: ").strip()
    os.system("cls")
    while True:
        try:
            test_harga = False
            aproset.test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai)
            harga_produk = int(input("Masukkan Harga Produk (Rp): "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            test_harga = True
            test_harga_selesai = False
            aproset.test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai)
            break
    test_harga_selesai = True
    kategori_produk = input("Masukkan Kategori Produk: ").strip()
    detail_produk = input("Masukkan Detail Produk: ").strip()
    deskripsi_produk = input("Masukkan Deskripsi Produk: ").strip()
    kondisi_produk = input("Masukkan Kondisi Produk (Baru/Bekas): ").strip()
    print("=" * 40)
    print("             BANYAK PRODUK             ")
    print("=" * 40)
    os.system("cls")
    while True:
        try:
            test_stok = False
            aproset.test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai)
            stok_produk = int(input("Masukkan Stok Produk: "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            test_stok = True
            test_stok_selesai = False
            aproset.test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai)
            break
    test_stok_selesai = True
    print("=" * 40)
    print("             PENGIRIMAN PRODUK             ")
    print("=" * 40)
    os.system("cls")
    while True:
        try:
            test_berat = False
            aproset.test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai)
            berat_produk = int(input("Masukkan Berat Produk (gram): "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            test_berat = True
            test_berat_selesai = False
            aproset.test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai)
            break
    test_berat_selesai = True
    detail_pengiriman = input("Masukkan Detail Pengiriman: ").strip()
    konfirmasi_tambah_produk(menu_utama_admin)

def konfirmasi_tambah_produk(menu_utama_admin):
    os.system("cls")
    print("=" * 40)
    print("         DATA PRODUK YANG DITAMBAHKAN         ")
    print("=" * 40)
    print(f"Nama Produk: {nama_produk}")
    print(f"Harga Produk: {harga_produk}")
    print(f"Kategori Produk: {kategori_produk}")
    print(f"Detail Produk: {detail_produk}")
    print(f"Deskripsi Produk: {deskripsi_produk}")
    print(f"Kondisi Produk: {kondisi_produk}")
    print(f"Stok Produk: {stok_produk}")
    print(f"Berat Produk: {berat_produk}")
    print(f"Detail Pengiriman: {detail_pengiriman}")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Pilih Tambah Produk", message="Simpan dan Kembali?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    simpan_kembali = jawaban["Opsi Pilih Tambah Produk"]
    if simpan_kembali == "Ya":
        os.system("cls")
        setvar.list_produk["nama_produk"].append(nama_produk)
        setvar.list_produk["harga_produk"].append(harga_produk)
        setvar.list_produk["kategori_produk"].append(kategori_produk)
        setvar.list_produk["detail_produk"].append(detail_produk)
        setvar.list_produk["deskripsi_produk"].append(deskripsi_produk)
        setvar.list_produk["kondisi_produk"].append(kondisi_produk)
        setvar.list_produk["stok_produk"].append(stok_produk)
        setvar.list_produk["berat_produk"].append(berat_produk)
        setvar.list_produk["detail_pengiriman"].append(detail_pengiriman)
        cek.tekan_kembali("Produk berhasil ditambahkan!")
        menu_produk(menu_utama_admin)
    elif simpan_kembali == "Tidak":
        os.system("cls")
        print("Pengisian dibatalkan.")
        print("=" * 40)
        opsi = [
            inquirer.List("Opsi Pilih Pengisian Ulang", message="Apakah Anda ingin mengisi ulang data produk?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        pengisian_ulang = jawaban["Opsi Pilih Pengisian Ulang"]
        if pengisian_ulang == "Ya":
            tambah_produk(menu_utama_admin)
        elif pengisian_ulang == "Tidak":
            menu_produk(menu_utama_admin)

def hapus_produk(menu_utama_admin):
    status_produk = setlpr.test_list_produk("             HAPUS PRODUK             ")
    if not status_produk:
        menu_produk(menu_utama_admin)
    else:
        global pilih_produk
        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
        status_produk = setlpr.tampilan_produk("             HAPUS PRODUK             ", pilih_produk)
        if status_produk:
            opsi = [
                inquirer.List("Opsi Pilih Hapus Produk", message="Apakah Anda ingin menghapus produk ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            pilih_hapus = jawaban["Opsi Pilih Hapus Produk"]
            if pilih_hapus == "Ya":
                os.system("cls")
                del setvar.list_produk["nama_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["harga_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["kategori_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["detail_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["deskripsi_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["kondisi_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["stok_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["berat_produk"][setlpr.indeks_list_produk]
                del setvar.list_produk["detail_pengiriman"][setlpr.indeks_list_produk]
                cek.tekan_kembali("Produk berhasil dihapus!")
                menu_produk(menu_utama_admin)
            elif pilih_hapus == "Tidak":
                menu_produk(menu_utama_admin)
        else:
            menu_produk(menu_utama_admin)
