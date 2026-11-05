import os
import inquirer

import fail_or_succeed as cek
import setup_variables as setvar

def tampilan_akun_pengguna(username_log_in, password_log_in):
    os.system('cls')
    print('=' * 40)
    print('             AKUN PENGGUNA             ')
    print('=' * 40)
    print(f'Username: {username_log_in}')
    print(f'Password: {password_log_in}')
    print('=' * 40)

def kelola_akun_pengguna(menu_utama_pengguna):
    global username_log_in, password_log_in
    tampilan_akun_pengguna(username_log_in, password_log_in)
    opsi = [
        inquirer.List("Opsi Kelola Akun Pengguna", message="Pilih Opsi", choices=["Ubah Username", "Ubah Password", "Kembali"])
    ]
    jawaban = inquirer.prompt(opsi)
    opsi_kelola_akun_pengguna = jawaban["Opsi Kelola Akun Pengguna"]
    if opsi_kelola_akun_pengguna == "Ubah Username":
        user_edit = False
        for data_edit in setvar.data_akun:
            if data_edit == username_log_in:
                user_edit = True
        if user_edit:
            while True:
                tampilan_akun_pengguna(username_log_in, password_log_in)
                username_baru = input("Masukkan Username Baru: ")
                if username_baru in setvar.data_akun:
                    cek.kesalahan("=====Username ini sudah digunakan. Silahkan masukkan kembali.=====")
                else:
                    del setvar.data_akun[username_log_in]
                    setvar.data_akun.update({username_baru : setvar.password_log_in})
                    username_log_in = username_baru
                    os.system("cls")
                    cek.tekan_kembali("Username berhasil diganti!")
                kelola_akun_pengguna(menu_utama_pengguna)
                break
    elif opsi_kelola_akun_pengguna == "Ubah Password":
        for data_edit in setvar.data_akun:   
            if data_edit == username_log_in:
                tampilan_akun_pengguna(username_log_in, password_log_in)
                password_baru = input("Masukkan Password Baru: ")
                setvar.data_akun[setvar.username_log_in] = password_baru
                password_log_in = password_baru
                os.system("cls")
                cek.tekan_kembali("Password berhasil diganti!")
                kelola_akun_pengguna(menu_utama_pengguna)
    elif opsi_kelola_akun_pengguna == "Kembali":
        menu_utama_pengguna()
