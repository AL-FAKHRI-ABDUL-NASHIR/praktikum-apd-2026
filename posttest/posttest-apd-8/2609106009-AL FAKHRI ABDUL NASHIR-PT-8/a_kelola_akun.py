import os
import inquirer

import fail_or_succeed as cek
import setup_variables as setvar

def tampilan_akun_admin():
    os.system("cls")
    print("=" * 40)
    print("             AKUN ADMIN             ")
    print("=" * 40)
    print(f"Username: {setvar.admin_username}")
    print(f"Password: {setvar.admin_password}")
    print(f"Simpanan Uang: {setvar.penyimpanan_uang_admin}")
    print("=" * 40)
def kelola_akun_admin(menu_utama_admin):
    tampilan_akun_admin()
    opsi = [
        inquirer.List("Opsi Pilih Kelola Akun Admin", message="Pilih Opsi", choices=["Ubah Username", "Ubah Password", "Kembali"])
    ]
    jawaban = inquirer.prompt(opsi)
    opsi_kelola_akun_admin = jawaban["Opsi Pilih Kelola Akun Admin"]
    if opsi_kelola_akun_admin == "Ubah Username":
        tampilan_akun_admin()
        setvar.admin_username = input("Masukkan Username Baru Admin: ")
        os.system("cls")
        cek.tekan_kembali("Username berhasil diganti!")
        kelola_akun_admin(menu_utama_admin)
    elif opsi_kelola_akun_admin == "Ubah Password":
        tampilan_akun_admin()
        setvar.admin_password = input("Masukkan Password Baru Admin: ")
        os.system("cls")
        cek.tekan_kembali("Password berhasil diganti!")
        kelola_akun_admin(menu_utama_admin)
    elif opsi_kelola_akun_admin == "Kembali":
        menu_utama_admin()