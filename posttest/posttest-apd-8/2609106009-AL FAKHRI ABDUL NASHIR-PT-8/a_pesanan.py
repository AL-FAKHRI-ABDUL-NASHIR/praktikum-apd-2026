import os
import inquirer
from prettytable import PrettyTable, ALL

import fail_or_succeed as cek
import setup_variables as setvar
import setup_list_pesanan as setlpe
import a_pesanan_setup as apesset

def menu_pesanan(menu_utama_admin):
    global list_pesanan_test
    list_produk_test = setvar.list_pesanan.get("nama_produk")
    if not list_produk_test:
        os.system("cls")
        print("=" * 40)
        print("             MENU PESANAN             ")
        print("=" * 40)
        cek.tekan_kembali("Belum ada pesanan.")
        menu_utama_admin()
    else:
        os.system("cls")
        print("=" * 40)
        print("             MENU PESANAN             ")
        print("=" * 40)
        tabel = PrettyTable()
        tabel.hrules = ALL
        tabel.field_names = ["Nama Produk"]
        for produk in setvar.list_pesanan["nama_produk"]:
            tabel.add_row([produk, setvar.list_pesanan["status_pesanan"]])
        tabel.add_autoindex("No")
        tabel.align["No"] = "l"
        print(tabel)
        print("=" * 40)
        opsi = [
            inquirer.List("Opsi Pilih Menu Pesanan", message="Pilih Opsi", choices=["Edit Pesanan", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        opsi_menu_pesanan = jawaban["Opsi Pilih Menu Pesanan"]
        if opsi_menu_pesanan == "Edit Pesanan":
            edit_pesanan(menu_utama_admin)
        elif opsi_menu_pesanan == "Kembali":
            menu_utama_admin()

def edit_pesanan(menu_utama_admin):
    status_pesanan = setlpe.tampilan_list_pesanan("             MENU PESANAN             ", "Belum ada yang memesan produk.")
    if status_pesanan:
        print("cls")
        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
        for produk in setvar.list_pesanan["nama_produk"]:
            if produk == pilih_produk.strip():
                indeks_list_pesanan = setvar.list_pesanan["nama_produk"].index(produk)
        apesset.informasi_pesanan(pilih_produk)
        opsi = [
            inquirer.List("Opsi Pilih Edit Status Pesanan", message="Edit Status Pesanan?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        opsi_edit_status = jawaban["Opsi Pilih Edit Status Pesanan"]
        if opsi_edit_status == "Ya":
            if setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] == "Pembatalan telah diajukan.":
                apesset.informasi_pesanan(pilih_produk)
                opsi = [
                    inquirer.List("Opsi Pilih Pembatalan Pesanan", message="Pilih Opsi", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                opsi_pembatalan = jawaban["Opsi Pilih Pembatalan Pesanan"]
                if opsi_pembatalan == "Ya":
                    apesset.terima_pengajuan_batal(pilih_produk)
                    cek.tekan_kembali("Pengajuan pembatalan diterima.")
                    menu_pesanan(menu_utama_admin)
                elif opsi_pembatalan == "Tidak":
                    apesset.tolak_pengajuan_batal(pilih_produk)
                    cek.tekan_kembali("Pengajuan pembatalan ditolak")
                    menu_pesanan(menu_utama_admin)
            else:
                apesset.informasi_pesanan(pilih_produk)
                setvar.list_pesanan["status_pesanan"][indeks_list_pesanan] = input("Ubah Status Pesanan: ")
                apesset.informasi_pesanan(pilih_produk)
                cek.tekan_kembali("Status pesanan berhasil diubah!")
                menu_pesanan(menu_utama_admin)
        elif opsi_edit_status == "Tidak":
            menu_pesanan(menu_utama_admin)
    