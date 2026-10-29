import os
import time
import sys; sys.setrecursionlimit(10000)

# Database Akun
data_akun = {}

# Database Admin
admin_username = "Al Fakhri AN"
admin_password = "2609106009"
penyimpanan_uang_admin = 0

# Database Produk
list_produk = {
    'nama_produk' : [],
    'harga_produk' : [],
    'kategori_produk' : [],
    'detail_produk' : [],
    'deskripsi_produk' : [],
    'kondisi_produk' : [],
    'stok_produk' : [],
    'berat_produk' : [],
    'detail_pengiriman' : []
}

# Database Keranjang Belanja
list_keranjang_belanja = {}

# Database Pesanan
list_pesanan = {
    'nama_produk' : [],
    'harga_produk' : [],
    'kategori_produk' : [],
    'detail_produk' : [],
    'deskripsi_produk' : [],
    'kondisi_produk' : [],
    'stok_produk' : [],
    'berat_produk' : [],
    'detail_pengiriman' : [],
    'status_pesanan' : []
}

# Database Hasil Perhitungan Pemesanan
list_hasil_pemesanan = {
    'jumlah_pesanan' : [],
    'uang_bayar' : [],
    'kembalian' : []
}

# Database Riwayat Transaksi
list_riwayat_transaksi = {
    'nama_produk' : [],
    'harga_produk' : [],
    'kategori_produk' : [],
    'detail_produk' : [],
    'deskripsi_produk' : [],
    'kondisi_produk' : [],
    'stok_produk' : [],
    'berat_produk' : [],
    'detail_pengiriman' : [],
    'jumlah_pesanan' : [],
    'total_harga' : [],
    'uang_bayar' : [],
    'kembalian' : []
}


# Database Komentar
halaman_komentar = {
    'nama_produk' : [],
    'komentar_produk' : []
}

# Variabel Kosong
username_log_in = None
password_log_in = None
list_pesanan_test = False


# Persiapan Fungsi Untuk Seluruh Program
def tekan_lanjut(keterangan_lanjut):
    print(keterangan_lanjut)
    print('=' * 40)
    lanjut = input('Tekan Enter Untuk Lanjut')
def tekan_kembali(keterangan_kembali):
    print(keterangan_kembali)
    print('=' * 40)
    kembali = input('Tekan Enter Untuk Kembali')
def kesalahan(keterangan_kesalahan):
    os.system('cls')
    print(keterangan_kesalahan)
    time.sleep(1)



# Menu Masuk
def menu_masuk():
    os.system('cls')
    print('=' * 40)
    print("         SELAMAT DATANG DI TOKO         ")
    print('=' * 40)
    print("Silakan Masuk Terlebih Dahulu")
    print("1. Log In")
    print("2. Sign In")
    print("3. Keluar")
    pilih_masuk = input("Pilih Opsi (1/2/3): ")
    # Melanjutkan Program ke Menu Log In
    if pilih_masuk.strip() == "1":
        menu_log_in()
    # Melanjutkan Program ke Menu Sign in
    elif pilih_masuk.strip() == "2":
        menu_sign_in()
    # Mengakhiri Program
    elif pilih_masuk.strip() == "3":
        return True
    # Mengulang Program ke Menu Masuk Karena Salah Input
    else:
        kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
        menu_masuk()

# {Persiapan Ketentuan Log In}
def log_in_admin():
    if username_log_in == admin_username and password_log_in == admin_password:
        return True
    return False
def log_in_pengguna():
    for data_test in data_akun:
        if username_log_in == data_test and password_log_in == data_akun[data_test]:
            return True
    return False

# Menu Masuk > Log In
def menu_log_in():
    os.system('cls')
    print('=' * 40)
    print("              LOG IN AKUN              ")
    print('=' * 40)
    global username_log_in, password_log_in
    username_log_in = input("Masukkan Username : ")
    password_log_in = input("Masukkan Password : ")
    log_in = input("Masuk? (Ya/Tidak): ")
    if log_in.strip().lower() == "ya":
        if log_in_admin():
            os.system('cls')
            tekan_lanjut("Login berhasil!")
            menu_utama_admin()
        elif log_in_pengguna():
            os.system('cls')
            tekan_lanjut("Login berhasil!")
            menu_utama_pengguna()
        else:
            kesalahan('=====Login gagal. Silakan coba lagi.=====')
            menu_masuk()
    elif log_in.strip().lower() == "tidak":
        menu_masuk()
    else:
        kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
        menu_masuk()


    

# Menu Masuk > Log In
def menu_sign_in():
    os.system('cls')
    print('=' * 40)
    print("              SIGN IN AKUN              ")
    print('=' * 40)
    global username_sign_in, password_sign_in, data_akun
    username_sign_in = input("Masukkan Username : ")
    password_sign_in = input("Masukkan Password : ")
    simpan_akun = input("Simpan akun? (Ya/Tidak): ")
    if simpan_akun.strip().lower() == "ya":
        if username_sign_in in data_akun:
            kesalahan('=====Username ini sudah digunakan. Silahkan masukkan kembali.=====')
            menu_masuk()
        else:
            data_akun.setdefault(username_sign_in, password_sign_in)
            os.system('cls')
            tekan_lanjut("Akun berhasil dibuat!")
            menu_masuk()
    elif simpan_akun.strip().lower() == "tidak":
        menu_masuk()
    else:
        kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
        menu_masuk()




# AKUN ADMIN #
# Menu Utama
def menu_utama_admin():
    os.system('cls')
    print('=' * 40)
    print('               MENU UTAMA               ')
    print('=' * 40)
    print('1. Produk')
    print('2. Pesanan')
    print('3. Kelola Akun')
    print('4. Log Out')
    print('=' * 40)
    pilihan_menu = input('Pilih Menu (1/2/3/4): ')
    if pilihan_menu.strip() == '1':
        menu_produk()
    elif pilihan_menu.strip() == '2':
        menu_pesanan()
    elif pilihan_menu.strip() == '3':
        kelola_akun_admin()
    elif pilihan_menu.strip() == '4':
        menu_masuk()
    else:
        kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
        menu_utama_admin()

def menu_produk():
    os.system('cls')
    print('=' * 40)
    print('               MENU PRODUK               ')
    print('=' * 40)
    print('1. Daftar Produk')
    print('2. Tambah Produk')
    print('3. Hapus Produk')
    print('4. Kembali')
    print('=' * 40)
    pilihan_menu_produk =  input('Pilih Menu (1/2/3/4): ')
    if pilihan_menu_produk.strip() == '1':
        daftar_produk()
    elif pilihan_menu_produk.strip() == '2':
        tambah_produk()
    elif pilihan_menu_produk.strip() == '3':
        hapus_produk()
    elif pilihan_menu_produk.strip() == '4':
        menu_utama_admin()
    else:
        kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
        menu_produk()

# {Persiapan Test List Produk}
def test_list_produk(keterangan_menu):
    os.system('cls')
    print('=' * 40)
    print(keterangan_menu)
    print('=' * 40)
    list_produk_test = list_produk.get('nama_produk')
    if not list_produk_test:
        tekan_kembali("Belum ada produk yang ditambahkan.")
        menu_produk()
        return False
    else:
        for produk in list_produk['nama_produk']:
            print(f'— {produk}')
# {Persiapan Tampilan Produk}
def tampilan_produk(keterangan_menu):
    os.system('cls')
    for produk in list_produk['nama_produk']:
        list_produk_test = list_produk['nama_produk'].index(produk)
        if list_produk['nama_produk'][list_produk_test] == pilih_produk.strip():
            global indeks_list_produk
            indeks_list_produk = list_produk['nama_produk'].index(pilih_produk)
            print('=' * 40)
            print(keterangan_menu)
            print('=' * 40)
            print(f'Nama Produk: {list_produk['nama_produk'][indeks_list_produk]}')
            print(f'Harga Produk: Rp{list_produk['harga_produk'][indeks_list_produk]}')
            print(f'Kategori Produk: {list_produk['kategori_produk'][indeks_list_produk]}')
            print(f'Detail Produk: {list_produk['detail_produk'][indeks_list_produk]}')
            print(f'Deskripsi Produk: {list_produk['deskripsi_produk'][indeks_list_produk]}')
            print(f'Kondisi Produk: {list_produk['kondisi_produk'][indeks_list_produk]}')
            print(f'Stok Produk: {list_produk['stok_produk'][indeks_list_produk]}')
            print(f'Berat Produk: {list_produk['berat_produk'][indeks_list_produk]}')
            print(f'Detail Pengiriman: {list_produk['detail_pengiriman'][indeks_list_produk]}')
            print('=' * 40)
            return True
    os.system('cls')
    tekan_kembali("Produk tidak ditemukan.")
    return False
# {Persiapan Tampilan Komentar}
def tampilan_komentar():
    for produk_komen in halaman_komentar['nama_produk']:
        if produk_komen == list_produk['nama_produk'][indeks_list_produk]:
            isi_komentar = halaman_komentar['komentar_produk'].index(produk_komen)
            print(produk_komen)
            print(produk_komen[isi_komentar])

def daftar_produk():
    test_list_produk('             DAFTAR PRODUK             ')
    global pilih_produk
    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
    tampilan_produk('             DAFTAR PRODUK             ')
    if tampilan_produk:
        tampilan_produk('             DAFTAR PRODUK             ')
        print('1. Kembali Ke Menu Produk')
        print('2. Kembali Ke Daftar Produk')
        kembali = input('Pilih Opsi (1/2): ')
        if kembali.strip().lower() == '1':
            menu_produk()
        elif kembali.strip().lower() == '2':
            daftar_produk()
        else:
            kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
            daftar_produk()
    else:
        menu_produk()

# {Persiapan Error-Handling Tambah Produk}
def test_angka():
    print('=' * 40)
    print('             TAMBAH PRODUK             ')
    print('=' * 40)
    print('=' * 40)
    print('            INFORMASI PRODUK            ')
    print('=' * 40)
    print(f'Masukkan Nama Produk: {nama_produk}')
    if not test_harga:
        return False
    print(f'Masukkan Harga Produk (Rp): {harga_produk}')
    if not test_harga_selesai:
        return True
    print(f'Masukkan Kategori Produk: {kategori_produk}')
    print(f'Masukkan Detail Produk: {detail_produk}')
    print(f'Masukkan Deskripsi Produk: {deskripsi_produk}')
    print(f'Masukkan Kondisi Produk (Baru/Bekas): {kondisi_produk}')
    print('=' * 40)
    print('             BANYAK PRODUK             ')
    print('=' * 40)
    if not test_stok:
        return False
    print(f'Masukkan Stok Produk: {stok_produk}')
    if not test_stok_selesai:
        return True
    print('=' * 40)
    print('             PENGIRIMAN PRODUK             ')
    print('=' * 40)
    if not test_berat:
        return False
    print(f'Masukkan Berat Produk (gram): {berat_produk}')
    if not test_berat_selesai:
        return True

def tambah_produk():
    global nama_produk, harga_produk, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, stok_produk, berat_produk, detail_pengiriman, test_harga, test_harga_selesai, test_stok, test_stok_selesai, test_berat, test_berat_selesai
    os.system('cls')
    print('=' * 40)
    print('             TAMBAH PRODUK             ')
    print('=' * 40)
    print('=' * 40)
    print('            INFORMASI PRODUK            ')
    print('=' * 40)
    nama_produk = input('Masukkan Nama Produk: ')
    os.system('cls')
    while True:
        try:
            test_harga = False
            test_angka()
            harga_produk = int(input('Masukkan Harga Produk (Rp): '))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            test_harga = True
            test_harga_selesai = False
            test_angka()
            break
    test_harga_selesai = True
    kategori_produk = input('Masukkan Kategori Produk: ')
    detail_produk = input('Masukkan Detail Produk: ')
    deskripsi_produk = input('Masukkan Deskripsi Produk: ')
    kondisi_produk = input('Masukkan Kondisi Produk (Baru/Bekas): ')
    print('=' * 40)
    print('             BANYAK PRODUK             ')
    print('=' * 40)
    os.system('cls')
    while True:
        try:
            test_stok = False
            test_angka()
            stok_produk = int(input('Masukkan Stok Produk: '))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            test_stok = True
            test_stok_selesai = False
            test_angka()
            break
    test_stok_selesai = True
    print('=' * 40)
    print('             PENGIRIMAN PRODUK             ')
    print('=' * 40)
    os.system('cls')
    while True:
        try:
            test_berat = False
            test_angka()
            berat_produk = int(input('Masukkan Berat Produk (gram): '))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            test_berat = True
            test_berat_selesai = False
            test_angka()
            break
    test_berat_selesai = True
    detail_pengiriman = input('Masukkan Detail Pengiriman: ')
    konfirmasi_tambah_produk()

def konfirmasi_tambah_produk():
    os.system('cls')
    print('=' * 40)
    print('         DATA PRODUK YANG DITAMBAHKAN         ')
    print('=' * 40)
    print(f'Nama Produk: {nama_produk}')
    print(f'Harga Produk: {harga_produk}')
    print(f'Kategori Produk: {kategori_produk}')
    print(f'Detail Produk: {detail_produk}')
    print(f'Deskripsi Produk: {deskripsi_produk}')
    print(f'Kondisi Produk: {kondisi_produk}')
    print(f'Stok Produk: {stok_produk}')
    print(f'Berat Produk: {berat_produk}')
    print(f'Detail Pengiriman: {detail_pengiriman}')
    print('=' * 40)
    simpan_kembali = input('Simpan dan Kembali? (Ya/Tidak): ')
    if simpan_kembali.strip().lower() == 'ya':
        os.system('cls')
        list_produk['nama_produk'].append(nama_produk)
        list_produk['harga_produk'].append(harga_produk)
        list_produk['kategori_produk'].append(kategori_produk)
        list_produk['detail_produk'].append(detail_produk)
        list_produk['deskripsi_produk'].append(deskripsi_produk)
        list_produk['kondisi_produk'].append(kondisi_produk)
        list_produk['stok_produk'].append(stok_produk)
        list_produk['berat_produk'].append(berat_produk)
        list_produk['detail_pengiriman'].append(detail_pengiriman)
        tekan_kembali('Produk berhasil ditambahkan!')
        menu_produk()
    elif simpan_kembali.strip().lower() == 'tidak':
        while True:
            os.system('cls')
            print('Pengisian dibatalkan.')
            print('=' * 40)
            pengulangan = input('Apakah Anda ingin mengisi ulang data produk? (Ya/Tidak): ')
            if pengulangan.strip().lower() == 'ya':
                tambah_produk()
                break
            elif pengulangan.strip().lower() == 'tidak':
                menu_produk()
                break
            else:
                kesalahan('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
    else:
        kesalahan('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
        konfirmasi_tambah_produk()

def hapus_produk():
    test_list_produk('             HAPUS PRODUK             ')
    global pilih_produk
    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
    while True:
        tampilan_produk('             HAPUS PRODUK             ')
        if tampilan_produk:
            pilih_hapus = input('Apakah Anda ingin menghapus produk ini? (Ya/Tidak): ')
            if pilih_hapus.strip().lower() == 'ya':
                os.system('cls')
                del list_produk['nama_produk'][indeks_list_produk]
                del list_produk['harga_produk'][indeks_list_produk]
                del list_produk['kategori_produk'][indeks_list_produk]
                del list_produk['detail_produk'][indeks_list_produk]
                del list_produk['deskripsi_produk'][indeks_list_produk]
                del list_produk['kondisi_produk'][indeks_list_produk]
                del list_produk['stok_produk'][indeks_list_produk]
                del list_produk['berat_produk'][indeks_list_produk]
                del list_produk['detail_pengiriman'][indeks_list_produk]
                tekan_kembali('Produk berhasil dihapus!')
                menu_produk()
                break
            elif pilih_hapus.strip().lower() == 'tidak':
                menu_produk()
                break
            else:
                kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
        else:
            menu_produk()
            break
            
def menu_pesanan():
    global list_pesanan_test
    list_produk_test = list_pesanan.get('nama_produk')
    if not list_produk_test:
        os.system('cls')
        print('=' * 40)
        print('             MENU PESANAN             ')
        print('=' * 40)
        tekan_kembali("Belum ada pesanan.")
        menu_utama_admin()
    else:
        os.system('cls')
        print('=' * 40)
        print('             MENU PESANAN             ')
        print('=' * 40)
        for produk in list_pesanan['nama_produk']:
            list_pesanan_test = list_pesanan['nama_produk'].index(produk)
            print(f'— {produk}, Status: {list_pesanan['status_pesanan'][list_pesanan_test]}')
        print('=' * 40)
        print('1. Edit Pesanan')
        print('2. Kembali')
        opsi_menu_pesanan = input('Pilih Opsi (1/2): ')
        if opsi_menu_pesanan == '1':
            edit_pesanan()
        elif opsi_menu_pesanan == '2':
            menu_utama_admin()
        else:
            kesalahan('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
            menu_pesanan()

# {Persiapan Tampilan Pesanan}
def tampilan_list_pesanan(keterangan_menu, keterangan_akun):
    global pilih_produk, indeks_list_pesanan, test_daftar_pesanan
    os.system('cls')
    print('=' * 40)
    print(keterangan_menu)
    print('=' * 40)
    if not list_pesanan_test:
        test_daftar_pesanan = False
        tekan_kembali(keterangan_akun)
    else:
        test_daftar_pesanan = True
        for produk in list_pesanan['nama_produk']:
            print(f'— {produk}, Status: {list_pesanan['status_pesanan'][list_pesanan_test]}')
        print('=' * 40)
        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
        for produk in list_pesanan['nama_produk']:
            if list_pesanan['nama_produk'][list_pesanan_test] == pilih_produk.strip():
                indeks_list_pesanan = list_pesanan['nama_produk'].index(pilih_produk)

def terima_pengajuan_batal():
    global penyimpanan_uang_admin
    for produk in list_produk['nama_produk']:
        if list_pesanan['nama_produk'][indeks_list_pesanan] == produk:
            indeks = list_produk['nama_produk'].index(produk)
    list_produk['stok_produk'][indeks] = int(list_produk['stok_produk'][indeks]) + int(list_hasil_pemesanan['jumlah_pesanan'][indeks_list_pesanan])
    penyimpanan_uang_admin = int(penyimpanan_uang_admin) + int(list_hasil_pemesanan['kembalian'][indeks_list_pesanan]) - int(list_hasil_pemesanan['uang_bayar'][indeks_list_pesanan])
    del list_pesanan['nama_produk'][indeks_list_pesanan]
    del list_pesanan['harga_produk'][indeks_list_pesanan]
    del list_pesanan['kategori_produk'][indeks_list_pesanan]
    del list_pesanan['detail_produk'][indeks_list_pesanan]
    del list_pesanan['deskripsi_produk'][indeks_list_pesanan]
    del list_pesanan['kondisi_produk'][indeks_list_pesanan]
    del list_pesanan['stok_produk'][indeks_list_pesanan]
    del list_pesanan['berat_produk'][indeks_list_pesanan]
    del list_pesanan['detail_pengiriman'][indeks_list_pesanan]
    del list_pesanan['status_pesanan'][indeks_list_pesanan]
    print('=' * 40)
    print('             MENU PESANAN             ')
    print('=' * 40)
    print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
def tolak_pengajuan_batal():
    list_pesanan['status_pesanan'][indeks_list_pesanan] = 'Menunggu'
    print('=' * 40)
    print('             MENU PESANAN             ')
    print('=' * 40)
    print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
def informasi_pesanan():
    os.system('cls')
    print('=' * 40)
    print('             MENU PESANAN             ')
    print('=' * 40)
    print(f'{list_pesanan['nama_produk'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')


def edit_pesanan():
    tampilan_list_pesanan('             MENU PESANAN             ', 'Belum ada yang memesan produk.')
    if list_pesanan['status_pesanan'][indeks_list_pesanan] == 'Pembatalan telah diajukan.':
        while True:
            informasi_pesanan()
            pilihan_ajuan = input('Setujui Pembatalan? (Ya/Tidak): ')
            if pilihan_ajuan.strip().lower() == 'ya':
                terima_pengajuan_batal()
                tekan_kembali('Pengajuan pembatalan diterima.')
                menu_pesanan()
                return True
            elif pilihan_ajuan.strip().lower() == 'tidak':
                tolak_pengajuan_batal()
                tekan_kembali('Pengajuan pembatalan ditolak')
                menu_pesanan()
                return True
            else:
                kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
    informasi_pesanan()
    edit_status_pesanan = input('Edit Status Pesanan? (Ya/Tidak): ')
    if edit_status_pesanan.strip().lower() == 'ya':
        informasi_pesanan()
        list_pesanan['status_pesanan'][indeks_list_pesanan] = input('Ubah Status Pesanan: ')
        informasi_pesanan()
        tekan_kembali('Status pesanan berhasil diubah!')
        menu_pesanan()

def tampilan_akun_admin():
    os.system('cls')
    print('=' * 40)
    print('             AKUN ADMIN             ')
    print('=' * 40)
    print(f'Username: {admin_username}')
    print(f'Password: {admin_password}')
    print(f'Simpanan Uang: {penyimpanan_uang_admin}')
    print('=' * 40)

# Menu Utama > Kelola Akun
def kelola_akun_admin():
    tampilan_akun_admin()
    print('1. Ubah Username')
    print('2. Ubah Password')
    print('3. Kembali')
    opsi_kelola_akun_admin = input('Pilih Opsi (1/2/3): ')
    if opsi_kelola_akun_admin.strip() == '1':
        tampilan_akun_admin()
        global admin_username
        admin_username = input('Masukkan Username Baru Admin: ')
        os.system('cls')
        tekan_kembali('Username berhasil diganti!')
        kelola_akun_admin()
    elif opsi_kelola_akun_admin.strip() == '2':
        tampilan_akun_admin()
        global admin_password
        admin_password = input('Masukkan Password Baru Admin: ')
        os.system('cls')
        tekan_kembali('Password berhasil diganti!')
        kelola_akun_admin()
    elif opsi_kelola_akun_admin.strip() == '3':
        menu_utama_admin()
    else:
        kesalahan('=====Pilihan tidak valid!  Silakan masukkan kembali.=====')
        kelola_akun_admin()




# AKUN PENGGUNA #
# Menu Utama (Pengguna)
def menu_utama_pengguna():
    os.system('cls')
    print('=' * 40)
    print('               MENU UTAMA               ')
    print('=' * 40)
    print('1. Halaman Produk')
    print('2. Keranjang Belanja')
    print('3. Daftar Pesanan')
    print('4. Riwayat Transaksi')
    print('5. Kelola Akun')
    print('6. Log Out')
    print('=' * 40)
    pilihan_menu = input('Pilih Menu: ')
    if pilihan_menu.strip() == "1":
        halaman_produk()
    elif pilihan_menu.strip() == "2":
        keranjang_belanja()
    elif pilihan_menu.strip() == "3":
        daftar_pesanan()
    elif pilihan_menu.strip() == "4":
        riwayat_transaksi()
    elif pilihan_menu.strip() == "5":
        kelola_akun_pengguna()
    elif pilihan_menu.strip() == "6":
        menu_masuk()
    else:
        kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
        menu_utama_pengguna()

def halaman_produk():
    test_list_produk('             HALAMAN PRODUK             ')
    global pilih_produk
    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
    tampilan_produk('             HALAMAN PRODUK             ')
    if tampilan_produk:
        pesanan = input("Apakah Anda ingin memesan produk ini? (Ya/Tidak): ")
        if pesanan.strip().lower() == 'ya':
            if pilih_produk in list_pesanan['nama_produk']:
                os.system('cls')
                tekan_kembali('Produk ini sudah Anda pesan.')
                halaman_produk()
            else:
                global jumlah_stok
                jumlah_stok = int(list_produk['stok_produk'][indeks_list_produk])
                if jumlah_stok == 0:
                    os.system('cls')
                    tekan_kembali('Stok produk tidak tersedia.')
                    halaman_produk()
                else:
                    pemesanan_produk()
        elif pesanan.strip().lower() == 'tidak':
            menu_utama_pengguna()
        else:
            kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
    else:
        menu_utama_pengguna()

def pemesanan_produk():
    os.system('cls')
    print('=' * 40)
    print('             OPSI PEMESANAN             ')
    print('=' * 40)
    print('1. Tambahkan ke Keranjang Belanja')
    print('2. Langsung Bayar')
    opsi_pemesanan = input("Opsi Pemesanan (1/2): ")
    if opsi_pemesanan == '1':
        opsi_keranjang_belanja()
    elif opsi_pemesanan == '2':
        opsi_bayar_langsung()
    else:
        kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
    
def opsi_keranjang_belanja():
    while True:
        global jumlah_pesanan
        try:
            os.system('cls')
            print('=' * 40)
            print('             OPSI PEMESANAN             ')
            print('=' * 40)
            print(f'Stok Produk: {list_produk['stok_produk'][indeks_list_produk]}')
            print('=' * 40)
            jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            break
    if int(jumlah_pesanan) > int(jumlah_stok):
        tekan_kembali("Stok tidak mencukupi.")
        menu_utama_pengguna()
    elif int(jumlah_pesanan) > 0:
        list_keranjang_belanja.setdefault(list_produk['nama_produk'][indeks_list_produk], [list_produk['harga_produk'][indeks_list_produk], jumlah_pesanan])
        tekan_kembali("Produk berhasil ditambahkan ke keranjang belanja!")
        menu_utama_pengguna()
    else:
        kesalahan("Jumlah pesanan tidak valid. Silakan masukkan kembali jumlah pesanan anda.")
        opsi_keranjang_belanja()

def opsi_bayar_langsung():
    while True:
        global jumlah_pesanan
        try:
            os.system('cls')
            print('=' * 40)
            print('             OPSI PEMESANAN             ')
            print('=' * 40)
            print(f'Stok Produk: {list_produk['stok_produk'][indeks_list_produk]}')
            print('=' * 40)
            jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            break
    if int(jumlah_pesanan) > int(jumlah_stok):
        tekan_kembali("=====Stok tidak mencukupi. Silakan masukkan kembali jumlah pesanan anda.=====")
        opsi_bayar_langsung()
    elif int(jumlah_pesanan) > 0:
        global jumlah_harga, total_harga
        jumlah_harga = list_produk['harga_produk'][indeks_list_produk]
        total_harga = int(jumlah_pesanan) * int(jumlah_harga)
        while True:
            os.system('cls')
            print('=' * 40)
            print(f'Total Harga: {total_harga}')
            print('=' * 40)
            konfirmasi_pesanan = input("Apakah Anda ingin melanjutkan ke pembayaran? (Ya/Tidak): ")
            if konfirmasi_pesanan.strip().lower() == 'ya':
                # Pembayaran Produk
                proses_pembayaran()
                break
            elif konfirmasi_pesanan.strip().lower() == 'tidak':
                os.system('cls')
                tekan_kembali("Pesanan dibatalkan.")
                menu_utama_pengguna()
                break
            else:
                kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
    else:
        kesalahan("=====Jumlah pesanan tidak valid. Silakan masukkan kembali.=====")
        opsi_bayar_langsung()

def proses_pembayaran():
    os.system('cls')
    global uang_bayar
    while True:
        try:
            print('=' * 40)
            print(f'Total Harga: {total_harga}')
            uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            break
    if int(uang_bayar) >= int(total_harga):
        global kembalian, status_pesanan
        kembalian = int(uang_bayar) - int(total_harga)
        status_pesanan = 'Menunggu'
        hasil_setelah_pembayaran()
    elif int(uang_bayar) < int(total_harga):
        while True:
            os.system('cls')
            print("Uang yang dibayarkan tidak mencukupi.")
            print('=' * 40)
            ulang_pembayaran = input("Apakah Anda ingin mengulangi pembayaran? (Ya/Tidak): ")
            if ulang_pembayaran.strip().lower() == 'ya':
                proses_pembayaran()
                break
            elif ulang_pembayaran.strip().lower() == 'tidak':
                menu_utama_pengguna()
                break
            else:
                kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")


def hasil_setelah_pembayaran():
    global penyimpanan_uang_admin
    penyimpanan_uang_admin = int(penyimpanan_uang_admin) + int(total_harga)
    list_pesanan['nama_produk'].append(list_produk['nama_produk'][indeks_list_produk])
    list_pesanan['harga_produk'].append(list_produk['harga_produk'][indeks_list_produk])
    list_pesanan['kategori_produk'].append(list_produk['kategori_produk'][indeks_list_produk])
    list_pesanan['detail_produk'].append(list_produk['detail_produk'][indeks_list_produk])
    list_pesanan['deskripsi_produk'].append(list_produk['deskripsi_produk'][indeks_list_produk])
    list_pesanan['kondisi_produk'].append(list_produk['kondisi_produk'][indeks_list_produk])
    list_pesanan['stok_produk'].append(list_produk['stok_produk'][indeks_list_produk])
    list_pesanan['berat_produk'].append(list_produk['berat_produk'][indeks_list_produk])
    list_pesanan['detail_pengiriman'].append(list_produk['detail_pengiriman'][indeks_list_produk])
    list_pesanan['status_pesanan'].append(status_pesanan)
    list_riwayat_transaksi['nama_produk'].append(list_produk['nama_produk'][indeks_list_produk])
    list_riwayat_transaksi['harga_produk'].append(list_produk['harga_produk'][indeks_list_produk])
    list_riwayat_transaksi['kategori_produk'].append(list_produk['kategori_produk'][indeks_list_produk])
    list_riwayat_transaksi['detail_produk'].append(list_produk['detail_produk'][indeks_list_produk])
    list_riwayat_transaksi['deskripsi_produk'].append(list_produk['deskripsi_produk'][indeks_list_produk])
    list_riwayat_transaksi['kondisi_produk'].append(list_produk['kondisi_produk'][indeks_list_produk])
    list_riwayat_transaksi['stok_produk'].append(list_produk['stok_produk'][indeks_list_produk])
    list_riwayat_transaksi['berat_produk'].append(list_produk['berat_produk'][indeks_list_produk])
    list_riwayat_transaksi['detail_pengiriman'].append(list_produk['detail_pengiriman'][indeks_list_produk])
    list_riwayat_transaksi['jumlah_pesanan'].append(jumlah_pesanan)
    list_riwayat_transaksi['total_harga'].append(total_harga)
    list_riwayat_transaksi['uang_bayar'].append(uang_bayar)
    list_riwayat_transaksi['kembalian'].append(kembalian)
    list_hasil_pemesanan['jumlah_pesanan'].append(jumlah_pesanan)
    list_hasil_pemesanan['uang_bayar'].append(uang_bayar)
    list_hasil_pemesanan['kembalian'].append(kembalian)
    list_produk['stok_produk'][indeks_list_produk] = int(list_produk['stok_produk'][indeks_list_produk]) - int(jumlah_pesanan)
    struk_pembelian()

def struk_pembelian():
    print('=' * 40)
    print('             STRUK PEMBELIAN             ')
    print('=' * 40)
    print(f'Nama Produk: {list_produk['nama_produk'][indeks_list_produk]}')
    print(f'Harga Produk: Rp{list_produk['harga_produk'][indeks_list_produk]}')
    print(f'Banyak Pesanan: {jumlah_pesanan}')
    print(f'Total Harga: {total_harga}')
    print(f'Nominal Pembayaran: {uang_bayar}')
    print(f'Kembalian: Rp{kembalian}')
    print(f'Status Pesanan: {status_pesanan}')
    print('=' * 40)
    tekan_kembali('Pembayaran berhasil!')
    menu_utama_pengguna()


def keranjang_belanja():
    os.system('cls')
    print('=' * 40)
    print('             KERANJANG BELANJA             ')
    print('=' * 40)
# Tidak Ada Produk Di Dalam Keranjang Belanja
    if not list_keranjang_belanja:
        tekan_kembali('Keranjang belanja kosong.')
        menu_utama_pengguna()
    else:
        print('=' * 40)
        for produk in list_keranjang_belanja:
            print(f'— {produk}: Harga Produk = {list_keranjang_belanja[produk][0]}, Banyak Pesanan = {list_keranjang_belanja[produk][1]}')
        print('=' * 40)
        print('1. Beli Produk')
        print('2. Beli Semua')
        print('3. Hapus Produk')
        print('4. Kembali')
        print('=' * 40)
        opsi_keranjang = input('Pilih Opsi (1/2/3/4): ')
        if opsi_keranjang == '1':
            beli_satu_produk()
        elif opsi_keranjang == '2':
            beli_semua_produk()
        elif opsi_keranjang == '3':
            hapus_produk_keranjang()
        elif opsi_keranjang == '4':
            menu_utama_pengguna()
        else:
            keranjang_belanja()

def beli_satu_produk():
    global total_harga, pilih_produk_keranjang, indeks_list_produk
    total_harga = int(list_keranjang_belanja[produk][0]) * int(list_keranjang_belanja[produk][1])
    pilih_produk_keranjang = input('Masukkan nama produk yang ingin dibayar: ')
    for produk in list_produk['nama_produk']:
        list_produk_test = list_produk['nama_produk'].index(produk)
        if list_produk['nama_produk'][list_produk_test] == pilih_produk_keranjang:
            indeks_list_produk = list_produk['nama_produk'].index(pilih_produk_keranjang)
            os.system('cls')
            print(f'Nama Produk: {list_produk['nama_produk'][indeks_list_produk]}')
            print(f'Harga Produk: {list_produk['harga_produk'][indeks_list_produk]}')
            print(f'Kategori Produk: {list_produk['kategori_produk'][indeks_list_produk]}')
            print(f'Detail Produk: {list_produk['detail_produk'][indeks_list_produk]}')
            print(f'Deskripsi Produk: {list_produk['deskripsi_produk'][indeks_list_produk]}')
            print(f'Kondisi Produk: {list_produk['kondisi_produk'][indeks_list_produk]}')
            print(f'Stok Produk: {list_produk['stok_produk'][indeks_list_produk]}')
            print(f'Berat Produk: {list_produk['berat_produk'][indeks_list_produk]}')
            print(f'Detail Pengiriman: {list_produk['detail_pengiriman'][indeks_list_produk]}')
            os.system('cls')
            pembayaran()
            return True
    tekan_kembali('Produk tidak ditemukan.')
    keranjang_belanja()
    return False
    

def pembayaran():
    global kembalian, status_pesanan, uang_bayar
    while True:
        os.system('cls')
        try:
            print('=' * 40)
            print(f'Total Harga: {total_harga}')
            uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
        except ValueError:
            os.system('cls')
            print('Input harus angka!')
        else:
            os.system('cls')
            break
    if int(uang_bayar) >= int(total_harga):
        kembalian = int(uang_bayar) - int(total_harga)
        status_pesanan = 'Menunggu'
        for produk in list_keranjang_belanja:
            if list_produk['nama_produk'][indeks_list_produk] == produk:
                hasil_setelah_pembayaran()
    elif int(uang_bayar) < int(total_harga):
        while True:
            os.system('cls')
            print("Uang yang dibayarkan tidak mencukupi.")
            print('=' * 40)
            ulang_pembayaran = input("Apakah Anda ingin mengulangi pembayaran? (Ya/Tidak): ")
            if ulang_pembayaran.strip().lower() == 'ya':
                pembayaran()
                break
            elif ulang_pembayaran.strip().lower() == 'tidak':
                menu_utama_pengguna()
                break
            else:
                kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")

def beli_semua_produk():
    global total_harga, list_keranjang_belanja
    while True:
        os.system('cls')
        print('=' * 40)
        print('             KERANJANG BELANJA             ')
        total_harga = 0
        for produk in list_keranjang_belanja:
            total_harga = int(list_keranjang_belanja[produk][0]) * int(list_keranjang_belanja[produk][1]) + int(total_harga)
        konfirmasi_pesanan = input("Apakah Anda ingin melanjutkan ke pembayaran? (Ya/Tidak): ")
        if konfirmasi_pesanan.strip().lower() == 'ya':
            os.system('cls')
            pembayaran()
            list_keranjang_belanja = {}
            break
        elif konfirmasi_pesanan.strip().lower() == 'tidak':
            keranjang_belanja()
            break
        else:
            kesalahan("=====Pilihan tidak valid! Silakan masukkan kembali.=====")

def hapus_produk_keranjang():
    while True:
        global pilih_produk_keranjang
        pilih_produk_keranjang = input('Masukkan nama produk yang ingin dihapus: ')
        for produk in list_produk['nama_produk']:
            list_produk_test = list_produk['nama_produk'].index(produk)
            if list_produk['nama_produk'][list_produk_test] == pilih_produk_keranjang:
                indeks_list_produk = list_produk['nama_produk'].index(pilih_produk_keranjang)
                os.system('cls')
                print(f'Nama Produk: {list_produk['nama_produk'][indeks_list_produk]}')
                print(f'Harga Produk: {list_produk['harga_produk'][indeks_list_produk]}')
                print(f'Kategori Produk: {list_produk['kategori_produk'][indeks_list_produk]}')
                print(f'Detail Produk: {list_produk['detail_produk'][indeks_list_produk]}')
                print(f'Deskripsi Produk: {list_produk['deskripsi_produk'][indeks_list_produk]}')
                print(f'Kondisi Produk: {list_produk['kondisi_produk'][indeks_list_produk]}')
                print(f'Stok Produk: {list_produk['stok_produk'][indeks_list_produk]}')
                print(f'Berat Produk: {list_produk['berat_produk'][indeks_list_produk]}')
                print(f'Detail Pengiriman: {list_produk['detail_pengiriman'][indeks_list_produk]}')
                print('=' * 40)
                print(f'Banyak Pesanan: {list_keranjang_belanja[produk][1]}')
                print(f'Keseluruhan Harga: {list_keranjang_belanja[produk][0]}')
                print('=' * 40)
            else:
                os.system('cls')
                tekan_kembali('Produk tidak ditemukan.')
                keranjang_belanja()
                return False
        for produk_keranjang in list_keranjang_belanja:
            if produk_keranjang == pilih_produk_keranjang:
                konfirmasi_hapus_produk_keranjang = input('Hapus produk ini dari keranjang belanja? (Ya/Tidak): ')
                if konfirmasi_hapus_produk_keranjang.strip().lower() == 'ya':
                    del list_keranjang_belanja[pilih_produk_keranjang]
                    os.system('cls')
                    tekan_kembali('Produk berhasil dihapus!')
                    keranjang_belanja()
                    return True
                elif konfirmasi_hapus_produk_keranjang.strip().lower() == 'tidak':
                    keranjang_belanja()
                    return True
                else:
                    kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')



def tampilan_daftar_pesanan():
    os.system('cls')
    indeks_list_pesanan = list_pesanan['nama_produk'].index(pilih_produk)
    print('=' * 40)
    print('             DAFTAR PESANAN             ')
    print('=' * 40)
    print(f'Nama Produk: {list_pesanan['nama_produk'][indeks_list_pesanan]}')
    print(f'Harga Produk: Rp{list_pesanan['harga_produk'][indeks_list_pesanan]}')
    print(f'Kategori Produk: {list_pesanan['kategori_produk'][indeks_list_pesanan]}')
    print(f'Detail Produk: {list_pesanan['detail_produk'][indeks_list_pesanan]}')
    print(f'Deskripsi Produk: {list_pesanan['deskripsi_produk'][indeks_list_pesanan]}')
    print(f'Kondisi Produk: {list_pesanan['kondisi_produk'][indeks_list_pesanan]}')
    print(f'Stok Produk: {list_pesanan['stok_produk'][indeks_list_pesanan]}')
    print(f'Berat Produk: {list_pesanan['berat_produk'][indeks_list_pesanan]}')
    print(f'Detail Pengiriman: {list_pesanan['detail_pengiriman'][indeks_list_pesanan]}')
    print(f'Status Pesanan: {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
    print('=' * 40)

def daftar_pesanan():
    tampilan_list_pesanan('             DAFTAR PESANAN             ', 'Anda belum memesan produk')
    if not test_daftar_pesanan:
        menu_utama_pengguna()
        return False
    if list_pesanan['status_pesanan'][indeks_list_pesanan] == 'Pembatalan telah diajukan.':
        while True:
            tampilan_daftar_pesanan()
            print('1. Tarik Pengajuan Pembatalan')
            print('2. Kembali')
            opsi_pesanan = input('Pilih Opsi (1/2): ')
            if opsi_pesanan == '1':
                list_pesanan['status_pesanan'][indeks_list_pesanan] = 'Menunggu'
                tekan_kembali('Pengajuan telah ditarik.')
                menu_utama_pengguna()
                break
            elif opsi_pesanan == '2':
                menu_utama_pengguna()
                break
            else:
                kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
    else:
        while True:
            tampilan_daftar_pesanan()
            print('1. Batalkan Pesanan')
            print('2. Kembali')
            opsi_pesanan = input('Pilih Opsi (1/2): ')
            if opsi_pesanan == '1':
                list_pesanan['status_pesanan'][indeks_list_pesanan] = 'Pembatalan telah diajukan.'
                tekan_kembali('Menunggu konfirmasi dari toko...')
                menu_utama_pengguna()
                break
            elif opsi_pesanan == '2':
                menu_utama_pengguna()
                break
            else:
                kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')

def tampilan_riwayat_transaksi():
    global indeks_list_riwayat_transaksi
    indeks_list_riwayat_transaksi = list_riwayat_transaksi['nama_produk'].index(pilih_produk)
    os.system('cls')
    print('=' * 40)
    print('             RIWAYAT TRANSAKSI             ')
    print('=' * 40)
    print(f'Nama Produk: {list_riwayat_transaksi['nama_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Harga Produk: Rp{list_riwayat_transaksi['harga_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Kategori Produk: {list_riwayat_transaksi['kategori_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Detail Produk: {list_riwayat_transaksi['detail_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Deskripsi Produk: {list_riwayat_transaksi['deskripsi_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Kondisi Produk: {list_riwayat_transaksi['kondisi_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Stok Produk: {list_riwayat_transaksi['stok_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Berat Produk: {list_riwayat_transaksi['berat_produk'][indeks_list_riwayat_transaksi]}')
    print(f'Detail Pengiriman: {list_riwayat_transaksi['detail_pengiriman'][indeks_list_riwayat_transaksi]}')
    print(f'Banyak Pesanan: {list_riwayat_transaksi['jumlah_pesanan'][indeks_list_riwayat_transaksi]}')
    print(f'Total Harga: {list_riwayat_transaksi['total_harga'][indeks_list_riwayat_transaksi]}')
    print(f'Nominal Pembayaran: {list_riwayat_transaksi['uang_bayar'][indeks_list_riwayat_transaksi]}')
    print(f'Kembalian: Rp{list_riwayat_transaksi['kembalian'][indeks_list_riwayat_transaksi]}')
    print('=' * 40)
def lihat_riwayat():
    os.system('cls')
    print('=' * 40)
    print('             RIWAYAT TRANSAKSI             ')
    print('=' * 40)
    for produk in list_riwayat_transaksi['nama_produk']:
        print(f'— {produk}')
    print('=' * 40)
    global pilih_produk
    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
# Menampilkan Informasi Produk
    for produk in list_riwayat_transaksi['nama_produk']:
        list_riwayat_transaksi_test = list_riwayat_transaksi['nama_produk'].index(produk)
        if list_riwayat_transaksi['nama_produk'][list_riwayat_transaksi_test] == pilih_produk.strip():
            while True:
                tampilan_riwayat_transaksi()
                print('1. Kirim Komentar')
                print('2. Kembali')
                opsi_komentar = input('Pilih Opsi: ')
                os.system('cls')
                if opsi_komentar == '1':
                    for produk_komentar in halaman_komentar:
                        if produk_komentar == list_riwayat_transaksi['nama_produk'][indeks_list_riwayat_transaksi]:
                            komentar_pengguna = f'({username_log_in}: \n)' + input('Masukkan tanggapan: ')
                            halaman_komentar['nama_produk'].append(list_riwayat_transaksi['nama_produk'])
                            halaman_komentar['komentar_produk'].append(komentar_pengguna)
                    riwayat_transaksi()
                    break
                elif opsi_komentar == '2':
                    riwayat_transaksi()
                    break
                else:
                    kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                return True
    # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
    os.system('cls')
    tekan_kembali("Produk tidak ditemukan.")
    return False

def riwayat_transaksi():
    os.system('cls')
    print('=' * 40)
    print('             RIWAYAT TRANSAKSI             ')
    print('=' * 40)
    riwayat_transaksi_test = list_riwayat_transaksi.get('nama_produk')
    if not riwayat_transaksi_test:
        tekan_kembali('Anda belum melakukan pemesanan')
        menu_utama_pengguna()
    else:
        for produk in list_riwayat_transaksi['nama_produk']:
            print(f'— {produk}')
        print('1. Lihat Riwayat Transaksi Produk')
        print('2. Hapus Semua Riwayat Transaksi')
        print('3. Kembali')
        opsi_riwayat_transaksi = input('Pilih Opsi (1/2/3): ')
        if opsi_riwayat_transaksi.strip() == '1':
            lihat_riwayat()
        elif opsi_riwayat_transaksi.strip() == '2':
            while True:
                os.system('cls')
                print('=' * 40)
                print('             RIWAYAT TRANSAKSI             ')
                print('=' * 40)
                for produk in list_riwayat_transaksi['nama_produk']:
                    print(f'— {produk}')
                print('=' * 40)
                hapus_riwayat_transaksi = input("Apakah Anda yakin ingin menghapus semua riwayat transaksi? (Ya/Tidak): ")
                if hapus_riwayat_transaksi.strip().lower() == 'ya':
                    for data in list_riwayat_transaksi.values():
                        data.clear()
                    tekan_kembali('Riwayat transaksi berhasil dihapus')
                    menu_utama_pengguna()
                    break
                elif hapus_riwayat_transaksi.strip().lower() == 'tidak':
                    riwayat_transaksi()
                    break
                else:
                    kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
        elif opsi_riwayat_transaksi.strip() == '3':
            menu_utama_pengguna()
        else:
            kesalahan('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
            riwayat_transaksi()

def tampilan_akun_pengguna():
    os.system('cls')
    print('=' * 40)
    print('             AKUN PENGGUNA             ')
    print('=' * 40)
    print(f'Username: {username_log_in}')
    print(f'Password: {password_log_in}')
    print('=' * 40)

def kelola_akun_pengguna():
    tampilan_akun_pengguna()
    global username_log_in, password_log_in
    print('1. Ubah Username')
    print('2. Ubah Password')
    print('3. Kembali')
    opsi_kelola_akun = input('Pilih Opsi (1/2/3): ')
    if opsi_kelola_akun.strip() == '1':
        for data_edit in data_akun:
            if data_edit == username_log_in:
                while True:
                    tampilan_akun_pengguna()
                    username_baru = input('Masukkan Username Baru: ')
                    if username_baru in data_akun:
                        os.system('cls')
                        print('=====Username ini sudah digunakan. Silahkan masukkan kembali.=====')
                        time.sleep(2)
                    else:
                        del data_akun[username_log_in]
                        data_akun.update({username_baru : password_log_in})
                        username_log_in = username_baru
                        os.system('cls')
                        tekan_kembali('Username berhasil diganti!')
                        break
    elif opsi_kelola_akun.strip() == '2':
        for data_edit in data_akun:   
            if data_edit == username_log_in:
                tampilan_akun_pengguna()
                password_baru = input('Masukkan Password Baru: ')
                data_akun[username_log_in] = password_baru
                password_log_in = password_baru
                os.system('cls')
                tekan_kembali('Password berhasil diganti!')
    elif opsi_kelola_akun.strip() == '3':
        menu_utama_pengguna()
    else:
        kesalahan('=====Pilihan tidak valid!  Silakan masukkan kembali.=====')
        kelola_akun_pengguna()
        


menu_masuk()