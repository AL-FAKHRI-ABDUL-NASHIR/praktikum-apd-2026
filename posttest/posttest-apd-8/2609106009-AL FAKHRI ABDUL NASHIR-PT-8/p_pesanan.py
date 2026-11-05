import os
import inquirer

import fail_or_succeed as cek
import setup_variables as setvar
import setup_list_pesanan as setlpe

def daftar_pesanan(menu_utama_pengguna):
    status_pesanan = setlpe.tampilan_list_pesanan("             DAFTAR PESANAN             ", "Anda belum memesan produk")
    if not status_pesanan:
        menu_utama_pengguna()
    else:
        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
        for produk in setvar.list_pesanan["nama_produk"]:
            if produk == pilih_produk.strip():
                indeks_list_pesanan = setvar.list_pesanan["nama_produk"].index(produk)
        if setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] == "Pembatalan telah diajukan.":
            indeks_list_pesanan = setvar.list_pesanan['nama_produk'].index(produk)
            setlpe.tampilan_daftar_pesanan(pilih_produk)
            opsi = [
                inquirer.List("Opsi Daftar Pesanan", message="Pilih Opsi", choices=["Tarik Pengajuan Pembatalan", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            opsi_daftar_pesanan = jawaban["Opsi Daftar Pesanan"]
            if opsi_daftar_pesanan == "Tarik Pengajuan Pembatalan":
                setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] = "Menunggu"
                cek.tekan_kembali("Pengajuan telah ditarik.")
                menu_utama_pengguna()
            elif opsi_daftar_pesanan == "Kembali":
                menu_utama_pengguna()
        else:
            setlpe.tampilan_daftar_pesanan(pilih_produk)
            opsi = [
                inquirer.List("Opsi Pengajuan Pembatalan", message="Pilih Opsi", choices=["Batalkan Pesanan", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            opsi_daftar_pesanan = jawaban["Opsi Pengajuan Pembatalan"]
            if opsi_daftar_pesanan == "Batalkan Pesanan":
                if setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] == "Menunggu":
                    setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] = "Pembatalan telah diajukan."
                    os.system("cls")
                    cek.tekan_kembali("Menunggu konfirmasi dari toko...")
                    menu_utama_pengguna()
                else:
                    os.system("cls")
                    cek.tekan_kembali("Pesanan telah diproses. Anda tidak bisa mengajukan pembatalan.")
                    menu_utama_pengguna()
            elif opsi_daftar_pesanan == "Kembali":
                menu_utama_pengguna()