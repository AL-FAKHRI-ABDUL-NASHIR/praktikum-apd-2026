import os

import fail_or_succeed as cek
import setup_variables as setvar

def tampilan_list_pesanan(keterangan_menu, keterangan_akun):
    global test_daftar_pesanan
    os.system("cls")
    print("=" * 40)
    print(keterangan_menu)
    print("=" * 40)
    if not setvar.list_pesanan["nama_produk"]:
        cek.tekan_kembali(keterangan_akun)
        return False
    else:
        for produk in setvar.list_pesanan["nama_produk"]:
            list_pesanan_test = setvar.list_pesanan["nama_produk"].index(produk)
            print(f"— {produk}, Status: {setvar.list_pesanan["status_pesanan"][list_pesanan_test]}")
        return True
def tampilan_daftar_pesanan(pilih_produk):
    os.system('cls')
    global indeks_list_pesanan
    for produk in setvar.list_pesanan["nama_produk"]:
        if produk == pilih_produk.strip():
            indeks_list_pesanan = setvar.list_pesanan["nama_produk"].index(produk)
    print('=' * 40)
    print('             DAFTAR PESANAN             ')
    print('=' * 40)
    print(f'Nama Produk: {setvar.list_pesanan["nama_produk"][indeks_list_pesanan]}')
    print(f'Harga Produk: Rp{setvar.list_pesanan["harga_produk"][indeks_list_pesanan]}')
    print(f'Kategori Produk: {setvar.list_pesanan["kategori_produk"][indeks_list_pesanan]}')
    print(f'Detail Produk: {setvar.list_pesanan["detail_produk"][indeks_list_pesanan]}')
    print(f'Deskripsi Produk: {setvar.list_pesanan["deskripsi_produk"][indeks_list_pesanan]}')
    print(f'Kondisi Produk: {setvar.list_pesanan["kondisi_produk"][indeks_list_pesanan]}')
    print(f'Berat Produk: {setvar.list_pesanan["berat_produk"][indeks_list_pesanan]}')
    print(f'Detail Pengiriman: {setvar.list_pesanan["detail_pengiriman"][indeks_list_pesanan]}')
    print(f'Status Pesanan: {setvar.list_pesanan["status_pesanan"][indeks_list_pesanan]}')
    print('=' * 40)
