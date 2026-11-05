import os
import sys; sys.setrecursionlimit(10000)
import inquirer

import autentikasi as autent
import a_produk as apro
import a_pesanan as apes
import a_kelola_akun as akelakun
import p_produk as ppro
import p_keranjang_belanja as pkerbel
import p_pesanan as ppes
import p_riwayat_transaksi as priwtrans
import p_kelola_akun as pkelakun

def menu_masuk():
    os.system("cls")
    print("=" * 40)
    print("         SELAMAT DATANG DI TOKO         ")
    print("=" * 40)
    print("Silakan Masuk Terlebih Dahulu")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Pilih Masuk", message="Pilih Opsi", choices=["Log In", "Sign In", "Keluar"])
    ]
    jawaban = inquirer.prompt(opsi)
    pilih_masuk = jawaban["Opsi Pilih Masuk"]
    if pilih_masuk == "Log In":
        autent.menu_log_in(menu_utama_admin, menu_utama_pengguna, menu_masuk)
    elif pilih_masuk == "Sign In":
        autent.menu_sign_in(menu_masuk)
    elif pilih_masuk == "Keluar":
        os.system("cls")
        print("=" * 50)
        print("Terimakasih karena telah menggunakan layanan kami.")
        print("=" * 50)
        exit()

# AKUN ADMIN #
# Menu Utama
def menu_utama_admin():
    os.system("cls")
    print("=" * 40)
    print("               MENU UTAMA               ")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Pilih Menu Utama Admin", message="Pilih Menu", choices=["Produk", "Pesanan", "Kelola Akun", "Log Out"])
    ]
    jawaban = inquirer.prompt(opsi)
    pilih_menu_utama_admin = jawaban["Opsi Pilih Menu Utama Admin"]
    print("=" * 40)
    if pilih_menu_utama_admin == "Produk":
        apro.menu_produk(menu_utama_admin)
    elif pilih_menu_utama_admin == "Pesanan":
        apes.menu_pesanan(menu_utama_admin)
    elif pilih_menu_utama_admin == "Kelola Akun":
        akelakun.kelola_akun_admin(menu_utama_admin)
    elif pilih_menu_utama_admin == "Log Out":
        menu_masuk()

# AKUN PENGGUNA #
# Menu Utama (Pengguna)
def menu_utama_pengguna():
    os.system("cls")
    print("=" * 40)
    print("               MENU UTAMA               ")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Pilih Menu Utama Pengguna", message="Pilih Opsi", choices=["Halaman Produk", "Keranjang Belanja", "Daftar Pesanan", "Riwayat Transaksi", "Kelola Akun", "Log Out"])
    ]
    jawaban = inquirer.prompt(opsi)
    pilih_menu_utama_pengguna = jawaban["Opsi Pilih Menu Utama Pengguna"]
    if pilih_menu_utama_pengguna == "Halaman Produk":
        ppro.halaman_produk(menu_utama_pengguna)
    elif pilih_menu_utama_pengguna == "Keranjang Belanja":
        pkerbel.keranjang_belanja(menu_utama_pengguna)
    elif pilih_menu_utama_pengguna == "Daftar Pesanan":
        ppes.daftar_pesanan(menu_utama_pengguna)
    elif pilih_menu_utama_pengguna == "Riwayat Transaksi":
        priwtrans.riwayat_transaksi(menu_utama_pengguna)
    elif pilih_menu_utama_pengguna == "Kelola Akun":
        pkelakun.kelola_akun_pengguna(menu_utama_pengguna)
    elif pilih_menu_utama_pengguna == "Log Out":
        menu_masuk()


menu_masuk()