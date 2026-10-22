import os
import time

# Database Akun
data_akun = {}

# Database Admin
admin_username = "AL"
admin_password = "009"
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
username_log_in = 'none'
password_log_in = 'none'

# Menu Masuk
go_out = False
status_log_in = False
while not go_out and not status_log_in:
    os.system('cls')
    print('=' * 40)
    print("         SELAMAT DATANG DI TOKO         ")
    print('=' * 40)
    print("Silakan Masuk Terlebih Dahulu")
    print("1. Log In")
    print("2. Sign In")
    print("3. Keluar")
    pilih_masuk = input("Pilih Opsi (1/2/3): ")
    # Melanjutkan Program ke Bagian Log In / Sign in
    if pilih_masuk.strip() == "1" or pilih_masuk.strip() == "2":
        pass
    # Mengakhiri Program
    elif pilih_masuk.strip() == "3":
        go_out = True
    # Mengulang Program ke Menu Masuk Karena Salah Input
    else:
        os.system('cls')
        print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
        time.sleep(2)

# Menu Masuk > Log In / Sign In
    # Bagian Log In
    if pilih_masuk.strip() == "1":
        os.system('cls')
        print('=' * 40)
        print("              LOG IN AKUN              ")
        print('=' * 40)
        username_log_in = input("Masukkan Username : ")
        password_log_in = input("Masukkan Password : ")
        log_in = input("Masuk? (Ya/Tidak): ")
        if log_in.strip().lower() == "ya":
            if username_log_in == admin_username and password_log_in == admin_password:
                os.system('cls')
                print("Login berhasil!")
                print('=' * 40)
                lanjut = input('Tekan Enter Untuk Lanjut')
                status_log_in = True
            else:
                for data_test in data_akun:
                    if username_log_in == data_test and password_log_in == data_akun[data_test]:
                        os.system('cls')
                        print("Login berhasil!")
                        print('=' * 40)
                        lanjut = input('Tekan Enter Untuk Lanjut')
                        status_log_in = True
                        break
                if not status_log_in:
                    os.system('cls')
                    print("=====Login gagal. Silakan coba lagi.=====")
                    time.sleep(2)
        elif log_in.strip().lower() == "tidak":
            pass
        else:
            os.system('cls')
            print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
            time.sleep(2)
            os.system('cls')
    # Bagian Sign In
    elif pilih_masuk.strip() == "2":
        os.system('cls')
        print('=' * 40)
        print("              SIGN IN AKUN              ")
        print('=' * 40)
        username_sign_in = input("Masukkan Username : ")
        password_sign_in = input("Masukkan Password: ")
        simpan_akun = input("Simpan akun? (Ya/Tidak): ")
        if simpan_akun.strip().lower() == "ya":
            os.system('cls')
            if username_sign_in in data_akun:
                os.system('cls')
                print('=====Username ini sudah digunakan. Silahkan masukkan kembali.=====')
                time.sleep(2)
            else:
                data_akun.setdefault(username_sign_in, password_sign_in)
                print("Akun berhasil dibuat!")
                print('=' * 40)
                lanjut = input('Tekan Enter Untuk Lanjut')
                go_out = False
        elif simpan_akun.strip().lower() == "tidak":
            pass
        else:
            os.system('cls')
            print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
            time.sleep(2)






# AKUN ADMIN
    if status_log_in:    
        if username_log_in == admin_username and password_log_in == admin_password:

# Menu Utama
            go_back_menu_utama = False
            while not go_back_menu_utama:
                go_out = False
                status_log_in = False
                os.system('cls')
                print('=' * 40)
                print('               MENU UTAMA               ')
                print('=' * 40)
                print('1. Produk')
                print('2. Pesanan')
                print('3. Kelola Akun')
                print('4. Log Out')
                print('=' * 40)
                pilihan_menu = input('Pilih Menu: ')

#  Menu Utama > Menu Produk
                if pilihan_menu.strip() == "1":
                    go_back_menu_utama = False
                    go_back_produk = True
                    while not go_back_menu_utama and go_back_produk:
                        os.system('cls')
                        print('=' * 40)
                        print('               MENU PRODUK               ')
                        print('=' * 40)
                        print('1. Daftar Produk')
                        print('2. Tambah Produk')
                        print('3. Hapus Produk')
                        print('4. Kembali')
                        print('=' * 40)
                        pilihan_menu_produk = input('Pilih Menu: ')

# Menu Utama > Menu Produk > Daftar Produk
                        if pilihan_menu_produk.strip() == '1':
                            go_back_produk = False
                            while not go_back_produk:                    
                            # Menampilkan Daftar Produk
                                os.system('cls')
                                print('=' * 40)
                                print('             DAFTAR PRODUK             ')
                                print('=' * 40)
                                list_produk_test = list_produk.get('nama_produk')
                            # Tidak Ada Produk Yang Ditambahkan
                                if not list_produk_test:
                                    print("Belum ada produk yang ditambahkan.")
                                    print('=' * 40)
                                    kembali = input('Tekan Enter Untuk Kembali')
                                    go_back_produk = True
                            # List Semua Produk Yang Ada
                                else:
                                    for produk in list_produk['nama_produk']:
                                        print(f'— {produk}')
                                    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                # Menampilkan Informasi Produk
                                    produk_ditemukan = False
                                    while True:
                                        for produk in list_produk['nama_produk']:
                                            list_produk_test = list_produk['nama_produk'].index(produk)
                                            if list_produk['nama_produk'][list_produk_test] == pilih_produk.strip():
                                                indeks_list_produk = list_produk['nama_produk'].index(pilih_produk)
                                                os.system('cls')
                                                print('=' * 40)
                                                print('             DAFTAR PRODUK             ')
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
                                                for produk_komen in halaman_komentar['nama_produk']:
                                                    if produk_komen == list_produk['nama_produk'][indeks_list_produk]:
                                                        print(produk_komen)
                                                        isi_komentar = halaman_komentar['komentar_produk'].index(produk_komen)
                                                        print(produk_komen[isi_komentar])
                                                produk_ditemukan = True
                                        # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
                                        if not produk_ditemukan:
                                            os.system('cls')
                                            print("Produk tidak ditemukan.")
                                            print('=' * 40)
                                            kembali = input('Tekan Enter Untuk Kembali')
                                            os.system('cls')
                                            break
                                        else:
                                        # Opsi Kembali ke Menu Utama atau Menu Produk
                                            print('1. Kembali Ke Menu Produk')
                                            print('2. Kembali Ke Daftar Produk')
                                            kembali = input('Pilih Opsi: ')
                                            if kembali.strip().lower() == '1':
                                                go_back_produk = True
                                                break
                                            elif kembali.strip().lower() == '2':
                                                break
                                            else:
                                                os.system('cls')
                                                print('=====Pilihan tidak valid! Silakan masukkan kembali=====')
                                                time.sleep(2)

# Menu Utama > Menu Produk > Tambahkan Produk
                        elif pilihan_menu_produk.strip() == '2':
                            go_back_produk = False
                            while not go_back_produk:
                            # Input Data Produk
                                os.system('cls')
                                print('=' * 40)
                                print('             TAMBAH PRODUK             ')
                                print('=' * 40)
                                nama_produk = input('Masukkan Nama Produk: ')
                                while True:
                                    harga_produk = (input('Masukkan Harga Produk (Rp): '))
                                    if not harga_produk.isdigit():
                                        os.system('cls')
                                        print('Input harus angka!')
                                        print('=' * 40)
                                        print('             TAMBAH PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Nama Produk: {nama_produk}')
                                    else:
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             TAMBAH PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Nama Produk: {nama_produk}')
                                        print(f'Masukkan Harga Produk (Rp): {harga_produk}')
                                        break
                                kategori_produk = input('Masukkan Kategori Produk: ')
                                detail_produk = input('Masukkan Detail Produk: ')
                                deskripsi_produk = input('Masukkan Deskripsi Produk: ')
                                kondisi_produk = input('Masukkan Kondisi Produk (Baru/Bekas): ')
                                print('=' * 40)
                                print('             BANYAK PRODUK             ')
                                print('=' * 40)
                                while True:
                                    stok_produk = (input('Masukkan Stok Produk: '))
                                    if not stok_produk.isdigit():
                                        os.system('cls')
                                        print('Input harus angka!')
                                        print('=' * 40)
                                        print('             TAMBAH PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Nama Produk: {nama_produk}')
                                        print(f'Masukkan Harga Produk (Rp): {harga_produk}')
                                        print(f'Masukkan Kategori Produk: {kategori_produk}')
                                        print(f'Masukkan Detail Produk: {detail_produk}')
                                        print(f'Masukkan Deskripsi Produk: {deskripsi_produk}')
                                        print(f'Masukkan Kondisi Produk (Baru/Bekas): {kondisi_produk}')
                                        print('=' * 40)
                                        print('             BANYAK PRODUK             ')
                                        print('=' * 40)
                                    else:
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             TAMBAH PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Nama Produk: {nama_produk}')
                                        print(f'Masukkan Harga Produk (Rp): {harga_produk}')
                                        print(f'Masukkan Kategori Produk: {kategori_produk}')
                                        print(f'Masukkan Detail Produk: {detail_produk}')
                                        print(f'Masukkan Deskripsi Produk: {deskripsi_produk}')
                                        print(f'Masukkan Kondisi Produk (Baru/Bekas): {kondisi_produk}')
                                        print('=' * 40)
                                        print('             BANYAK PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Stok Produk: {stok_produk}')
                                        break
                                print('=' * 40)
                                print('             PENGIRIMAN PRODUK             ')
                                print('=' * 40)
                                while True:
                                    berat_produk = (input('Masukkan Berat Produk (gram): '))
                                    if not berat_produk.isdigit():
                                        os.system('cls')
                                        print('Input harus angka!')
                                        print('=' * 40)
                                        print('             TAMBAH PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Nama Produk: {nama_produk}')
                                        print(f'Masukkan Harga Produk (Rp): {harga_produk}')
                                        print(f'Masukkan Kategori Produk: {kategori_produk}')
                                        print(f'Masukkan Detail Produk: {detail_produk}')
                                        print(f'Masukkan Deskripsi Produk: {deskripsi_produk}')
                                        print(f'Masukkan Kondisi Produk (Baru/Bekas): {kondisi_produk}')
                                        print('=' * 40)
                                        print('             BANYAK PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Stok Produk: {stok_produk}')
                                        print('=' * 40)
                                        print('             PENGIRIMAN PRODUK             ')
                                        print('=' * 40)
                                    else:
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             TAMBAH PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Nama Produk: {nama_produk}')
                                        print(f'Masukkan Harga Produk (Rp): {harga_produk}')
                                        print(f'Masukkan Kategori Produk: {kategori_produk}')
                                        print(f'Masukkan Detail Produk: {detail_produk}')
                                        print(f'Masukkan Deskripsi Produk: {deskripsi_produk}')
                                        print(f'Masukkan Kondisi Produk (Baru/Bekas): {kondisi_produk}')
                                        print('=' * 40)
                                        print('             BANYAK PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Stok Produk: {stok_produk}')
                                        print('=' * 40)
                                        print('             PENGIRIMAN PRODUK             ')
                                        print('=' * 40)
                                        print(f'Masukkan Berat Produk (gram): {berat_produk}')
                                        break
                                detail_pengiriman = input('Masukkan Detail Pengiriman: ')
                                print('=' * 40)
                                break
                        # Menampilkan Data Produk yang Ditambahkan
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
                        # Opsi Simpan dan Kembali ke Menu Produk
                            kembali = input('Simpan dan Kembali? (Ya/Tidak): ')
                            if kembali.strip().lower() == 'ya':
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
                                print('=' * 40)
                                print('Produk berhasil ditambahkan!')
                                print('=' * 40)
                                kembali = input('Tekan Enter Untuk Kembali')
                                go_back_produk = True
                            elif kembali.strip().lower() == 'tidak':
                                input_test = False
                                while not input_test:
                                    os.system('cls')
                                    print('Pengisian dibatalkan.')
                                    print('=' * 40)
                                    pengulangan = input('Apakah Anda ingin mengisi ulang data produk? (Ya/Tidak): ')
                                    if pengulangan.strip().lower() == 'ya':
                                        input_test = True
                                    elif pengulangan.strip().lower() == 'tidak':
                                        input_test = True
                                        go_back_produk = True
                                    else:
                                        os.system('cls')
                                        print('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
                                        time.sleep(2)
                            else:
                                os.system('cls')
                                print('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
                                time.sleep(2)


                        elif pilihan_menu_produk.strip() == '3':
                            go_back_produk = False
                            while not go_back_produk:                    
                            # Menampilkan Daftar Produk
                                os.system('cls')
                                print('=' * 40)
                                print('             HAPUS PRODUK             ')
                                print('=' * 40)
                                list_produk_test = list_produk.get('nama_produk')
                            # Tidak Ada Produk Yang Ditambahkan
                                if not list_produk_test:
                                    print("Belum ada produk yang ditambahkan.")
                                    print('=' * 40)
                                    kembali = input('Tekan Enter Untuk Kembali')
                                    go_back_produk = True
                            # List Semua Produk Yang Ada
                                else:
                                    for produk in list_produk['nama_produk']:
                                        print(f'— {produk}')
                                    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                # Menampilkan Informasi Produk
                                    produk_ditemukan = False
                                    for produk in list_produk['nama_produk']:
                                        list_produk_test = list_produk['nama_produk'].index(produk)
                                        if list_produk['nama_produk'][list_produk_test] == pilih_produk.strip():
                                            indeks_list_produk = list_produk['nama_produk'].index(pilih_produk)
                                            os.system('cls')
                                            print('=' * 40)
                                            print('             HAPUS PRODUK             ')
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
                                                print('Produk berhasil dihapus!')
                                                print('=' * 40)
                                                kembali = input('Tekan Enter Untuk Kembali')
                                                go_back_produk = True
                                            elif pilih_hapus.strip().lower() == 'tidak':
                                                go_back_produk = True
                                            else:
                                                os.system('cls')
                                                print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                            produk_ditemukan = True
                                    # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
                                    if not produk_ditemukan:
                                        os.system('cls')
                                        print("Produk tidak ditemukan.")
                                        print('=' * 40)
                                        kembali = input('Tekan Enter Untuk Kembali')
    
                            
    # Menu Utama > Menu Produk > Kembali                
                        elif pilihan_menu_produk.strip() == '4':
                            go_back_produk = False

    # Menu Utama > Menu Produk > Pilihan Tidak Valid
                        else:
                            os.system('cls')
                            print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
                            time.sleep(2)


    # Menu Utama > Menu Pesanan
                elif pilihan_menu.strip() == "2":
                    go_back_menu_pesanan = False
                    while not go_back_menu_pesanan:
                        list_produk_test = list_pesanan.get('nama_produk')
                        if not list_produk_test:
                            os.system('cls')
                            print('=' * 40)
                            print('             MENU PESANAN             ')
                            print('=' * 40)
                            print("Belum ada pesanan.")
                            print('=' * 40)
                            kembali = input('Tekan Enter Untuk Kembali')
                            go_back_menu_pesanan = True
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
                                os.system('cls')
                                print('=' * 40)
                                print('             MENU PESANAN             ')
                                print('=' * 40)
                                for produk in list_pesanan['nama_produk']:
                                    print(f'— {produk}, Status: {list_pesanan['status_pesanan'][list_pesanan_test]}')
                                print('=' * 40)
                                pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                for produk in list_pesanan['nama_produk']:
                                    list_pesanan_test = list_pesanan['nama_produk'].index(produk)
                                    if list_pesanan['nama_produk'][list_pesanan_test] == pilih_produk.strip():
                                        indeks_list_pesanan = list_pesanan['nama_produk'].index(pilih_produk)
                                        if list_pesanan['status_pesanan'][indeks_list_pesanan] == 'Pembatalan telah diajukan.':
                                            print('=' * 40)
                                            print('             MENU PESANAN             ')
                                            print('=' * 40)
                                            print(f'{list_pesanan['nama_produk'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
                                            print('=' * 40)
                                            pilihan_ajuan = input('Setujui Pembatalan? (Ya/Tidak): ')
                                            if pilihan_ajuan.strip().lower() == 'ya':
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
                                                list_produk['stok_produk'][indeks_list_pesanan] = list_produk['stok_produk'][indeks_list_pesanan] + int(list_hasil_pemesanan['jumlah_pesanan'])
                                                penyimpanan_uang_admin = int(penyimpanan_uang_admin) + int(list_hasil_pemesanan['kembalian']) - int(list_hasil_pemesanan['uang_bayar'])
                                                print('=' * 40)
                                                print('             MENU PESANAN             ')
                                                print('=' * 40)
                                                print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
                                                print('=' * 40)
                                                print('Pengajuan pembatalan diterima.')
                                                print('=' * 40)
                                                kembali = input('Tekan Enter Untuk Kembali')
                                            elif pilihan_ajuan.strip().lower() == 'tidak':
                                                list_pesanan['status_pesanan'][indeks_list_pesanan] = 'Menunggu'
                                                print('=' * 40)
                                                print('             MENU PESANAN             ')
                                                print('=' * 40)
                                                print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
                                                print('=' * 40)
                                                print('Pengajuan pembatalan ditolak')
                                                print('=' * 40)
                                                kembali = input('Tekan Enter Untuk Kembali')
                                            else:
                                                os.system('cls')
                                                print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                                time.sleep(2)
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             MENU PESANAN             ')
                                        print('=' * 40)
                                        print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
                                        edit_status_pesanan = input('Edit Status Pesanan? (Ya/Tidak): ')
                                        if edit_status_pesanan.strip().lower() == 'ya':
                                            os.system('cls')
                                            print('=' * 40)
                                            print('             MENU PESANAN             ')
                                            print('=' * 40)
                                            print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
                                            list_pesanan['status_pesanan'][indeks_list_pesanan] = input('Ubah Status Pesanan: ')
                                            os.system('cls')
                                            print('=' * 40)
                                            print('             MENU PESANAN             ')
                                            print('=' * 40)
                                            print(f'{list_pesanan['nama_pesanan'][indeks_list_pesanan]} : {list_pesanan['status_pesanan'][indeks_list_pesanan]}')
                                            print('Status pesanan berhasil diubah!')
                                            print('=' * 40)
                                            kembali = input('Tekan Enter Untuk Kembali')
                            elif opsi_menu_pesanan == '2':
                                go_back_menu_pesanan = True
                            else:
                                os.system('cls')
                                print('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
                                time.sleep(2)
                        
                            



    # Menu Utama > Kelola Akun
                elif pilihan_menu.strip() == "3":
                    go_back_kelola_akun = False
                    while not go_back_kelola_akun:
                        os.system('cls')
                        print('=' * 40)
                        print('             AKUN ADMIN             ')
                        print('=' * 40)
                        print(f'Username: {admin_username}')
                        print(f'Password: {admin_password}')
                        print(f'Simpanan Uang: {penyimpanan_uang_admin}')
                        print('=' * 40)
                        print('1. Ubah Username')
                        print('2. Ubah Password')
                        print('3. Kembali')
                        opsi_kelola_akun = input('Pilih Opsi (1/2/3): ')
                        os.system('cls')
                        if opsi_kelola_akun.strip() == '1':
                            print('=' * 40)
                            print('             AKUN ADMIN             ')
                            print('=' * 40)
                            print(f'Username: {admin_username}')
                            print(f'Password: {admin_password}')
                            print('=' * 40)
                            admin_username = input('Masukkan Username Baru Admin: ')
                            os.system('cls')
                            print('Username berhasil diganti!')
                            print('=' * 40)
                            kembali = input('Tekan Enter Untuk Kembali')
                        elif opsi_kelola_akun.strip() == '2':
                            print('=' * 40)
                            print('             AKUN ADMIN             ')
                            print('=' * 40)
                            print(f'Username: {admin_username}')
                            print(f'Password: {admin_password}')
                            print('=' * 40)
                            admin_password = input('Masukkan Password Baru Admin: ')
                            os.system('cls')
                            print('Password berhasil diganti!')
                            print('=' * 40)
                            kembali = input('Tekan Enter Untuk Kembali')
                        elif opsi_kelola_akun.strip() == '3':
                            go_back_kelola_akun = True
                        else:
                            os.system('cls')
                            print('=====Pilihan tidak valid!  Silakan masukkan kembali.=====')
                            time.sleep(2)
                        
                        

    # Menu Utama > Log Out
                elif pilihan_menu.strip() == '4':
                    go_back_menu_utama = True

    # Menu Utama > Pilihan Tidak Valid
                else:
                    os.system('cls')
                    print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
                    time.sleep(2)
                





        # AKUN PENGGUNA
        else:    
            for log_in_test in data_akun:
                if username_log_in in data_akun and password_log_in == data_akun[username_log_in]:
            # Menu Utama
                    go_back_menu_utama = False
                    while not go_back_menu_utama:
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
                        os.system('cls')
                        if pilihan_menu.strip() == '6':
                            go_back_menu_utama = True

            # Menu Utama > Halaman Produk
                        if pilihan_menu.strip() == "1":
                            go_back_produk = False
                            while not go_back_produk:
                                os.system('cls')
                                print('=' * 40)
                                print('             HALAMAN PRODUK             ')
                                print('=' * 40)
                                list_produk_test = list_produk.get('nama_produk')
                            # Tidak Ada Produk Yang Tersedia
                                if not list_produk_test:
                                    print("Belum ada produk yang ditambahkan.")
                                    print('=' * 40)
                                    kembali = input('Tekan Enter Untuk Kembali')
                                    go_back_produk = True
                                    break
                            # List Semua Produk Yang Ada
                                else:
                                    for produk in list_produk['nama_produk']:
                                        print(f'— {produk}')
                                pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                            # Menampilkan Informasi Produk
                                produk_ditemukan = False
                                for produk in list_produk['nama_produk']:
                                    list_produk_test = list_produk['nama_produk'].index(produk)
                                    if list_produk['nama_produk'][list_produk_test] == pilih_produk.strip():
                                        indeks_list_produk = list_produk['nama_produk'].index(pilih_produk)
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             HALAMAN PRODUK             ')
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
                                        for produk_komen in halaman_komentar['nama_produk']:
                                            if produk_komen == list_produk['nama_produk'][indeks_list_produk]:
                                                print(produk_komen)
                                                isi_komentar = halaman_komentar['komentar_produk'].index(produk_komen)
                                                print(produk_komen[isi_komentar])
                                                print('=' * 40)
                                        produk_ditemukan = True
                                    # Memesan Produk
                                        pesanan = input("Apakah Anda ingin memesan produk ini? (Ya/Tidak): ")
                                        if pesanan.strip().lower() == 'ya':
                                            if pilih_produk in list_pesanan['nama_produk']:
                                                os.system('cls')
                                                print('Produk ini sudah Anda pesan.')
                                                print('=' * 40)
                                                kembali = input ('Tekan Enter Untuk Kembali')
                                                go_back_produk = True
                                            else:
                                                jumlah_stok = int(list_produk['stok_produk'][indeks_list_produk])
                                                if jumlah_stok == 0:
                                                    os.system('cls')
                                                    print('Stok produk tidak tersedia.')
                                                    print('=' * 40)
                                                    kembali = input('Tekan Enter Untuk Kembali')
                                                    go_back_produk = True
                                                else:
                                                    go_back_pemesanan = False
                                                    while not go_back_pemesanan:
                                                        os.system('cls')
                                                        print('=' * 40)
                                                        print('             OPSI PEMESANAN             ')
                                                        print('=' * 40)
                                                        print('1. Tambahkan ke Keranjang Belanja')
                                                        print('2. Langsung Bayar')
                                                        opsi_keranjang = input("Opsi Pemesanan (1/2): ")
                                                        os.system('cls')
                                                        if opsi_keranjang.strip().lower() == '1':
                                                            while True:
                                                                print('=' * 40)
                                                                print('             OPSI PEMESANAN             ')
                                                                print('=' * 40)
                                                                print(f'Stok Produk: {list_produk['stok_produk'][indeks_list_produk]}')
                                                                print('=' * 40)
                                                                jumlah_pesanan = input("Masukkan jumlah pesanan: ")
                                                                if not jumlah_pesanan.isdigit():
                                                                    os.system('cls')
                                                                    print('Input harus angka!')
                                                                else:
                                                                    if int(jumlah_pesanan) > int(jumlah_stok):
                                                                        print("Stok tidak mencukupi.")
                                                                        print('=' * 40)
                                                                        kembali = input('Tekan Enter Untuk Kembali')
                                                                        go_back_pemesanan = True
                                                                        break
                                                                    elif int(jumlah_pesanan) > 0:
                                                                        list_keranjang_belanja.setdefault(nama_produk, jumlah_pesanan)
                                                                        print("Produk berhasil ditambahkan ke keranjang belanja!")
                                                                        print('=' * 40)
                                                                        kembali = input('Tekan Enter Untuk Kembali')
                                                                        go_back_pemesanan = True
                                                                        break
                                                                    else:
                                                                        os.system('cls')
                                                                        print("Jumlah pesanan tidak valid. Silakan masukkan kembali jumlah pesanan anda.")
                                                                        time.sleep(2)
                                                                    break
                                                        elif opsi_keranjang.strip().lower() == '2':
                                                            while True:
                                                                print("=" * 40)
                                                                jumlah_pesanan = (input("Masukkan jumlah pesanan: "))
                                                                if not jumlah_pesanan.isdigit():
                                                                    os.system('cls')
                                                                    print('Input harus angka!')
                                                                else:
                                                                    break
                                                            if int(jumlah_pesanan) > int(jumlah_stok):
                                                                print("Stok tidak mencukupi. Silakan masukkan kembali jumlah pesanan anda.")
                                                            elif int(jumlah_pesanan) > 0:
                                                                jumlah_harga = list_produk['harga_produk'][indeks_list_produk]
                                                                total_harga = int(jumlah_pesanan) * int(jumlah_harga)
                                                                print(f'Total Harga: {total_harga}')
                                                                konfirmasi_pesanan = input("Apakah Anda ingin melanjutkan ke pembayaran? (Ya/Tidak): ")
                                                                go_back_konfirmasi = False
                                                                while not go_back_konfirmasi:
                                                                    if konfirmasi_pesanan.strip().lower() == 'ya':
                                                                    # Pembayaran Produk
                                                                        pembayaran = False
                                                                        while not pembayaran:
                                                                            os.system('cls')
                                                                            while True:
                                                                                print('=' * 40)
                                                                                print(f'Total Harga: {total_harga}')
                                                                                uang_bayar = input("Masukkan jumlah uang yang dibayarkan: ")
                                                                                if not jumlah_pesanan.isdigit():
                                                                                    os.system('cls')
                                                                                    print('Input harus angka!')
                                                                                else:
                                                                                    break
                                                                            if int(uang_bayar) >= int(total_harga):
                                                                                kembalian = int(uang_bayar) - int(total_harga)
                                                                                status_pesanan = 'Menunggu'
                                                                                list_produk['stok_produk'][indeks_list_produk] = int(list_produk['stok_produk'][indeks_list_produk]) - int(jumlah_pesanan)
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
                                                                                print(f'Pembayaran berhasil!')
                                                                                print('=' * 40)
                                                                                kembali = input('Tekan Enter Untuk Kembali')
                                                                                pembayaran = True
                                                                                go_back_informasi_produk = True
                                                                                go_back_pemesanan = True
                                                                                go_back_produk = True
                                                                                go_back_konfirmasi = True
                                                                            elif uang_bayar < total_harga:
                                                                                print("Uang yang dibayarkan tidak mencukupi.")
                                                                                ulang_pembayaran = input("Apakah Anda ingin mengulangi pembayaran? (Ya/Tidak): ")
                                                                                if ulang_pembayaran.strip().lower() == 'ya':
                                                                                    pass
                                                                                elif ulang_pembayaran.strip().lower() == 'tidak':
                                                                                    pembayaran = True
                                                                                    go_back_informasi_produk = True
                                                                                    go_back_pemesanan = True
                                                                                    go_back_konfirmasi = True
                                                                                else:
                                                                                    os.system('cls')
                                                                                    print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
                                                                                    time.sleep(2)
                                                                    elif konfirmasi_pesanan.strip().lower() == 'tidak':
                                                                        go_back_pemesanan = True
                                                                        go_back_konfirmasi = True
                                                                        print("Pesanan dibatalkan.")
                                                                        print('=' * 40)
                                                                        kembali = input('Tekan Enter Untuk Kembali')
                                                                    else:
                                                                        os.system('cls')
                                                                        print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                                                        time.sleep(2)
                                                            else:
                                                                os.system('cls')
                                                                print("=====Jumlah pesanan tidak valid. Silakan masukkan kembali.=====")
                                                                time.sleep(2)
                                                        else:
                                                            os.system('cls')
                                                            print('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
                                                            time.sleep(2)
                                        elif pesanan.strip().lower() == 'tidak':
                                            go_back_produk = True
                                            break
                                        else:
                                            os.system('cls')
                                            print('=====Pilihan tidak valid! Silakan masukkan kembali.=====')
                                            time.sleep(2)
                            # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
                                if not produk_ditemukan:
                                    os.system('cls')
                                    print("Produk tidak ditemukan.")
                                    print('=' * 40)
                                    kembali = input('Tekan Enter Untuk Kembali')
                                    go_back_produk = True
                            

            # Menu Utama > Keranjang Belanja
                        elif pilihan_menu.strip() == "2":
                            go_back_keranjang_belanja = False
                            while not go_back_keranjang_belanja:
                                os.system('cls')
                                print('=' * 40)
                                print('             KERANJANG BELANJA             ')
                                print('=' * 40)
                                list_keranjang_test = list_keranjang_belanja.get('nama_produk')
                            # Tidak Ada Produk Di Dalam Keranjang Belanja
                                if not list_keranjang_test:
                                    print('Keranjang belanja kosong.')
                                    print('=' * 40)
                                    kembali = input('Tekan Enter Untuk Kembali')
                                    go_back_keranjang_belanja = True
                                else:
                                    print('=' * 40)
                                    for produk in list_keranjang_belanja:
                                        print(f'— {produk}')
                                    print('=' * 40)
                                    print('1. Beli Produk')
                                    print('2. Beli Semua')
                                    print('3. Hapus Produk')
                                    print('4. Kembali')
                                    print('=' * 40)
                                    opsi_keranjang = input('Pilih Opsi (1/2/3/4): ')
                                    if opsi_keranjang == '1':
                                        pilih_produk_keranjang = input("Masukkan nama produk yang ingin dibayar: ")
                                        go_back_beli_produk = False
                                        for produk in list_produk['nama_produk']:
                                            list_produk_test = list_produk['nama_produk'].index(produk)
                                            if list_produk['nama_produk'][list_produk_test] == pilih_produk_keranjang:
                                                indeks_list_produk = list_produk['nama_produk'].index(pilih_produk_keranjang)
                                                pembayaran = False
                                                while not pembayaran:
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
                                                    while True:
                                                        print('=' * 40)
                                                        print(f'Total Harga: {total_harga}')
                                                        uang_bayar = input("Masukkan jumlah uang yang dibayarkan: ")
                                                        if not jumlah_pesanan.isdigit():
                                                            os.system('cls')
                                                            print('Input harus angka!')
                                                        else:
                                                            break
                                                    if int(uang_bayar) >= int(total_harga):
                                                        kembalian = int(uang_bayar) - int(total_harga)
                                                        status_pesanan = 'Menunggu'
                                                        list_produk['stok_produk'][indeks_list_produk] = int(list_produk['stok_produk'][indeks_list_produk]) - int(jumlah_pesanan)
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
                                                        print(f'Pembayaran berhasil!')
                                                        print('=' * 40)
                                                        kembali = input('Tekan Enter Untuk Kembali')
                                                        pembayaran = True
                                                    elif uang_bayar < total_harga:
                                                        print("Uang yang dibayarkan tidak mencukupi.")
                                                        ulang_pembayaran = input("Apakah Anda ingin mengulangi pembayaran? (Ya/Tidak): ")
                                                        if ulang_pembayaran.strip().lower() == 'ya':
                                                            pass
                                                        elif ulang_pembayaran.strip().lower() == 'tidak':
                                                            pembayaran = True
                                                        else:
                                                            os.system('cls')
                                                            print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
                                                            time.sleep(2)
                                
                                    elif opsi_keranjang == '2':
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             KERANJANG BELANJA             ')
                                        print('=' * 40)
                                        for produk in list_keranjang_belanja['nama_produk']:
                                            indeks_list_produk = list_produk['nama_produk'].index(pilih_produk_keranjang)
                                            print(f'Nama Produk: {list_produk['nama_produk'][indeks_list_produk]}')
                                            print(f'Harga Produk: {list_produk['harga_produk'][indeks_list_produk]}')
                                            print('=' * 40)
                                            total_harga = 0
                                            for item in list_keranjang_belanja:
                                                produk = item.keys
                                                jumlah_pesanan = item
                                                subtotal = int(jumlah_pesanan) * int(item)
                                                total_harga = int(total_harga) + int(subtotal)
                                            print(f'Total Harga: {total_harga}')
                                            konfirmasi_pesanan = input("Apakah Anda ingin melanjutkan ke pembayaran? (Ya/Tidak): ")
                                            if konfirmasi_pesanan.strip().lower() == 'ya':
                                            # Pembayaran Produk
                                                pembayaran = False
                                                while not pembayaran:
                                                    os.system('cls')
                                                    while True:
                                                        uang_bayar = input("Masukkan jumlah uang yang dibayarkan: ")
                                                        if not uang_bayar.isdigit():
                                                            os.system('cls')
                                                            print('Input harus angka!')
                                                        else:
                                                            break
                                                    if int(uang_bayar) >= int(total_harga):
                                                        os.system('cls')
                                                        kembalian = int(uang_bayar) - int(total_harga)
                                                        list_produk['stok_produk'][indeks_list_produk] = int(list_produk['stok_produk'][indeks_list_produk]) - int(jumlah_pesanan)
                                                        penyimpanan_uang_admin = int(penyimpanan_uang_admin) + int(total_harga)
                                                        status_pesanan = 'Menunggu'
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
                                                        print(f'Pembayaran berhasil!')
                                                        print('=' * 40)
                                                        kembali = input('Tekan Enter Untuk Kembali')
                                                        pembayaran = True
                                                        go_back_informasi_produk = True
                                                    elif uang_bayar < total_harga:
                                                        os.system('cls')
                                                        print("Uang yang dibayarkan tidak mencukupi.")
                                                        print('=' * 40)
                                                        ulang_pembayaran = input("Apakah Anda ingin mengulangi pembayaran? (Ya/Tidak): ")
                                                        if ulang_pembayaran.strip().lower() == 'ya':
                                                            pass
                                                        elif ulang_pembayaran.strip().lower() == 'tidak':
                                                            pembayaran = True
                                                            go_back_informasi_produk = True
                                                        else:
                                                            os.system('cls')
                                                            print("=====Pilihan tidak valid! Silakan masukkan kembali.=====")
                                                            time.sleep(2)


            # Menu Utama > Status Pesanan
                        elif pilihan_menu.strip() == "3":
                            os.system('cls')
                            print('=' * 40)
                            print('             DAFTAR PESANAN             ')
                            print('=' * 40)
                            list_pesanan_test = list_pesanan.get('nama_produk')
                            if not list_pesanan_test:
                                print('Anda belum memesan produk')
                                print('=' * 40)
                                kembali = input('Tekan Untuk Kembali')
                            else:
                                for produk in list_pesanan['nama_produk']:
                                    print(f'— {produk}')
                                pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                for produk in list_pesanan['nama_produk']:
                                    indeks_list_pesanan = list_pesanan['nama_produk'].index(produk)
                                    if list_pesanan['nama_produk'][indeks_list_pesanan] == pilih_produk.strip():
                                        if list_pesanan['status_pesanan'][indeks_list_pesanan] == 'Pembatalan telah diajukan.':
                                            while True:
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
                                                print('1. Tarik Pengajuan Pembatalan')
                                                print('2. Kembali')
                                                opsi_pesanan = input('Pilih Opsi (1/2): ')
                                                if opsi_pesanan == '1':
                                                    list_pesanan['status_pesanan'][indeks_list_pesanan] = 'Menunggu'
                                                    print('Pengajuan telah ditarik.')
                                                    print('=' * 40)
                                                    kembali = input('Tekan Untuk Kembali')
                                                    break
                                                elif opsi_pesanan == '2':
                                                    break
                                                else:
                                                    print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                                    time.sleep(2)
                                        else:
                                            while True:
                                                os.system('cls')
                                                indeks_list_pesanan = list_produk['nama_produk'].index(pilih_produk)
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
                                                print('1. Batalkan Pesanan')
                                                print('2. Kembali')
                                                opsi_pesanan = input('Pilih Opsi (1/2): ')
                                                if opsi_pesanan == '1':
                                                    list_pesanan['status_pesanan'][indeks_list_pesanan] = 'Pembatalan telah diajukan.'
                                                    print('Menunggu konfirmasi dari toko...')
                                                    print('=' * 40)
                                                    kembali = input('Tekan Untuk Kembali')
                                                    break
                                                elif opsi_pesanan == '2':
                                                    break
                                                else:
                                                    os.system('cls')
                                                    print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                                    time.sleep(2)
                                        
                            
            # Menu Utama > Riwayat Transaksi
                        elif pilihan_menu.strip() == '4':
                            go_back_riwayat_transaksi = False
                            while not go_back_riwayat_transaksi:
                                os.system('cls')
                                print('=' * 40)
                                print('             RIWAYAT TRANSAKSI             ')
                                print('=' * 40)
                                riwayat_transaksi_test = list_riwayat_transaksi.get('nama_produk')
                                if not riwayat_transaksi_test:
                                    print('Anda belum melakukan pemesanan')
                                    print('=' * 40)
                                    kembali = input('Tekan Enter Untuk Kembali')
                                    go_back_riwayat_transaksi = True
                                else:
                                    for produk in list_riwayat_transaksi['nama_produk']:
                                        print(f'— {produk}')
                                    print('1. Lihat Riwayat Transaksi Produk')
                                    print('2. Hapus Semua Riwayat Transaksi')
                                    print('3. Kembali')
                                    opsi_riwayat_transaksi = input('Pilih Opsi (1/2/3): ')
                                    if opsi_riwayat_transaksi.strip() == '1':
                                        os.system('cls')
                                        print('=' * 40)
                                        print('             RIWAYAT TRANSAKSI             ')
                                        print('=' * 40)
                                        for produk in list_riwayat_transaksi['nama_produk']:
                                            print(f'— {produk}')
                                        print('=' * 40)
                                        pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                    # Menampilkan Informasi Produk
                                        produk_ditemukan = False
                                        for produk in list_riwayat_transaksi['nama_produk']:
                                            list_riwayat_transaksi_test = list_riwayat_transaksi['nama_produk'].index(produk)
                                            if list_riwayat_transaksi['nama_produk'][list_riwayat_transaksi_test] == pilih_produk.strip():
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
                                                produk_ditemukan = True
                                                print('=' * 40)
                                                print('1. Kirim Komentar')
                                                print('2. Kembali')
                                                opsi_komentar = input('Pilih Opsi: ')
                                                os.system('cls')
                                                if opsi_komentar == '1':
                                                    for produk_komentar in halaman_komentar:
                                                        if produk_komentar == list_riwayat_transaksi['nama_produk'][indeks_list_riwayat_transaksi]:
                                                            komentar_pengguna = f'({username_log_in}: \n)' + input('Masukkan tanggapan: ')
                                                            halaman_komentar['nama_produk'].append([list_riwayat_transaksi['nama_produk'][indeks_list_riwayat_transaksi]])
                                                            halaman_komentar[list_riwayat_transaksi['komentar_produk'][indeks_list_riwayat_transaksi]].append(komentar_pengguna)
                                                            go_back_riwayat_transaksi = True
                                                elif opsi_komentar == '2':
                                                    go_back_riwayat_transaksi = True
                                                else:
                                                    os.system('cls')
                                                    print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                                    time.sleep(2)
                                                    
                                                
                                        # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
                                        if not produk_ditemukan:
                                            os.system('cls')
                                            print("Produk tidak ditemukan.")
                                            print('=' * 40)
                                            kembali = input('Tekan Enter Untuk Kembali')
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
                                                'uang_bayar' :  [],
                                                'kembalian' : []
                                                }
                                                print('Riwayat transaksi berhasil dihapus')
                                                print('=' * 40)
                                                kembali = input('Tekan Enter Untuk Kembali')
                                                break
                                            elif hapus_riwayat_transaksi.strip().lower() == 'tidak':
                                                break
                                            else:
                                                os.system('cls')
                                                print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                                time.sleep(2)

                                    elif opsi_riwayat_transaksi.strip() == '3':
                                        go_back_riwayat_transaksi = True

                                    else:
                                        os.system('cls')
                                        print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                                        time.sleep(2)


            # Menu Utama > Kelola Akun
                        elif pilihan_menu.strip() == "5":
                            go_back_kelola_akun = False
                            while not go_back_kelola_akun:
                                os.system('cls')
                                print('=' * 40)
                                print('             AKUN PENGGUNA             ')
                                print('=' * 40)
                                print(f'Username: {username_log_in}')
                                print(f'Password: {password_log_in}')
                                print('=' * 40)
                                print('1. Ubah Username')
                                print('2. Ubah Password')
                                print('3. Kembali')
                                opsi_kelola_akun = input('Pilih Opsi (1/2/3): ')
                                if opsi_kelola_akun.strip() == '1':
                                    for data_edit in data_akun:
                                        if data_edit == username_log_in:
                                            os.system('cls')
                                            print('=' * 40)
                                            print('             AKUN PENGGUNA             ')
                                            print('=' * 40)
                                            print(f'Username: {username_log_in}')
                                            print(f'Password: {password_log_in}')
                                            print('=' * 40)
                                            username_baru = input('Masukkan Username Baru: ')
                                            del data_akun[username_log_in]
                                            data_akun.update({username_baru : password_log_in})
                                            username_log_in = username_baru
                                            os.system('cls')
                                            print('Username berhasil diganti!')
                                            print('=' * 40)
                                            lanjut = input('Tekan Enter Untuk Kembali')
                                elif opsi_kelola_akun.strip() == '2':
                                    for data_edit in data_akun:   
                                        if data_edit == username_log_in:
                                            os.system('cls')
                                            print('=' * 40)
                                            print('             AKUN PENGGUNA             ')
                                            print('=' * 40)
                                            print(f'Username: {username_log_in}')
                                            print(f'Password: {password_log_in}')
                                            print('=' * 40)
                                            password_baru = input('Masukkan Password Baru: ')
                                            data_akun[username_log_in] = password_baru
                                            password_log_in = password_baru
                                            os.system('cls')
                                            print('Password berhasil diganti!')
                                            print('=' * 40)
                                            lanjut = input('Tekan Enter Untuk Kembali')
                                elif opsi_kelola_akun.strip() == '3':
                                    go_back_kelola_akun = True
                                else:
                                    os.system('cls')
                                    print('=====Pilihan tidak valid!  Silakan masukkan kembali.=====')
                                    time.sleep

            # Menu Utama > Log Out
                        elif pilihan_menu.strip() == "6":
                            go_back_menu_utama = True
                            go_out = False
                            status_log_in = False

                        else:
                            os.system('cls')
                            print('=====Pilihan tidak valid. Silakan masukkan kembali.=====')
                            time.sleep(2)