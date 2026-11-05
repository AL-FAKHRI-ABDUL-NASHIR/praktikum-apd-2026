import os
import time
import inquirer
import maskpass

import fail_or_succeed as cek
import setup_variables as setvar
import autentikasi_setup as autentset

# Menu Masuk > Log In
def menu_log_in(menu_utama_admin, menu_utama_pengguna, menu_masuk):
    os.system("cls")
    global username_log_in, password_log_in
    print("Tekan Ctrl Kiri untuk Ubah Tampilan Password")
    print("=" * 40)
    print("              LOG IN AKUN              ")
    print("=" * 40)
    username_log_in = input("Masukkan Username : ") 
    print("Masukkan Password : ", end="")
    password_log_in = maskpass.advpass(prompt="", mask="*")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Masuk Akun", message="Masuk?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    masuk_akun = jawaban["Opsi Masuk Akun"]
    if masuk_akun == "Ya":
        if autentset.log_in_admin(username_log_in, password_log_in):
            os.system("cls")
            cek.tekan_lanjut("Login berhasil!")
            menu_utama_admin()
        elif autentset.log_in_pengguna(username_log_in, password_log_in):
            os.system("cls")
            cek.tekan_lanjut("Login berhasil!")
            menu_utama_pengguna()
        else:
            cek.kesalahan("=====Login gagal. Silakan coba lagi.=====")
            menu_masuk()
    elif masuk_akun == "Tidak":
        menu_masuk()

# Menu Masuk > Log In
def menu_sign_in(menu_masuk):
    os.system("cls")
    print("=" * 40)
    print("              SIGN IN AKUN              ")
    print("=" * 40)
    global username_sign_in, password_sign_in
    username_sign_in = input("Masukkan Username : ")
    password_sign_in = input("Masukkan Password : ")
    print("=" * 40)
    opsi = [
        inquirer.List("Opsi Simpan Akun", message="Simpan akun?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    simpan_akun = jawaban["Opsi Simpan Akun"]
    if simpan_akun == "Ya":
        if username_sign_in in setvar.data_akun or username_sign_in == setvar.admin_username:
            cek.kesalahan("=====Username ini sudah digunakan. Silahkan masukkan kembali.=====")
            time.sleep(1)
            menu_masuk()
        else:
            setvar.data_akun.setdefault(username_sign_in, password_sign_in)
            os.system("cls")
            cek.tekan_lanjut("Akun berhasil dibuat!")
            menu_masuk()
    elif simpan_akun == "Tidak":
        menu_masuk()
