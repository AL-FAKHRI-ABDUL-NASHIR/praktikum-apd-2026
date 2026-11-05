import os
import inquirer

import setup_variables as setvar
import setup_list_produk as setlpr
import setup_pembayaran as setbayar
import fail_or_succeed as cek

def halaman_produk(menu_utama_pengguna):
    status_produk = setlpr.test_list_produk("             HALAMAN PRODUK             ")
    if not status_produk:
        menu_utama_pengguna()
    elif status_produk:
        global pilih_produk
        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ").strip()
        status_produk = setlpr.tampilan_produk("             DAFTAR PRODUK             ", pilih_produk)
        if status_produk:
            setlpr.tampilan_produk("             HALAMAN PRODUK             ", pilih_produk)
            print("=" * 40)
            opsi = [
                inquirer.List("Opsi Pilih Halaman Produk", message="Apakah Anda ingin memesan produk ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            opsi_halaman_produk = jawaban["Opsi Pilih Halaman Produk"]
            if opsi_halaman_produk == "Ya":
                if pilih_produk in setvar.list_pesanan["nama_produk"]:
                    os.system("cls")
                    cek.tekan_kembali("Produk ini sudah Anda pesan.")
                    halaman_produk(menu_utama_pengguna)
                else:
                    global jumlah_stok
                    jumlah_stok = int(setvar.list_produk["stok_produk"][setlpr.indeks_list_produk])
                    if jumlah_stok == 0:
                        os.system("cls")
                        cek.tekan_kembali("Stok produk tidak tersedia.")
                        menu_utama_pengguna()
                    else:
                        pemesanan_produk(menu_utama_pengguna)
            elif opsi_halaman_produk == "Tidak":
                menu_utama_pengguna()
        else:
            menu_utama_pengguna()            

def pemesanan_produk(menu_utama_pengguna):
    os.system("cls")
    print("=" * 40)
    print("             OPSI PEMESANAN             ")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Pilih Pemesanan", message="Pilih Opsi", choices=["Tambahkan ke Keranjang Belanja", "Langsung Bayar"])
    ]
    jawaban = inquirer.prompt(opsi)
    opsi_pemesanan = jawaban["Opsi Pilih Pemesanan"]
    if opsi_pemesanan == "Tambahkan ke Keranjang Belanja":
        opsi_keranjang_belanja(menu_utama_pengguna)
    elif opsi_pemesanan == "Langsung Bayar":
        opsi_bayar_langsung(menu_utama_pengguna)

def opsi_keranjang_belanja(menu_utama_pengguna):
    while True:
        global jumlah_pesanan
        try:
            os.system("cls")
            print("=" * 40)
            print("             OPSI PEMESANAN             ")
            print("=" * 40)
            print(f"Stok Produk: {setvar.list_produk["stok_produk"][setlpr.indeks_list_produk]}")
            print("=" * 40)
            jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            break
    if int(jumlah_pesanan) > int(jumlah_stok):
        cek.tekan_kembali("Stok tidak mencukupi.")
        menu_utama_pengguna()
    elif int(jumlah_pesanan) > 0:
        setvar.list_keranjang_belanja.setdefault(setvar.list_produk["nama_produk"][setlpr.indeks_list_produk], [setvar.list_produk["harga_produk"][setlpr.indeks_list_produk], jumlah_pesanan])
        cek.tekan_kembali("Produk berhasil ditambahkan ke keranjang belanja!")
        menu_utama_pengguna()
    else:
        cek.kesalahan("=====Jumlah pesanan tidak valid. Silakan masukkan kembali anda.=====")
        opsi_keranjang_belanja(menu_utama_pengguna)

def opsi_bayar_langsung(menu_utama_pengguna):
    while True:
        global jumlah_pesanan
        try:
            os.system("cls")
            print("=" * 40)
            print("             OPSI PEMESANAN             ")
            print("=" * 40)
            print(f"Stok Produk: {setvar.list_produk["stok_produk"][setlpr.indeks_list_produk]}")
            print("=" * 40)
            jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            break
    if int(jumlah_pesanan) > int(jumlah_stok):
        cek.tekan_kembali("Stok tidak mencukupi. Silakan masukkan kembali jumlah pesanan anda.")
        opsi_bayar_langsung(menu_utama_pengguna)
    elif int(jumlah_pesanan) > 0:
        setbayar.perhitungan_total_harga(jumlah_pesanan)
        os.system("cls")
        print("=" * 40)
        print(f"Total Harga: {setbayar.total_harga}")
        print("=" * 40)
        opsi = [
            inquirer.List("Opsi Konfirmasi Pesanan", message="Apakah Anda ingin melanjutkan ke pembayaran?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        konfirmasi_pesanan = jawaban["Opsi Konfirmasi Pesanan"]
        if konfirmasi_pesanan == "Ya":
            setbayar.proses_pembayaran_langsung(menu_utama_pengguna, jumlah_pesanan)
        elif konfirmasi_pesanan == "Tidak":
            os.system("cls")
            cek.tekan_kembali("Pesanan dibatalkan.")
            menu_utama_pengguna()
    else:
        cek.kesalahan("=====Jumlah pesanan tidak valid. Silakan masukkan kembali.=====")
        opsi_bayar_langsung(menu_utama_pengguna)