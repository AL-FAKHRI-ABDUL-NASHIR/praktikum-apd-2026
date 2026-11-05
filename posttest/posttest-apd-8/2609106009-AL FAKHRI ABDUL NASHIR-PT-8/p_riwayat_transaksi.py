import os
import inquirer

import fail_or_succeed as cek
import setup_variables as setvar
import p_riwayat_transaksi_setup as priwtransset

def riwayat_transaksi(menu_utama_pengguna):
    os.system("cls")
    print("=" * 40)
    print("             RIWAYAT TRANSAKSI             ")
    print("=" * 40)
    riwayat_transaksi_test = setvar.list_riwayat_transaksi.get("nama_produk")
    if not riwayat_transaksi_test:
        cek.tekan_kembali("Anda belum melakukan pemesanan.")
        menu_utama_pengguna()
    else:
        for produk in setvar.list_riwayat_transaksi["nama_produk"]:
            print(f"— {produk}")
        opsi = [
            inquirer.List("Opsi Riwayat Transaksi", message="Pilih Opsi", choices=["Lihat Riwayat Transaksi Produk", "Hapus Semua Riwayat Transaksi", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        opsi_riwayat_transaksi = jawaban["Opsi Riwayat Transaksi"]
        if opsi_riwayat_transaksi == "Lihat Riwayat Transaksi Produk":
            priwtransset.lihat_riwayat(riwayat_transaksi)
        elif opsi_riwayat_transaksi == "Hapus Semua Riwayat Transaksi":
            while True:
                os.system("cls")
                print("=" * 40)
                print("             RIWAYAT TRANSAKSI             ")
                print("=" * 40)
                for produk in setvar.list_riwayat_transaksi["nama_produk"]:
                    print(f"— {produk}")
                print("=" * 40)
                opsi = [
                    inquirer.List("Opsi Hapus Riwayat Transaksi", message="Apakah Anda yakin ingin menghapus semua riwayat transaksi?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                hapus_riwayat_transaksi = jawaban["Opsi Hapus Riwayat Transaksi"]
                os.system("cls")
                if hapus_riwayat_transaksi == "Ya":
                    for data in setvar.list_riwayat_transaksi.values():
                        data.clear()
                    cek.tekan_kembali("Riwayat transaksi berhasil dihapus")
                    menu_utama_pengguna()
                    break
                elif hapus_riwayat_transaksi == "Tidak":
                    riwayat_transaksi()
                    break
        elif opsi_riwayat_transaksi == "Kembali":
            menu_utama_pengguna()
