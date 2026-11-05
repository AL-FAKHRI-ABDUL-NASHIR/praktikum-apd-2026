import os
import inquirer

import setup_variables as setvar
import fail_or_succeed as cek

def tampilan_riwayat_transaksi():
    global indeks_list_riwayat_transaksi
    indeks_list_riwayat_transaksi = setvar.list_riwayat_transaksi['nama_produk'].index(pilih_produk)
    os.system('cls')
    print('=' * 40)
    print('             RIWAYAT TRANSAKSI             ')
    print('=' * 40)
    print(f'Nama Produk: {setvar.list_riwayat_transaksi["nama_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Harga Produk: Rp{setvar.list_riwayat_transaksi["harga_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Kategori Produk: {setvar.list_riwayat_transaksi["kategori_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Detail Produk: {setvar.list_riwayat_transaksi["detail_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Deskripsi Produk: {setvar.list_riwayat_transaksi["deskripsi_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Kondisi Produk: {setvar.list_riwayat_transaksi["kondisi_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Berat Produk: {setvar.list_riwayat_transaksi["berat_produk"][indeks_list_riwayat_transaksi]}')
    print(f'Detail Pengiriman: {setvar.list_riwayat_transaksi["detail_pengiriman"][indeks_list_riwayat_transaksi]}')
    print(f'Banyak Pesanan: {setvar.list_riwayat_transaksi["jumlah_pesanan"][indeks_list_riwayat_transaksi]}')
    print(f'Total Harga: {setvar.list_riwayat_transaksi["total_harga"][indeks_list_riwayat_transaksi]}')
    print(f'Nominal Pembayaran: {setvar.list_riwayat_transaksi["uang_bayar"][indeks_list_riwayat_transaksi]}')
    print(f'Kembalian: Rp{setvar.list_riwayat_transaksi["kembalian"][indeks_list_riwayat_transaksi]}')
    print('=' * 40)
def lihat_riwayat(riwayat_transaksi):
    os.system('cls')
    print('=' * 40)
    print('             RIWAYAT TRANSAKSI             ')
    print('=' * 40)
    for produk in setvar.list_riwayat_transaksi['nama_produk']:
        print(f'— {produk}')
    print('=' * 40)
    global pilih_produk
    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
# Menampilkan Informasi Produk
    for produk in setvar.list_riwayat_transaksi['nama_produk']:
        list_riwayat_transaksi_test = setvar.list_riwayat_transaksi['nama_produk'].index(produk)
        if setvar.list_riwayat_transaksi['nama_produk'][list_riwayat_transaksi_test] == pilih_produk.strip():
            while True:
                tampilan_riwayat_transaksi()
                opsi = [
                    inquirer.List("Opsi Komentar", message="'Pilih Opsi", choices=["Kirim Komentar", "Kembali"])
                ]
                jawaban = inquirer.prompt(opsi)
                opsi_komentar = jawaban["Opsi Komentar"]
                os.system('cls')
                if opsi_komentar == "Kirim Komentar":
                    
                    for produk_komentar in setvar.halaman_komentar['nama_produk']:
                        if produk_komentar == setvar.list_riwayat_transaksi['nama_produk'][setvar.list_riwayat_transaksi['nama_produk'].index(pilih_produk.strip())]:
                            komentar_pengguna = f'({setvar.username_log_in}: \n)' + input('Masukkan tanggapan: ')
                            setvar.halaman_komentar['nama_produk'].append(setvar.list_riwayat_transaksi['nama_produk'][setvar.list_riwayat_transaksi['nama_produk'].index(pilih_produk.strip())])
                            setvar.halaman_komentar['komentar_produk'].append(komentar_pengguna)
                    riwayat_transaksi()
                    break
                elif opsi_komentar == "Kembali":
                    riwayat_transaksi()
                    break
                return True
    # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
    os.system('cls')
    cek.tekan_kembali("Produk tidak ditemukan.")
    return False
