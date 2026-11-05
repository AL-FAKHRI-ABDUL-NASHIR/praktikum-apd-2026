import os
import inquirer

import fail_or_succeed as cek
import setup_variables as setvar
import setup_list_produk as setlpr

def perhitungan_total_harga(jumlah_pesanan):
    global jumlah_harga, total_harga
    jumlah_harga = setvar.list_produk["harga_produk"][setlpr.indeks_list_produk]
    total_harga = int(jumlah_pesanan) * int(jumlah_harga)
    return total_harga
def proses_pembayaran_langsung(menu_utama_pengguna, jumlah_pesanan):
    os.system("cls")
    global uang_bayar, test_beli_keranjang_satu, test_beli_keranjang_semua
    test_beli_keranjang_satu = False
    test_beli_keranjang_semua = False
    while True:
        try:
            print("=" * 40)
            print(f"Total Harga: {total_harga}")
            print("=" * 40)
            uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            break
    if int(uang_bayar) >= int(total_harga):
        global kembalian, status_pesanan
        kembalian = int(uang_bayar) - int(total_harga)
        status_pesanan = "Menunggu"
        hasil_setelah_pembayaran(menu_utama_pengguna, jumlah_pesanan, total_harga)
    elif int(uang_bayar) < int(total_harga):
        while True:
            os.system("cls")
            print("Uang yang dibayarkan tidak mencukupi.")
            print("=" * 40)
            opsi = [
                inquirer.List("Opsi Ulang Pembayaran", message="Apakah Anda ingin mengulangi pembayaran?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            ulang_pembayaran = jawaban["Opsi Ulang Pembayaran"]
            if ulang_pembayaran == "Ya":
                proses_pembayaran_langsung(menu_utama_pengguna, jumlah_pesanan)
                break
            elif ulang_pembayaran == "Tidak":
                menu_utama_pengguna()
                break
def proses_pembayaran_keranjang(menu_utama_pengguna, jumlah_pesanan, total_harga, test_beli_keranjang_semua):
    global kembalian, status_pesanan, uang_bayar, test_beli_keranjang_satu
    test_beli_keranjang_satu = False
    while True:
        os.system("cls")
        try:
            print("=" * 40)
            print(f"Total Harga: {total_harga}")
            print("=" * 40)
            uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
        except ValueError:
            os.system("cls")
            print("Input harus angka!")
        else:
            os.system("cls")
            break
    if int(uang_bayar) >= int(total_harga):
        kembalian = int(uang_bayar) - int(total_harga)
        status_pesanan = "Menunggu"
        hasil_setelah_pembayaran(menu_utama_pengguna, jumlah_pesanan, total_harga, test_beli_keranjang_semua)
    elif int(uang_bayar) < int(total_harga):
        while True:
            os.system("cls")
            print("Uang yang dibayarkan tidak mencukupi.")
            print("=" * 40)
            opsi = [
                inquirer.List("Opsi Ulang Pembayaran", message="Apakah Anda ingin mengulangi pembayaran?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            ulang_pembayaran = jawaban["Opsi Ulang Pembayaran"]
            if ulang_pembayaran == "Ya":
                proses_pembayaran_keranjang(menu_utama_pengguna, jumlah_pesanan, total_harga, test_beli_keranjang_semua)
                break
            elif ulang_pembayaran == "Tidak":
                menu_utama_pengguna()
                break
def hasil_setelah_pembayaran(menu_utama_pengguna, jumlah_pesanan, total_harga, test_beli_keranjang_semua):
    global test_beli_keranjang_satu
    for produk in setvar.list_keranjang_belanja:
        if test_beli_keranjang_semua:
            test_beli_keranjang_satu = True
            setvar.penyimpanan_uang_admin = int(setvar.penyimpanan_uang_admin) + int(total_harga)
            setvar.list_pesanan["nama_produk"].append(setvar.list_produk["nama_produk"][produk])
            setvar.list_pesanan["harga_produk"].append(setvar.list_produk["harga_produk"][produk])
            setvar.list_pesanan["kategori_produk"].append(setvar.list_produk["kategori_produk"][produk])
            setvar.list_pesanan["detail_produk"].append(setvar.list_produk["detail_produk"][produk])
            setvar.list_pesanan["deskripsi_produk"].append(setvar.list_produk["deskripsi_produk"][produk])
            setvar.list_pesanan["kondisi_produk"].append(setvar.list_produk["kondisi_produk"][produk])
            setvar.list_pesanan["berat_produk"].append(setvar.list_produk["berat_produk"][produk])
            setvar.list_pesanan["detail_pengiriman"].append(setvar.list_produk["detail_pengiriman"][produk])
            setvar.list_pesanan["status_pesanan"].append(status_pesanan)
            setvar.list_riwayat_transaksi["nama_produk"].append(setvar.list_produk["nama_produk"][produk])
            setvar.list_riwayat_transaksi["harga_produk"].append(setvar.list_produk["harga_produk"][produk])
            setvar.list_riwayat_transaksi["kategori_produk"].append(setvar.list_produk["kategori_produk"][produk])
            setvar.list_riwayat_transaksi["detail_produk"].append(setvar.list_produk["detail_produk"][produk])
            setvar.list_riwayat_transaksi["deskripsi_produk"].append(setvar.list_produk["deskripsi_produk"][produk])
            setvar.list_riwayat_transaksi["kondisi_produk"].append(setvar.list_produk["kondisi_produk"][produk])
            setvar.list_riwayat_transaksi["berat_produk"].append(setvar.list_produk["berat_produk"][produk])
            setvar.list_riwayat_transaksi["detail_pengiriman"].append(setvar.list_produk["detail_pengiriman"][produk])
            setvar.list_riwayat_transaksi["jumlah_pesanan"].append(jumlah_pesanan)
            setvar.list_riwayat_transaksi["total_harga"].append(total_harga)
            setvar.list_riwayat_transaksi["uang_bayar"].append(uang_bayar)
            setvar.list_riwayat_transaksi["kembalian"].append(kembalian)
            setvar.list_hasil_pemesanan["jumlah_pesanan"].append(jumlah_pesanan)
            setvar.list_hasil_pemesanan["uang_bayar"].append(uang_bayar)
            setvar.list_hasil_pemesanan["kembalian"].append(kembalian)
            setvar.list_produk["stok_produk"][indeks_list_produk] = int(setvar.list_produk["stok_produk"][indeks_list_produk]) - int(jumlah_pesanan)
            setvar.list_keranjang_belanja = {}
        elif setvar.list_produk["nama_produk"][setlpr.indeks_list_produk] == produk:
            test_beli_keranjang_satu = True
            indeks_list_produk = setlpr.indeks_list_produk
            setvar.penyimpanan_uang_admin = int(setvar.penyimpanan_uang_admin) + int(total_harga)
            setvar.list_pesanan["nama_produk"].append(setvar.list_produk["nama_produk"][indeks_list_produk])
            setvar.list_pesanan["harga_produk"].append(setvar.list_produk["harga_produk"][indeks_list_produk])
            setvar.list_pesanan["kategori_produk"].append(setvar.list_produk["kategori_produk"][indeks_list_produk])
            setvar.list_pesanan["detail_produk"].append(setvar.list_produk["detail_produk"][indeks_list_produk])
            setvar.list_pesanan["deskripsi_produk"].append(setvar.list_produk["deskripsi_produk"][indeks_list_produk])
            setvar.list_pesanan["kondisi_produk"].append(setvar.list_produk["kondisi_produk"][indeks_list_produk])
            setvar.list_pesanan["berat_produk"].append(setvar.list_produk["berat_produk"][indeks_list_produk])
            setvar.list_pesanan["detail_pengiriman"].append(setvar.list_produk["detail_pengiriman"][indeks_list_produk])
            setvar.list_pesanan["status_pesanan"].append(status_pesanan)
            setvar.list_riwayat_transaksi["nama_produk"].append(setvar.list_produk["nama_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["harga_produk"].append(setvar.list_produk["harga_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["kategori_produk"].append(setvar.list_produk["kategori_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["detail_produk"].append(setvar.list_produk["detail_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["deskripsi_produk"].append(setvar.list_produk["deskripsi_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["kondisi_produk"].append(setvar.list_produk["kondisi_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["berat_produk"].append(setvar.list_produk["berat_produk"][indeks_list_produk])
            setvar.list_riwayat_transaksi["detail_pengiriman"].append(setvar.list_produk["detail_pengiriman"][indeks_list_produk])
            setvar.list_riwayat_transaksi["jumlah_pesanan"].append(jumlah_pesanan)
            setvar.list_riwayat_transaksi["total_harga"].append(total_harga)
            setvar.list_riwayat_transaksi["uang_bayar"].append(uang_bayar)
            setvar.list_riwayat_transaksi["kembalian"].append(kembalian)
            setvar.list_hasil_pemesanan["jumlah_pesanan"].append(jumlah_pesanan)
            setvar.list_hasil_pemesanan["uang_bayar"].append(uang_bayar)
            setvar.list_hasil_pemesanan["kembalian"].append(kembalian)
            setvar.list_produk["stok_produk"][indeks_list_produk] = int(setvar.list_produk["stok_produk"][indeks_list_produk]) - int(jumlah_pesanan)
    struk_pembelian(menu_utama_pengguna, jumlah_pesanan, total_harga)
def struk_pembelian(menu_utama_pengguna, jumlah_pesanan, total_harga):
    indeks_list_produk = setlpr.indeks_list_produk
    print("=" * 40)
    print("             STRUK PEMBELIAN             ")
    print("=" * 40)
    print(f"Nama Produk: {setvar.list_produk['nama_produk'][indeks_list_produk]}")
    print(f"Harga Produk: Rp{setvar.list_produk['harga_produk'][indeks_list_produk]}")
    print(f"Banyak Pesanan: {jumlah_pesanan}")
    print(f"Total Harga: {total_harga}")
    print(f"Nominal Pembayaran: {uang_bayar}")
    print(f"Kembalian: Rp{kembalian}")
    print(f"Status Pesanan: {status_pesanan}")
    print("=" * 40)
    cek.tekan_kembali("Pembayaran berhasil!")
    menu_utama_pengguna()
