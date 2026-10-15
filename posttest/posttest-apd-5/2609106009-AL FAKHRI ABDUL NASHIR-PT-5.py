import os
import time

# Database Akun
list_username = ['AL FAKHRI']
list_password = ['009']

# Database Admin
admin_username = "Al Fakhri AN"
admin_password = "2609106009"
penyimpanan_uang_admin = 0

# Database Produk
list_produk = []

# Database Keranjang Belanja
list_keranjang_belanja = []

# Database Pesanan
list_pesanan = []

# Database Kolom Komentar
list_komentar = []

# Variabel Kosong
username_log_in = 'none'
password_log_in = 'none'
status_pesanan = 'none'

# Menu Masuk
go_out = False
status_login = False
while not go_out and not status_login:
    os.system('cls')
    print("Selamat Datang di Toko")
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
        print("=====Pilihan tidak valid. Silakan masukkan kembali.=====")
        time.sleep(2)
        os.system('cls')
    os.system('cls')

# Menu Masuk > Log In / Sign In
    # Bagian Log In
    if pilih_masuk.strip() == "1":
        username_log_in = input("Masukkan Username : ")
        password_log_in = input("Masukkan Password : ")
        log_in = input("Masuk? (Ya/Tidak): ")
        if log_in.strip().lower() == "ya":
            if username_log_in == admin_username and password_log_in == admin_password:
                os.system('cls')
                print("Login berhasil!")
                print('=' * 40)
                lanjut = input('Tekan Enter Untuk Lanjut')
                status_login = True
            else:
                for i in range(len(list_username)):
                    if username_log_in == list_username[i] and password_log_in == list_password[i]:
                        os.system('cls')
                        print("Login berhasil!")
                        print('=' * 40)
                        lanjut = input('Tekan Enter Untuk Lanjut')
                        status_login = True
                        break
                if not status_login:
                    print("=====Login gagal. Silakan coba lagi.=====")
                    time.sleep(2)
                    os.system('cls')
        elif log_in.strip().lower() == "tidak":
            pass
        else:
            os.system('cls')
            print("=====Login gagal. Silakan coba lagi.=====")
            time.sleep(2)
            os.system('cls')
    # Bagian Sign In
    elif pilih_masuk.strip() == "2":
        username_sign_in = input("Masukkan Username : ")
        password_sign_in = input("Masukkan Password: ")
        simpan_akun = input("Simpan akun? (Ya/Tidak): ")
        if simpan_akun.strip().lower() == "ya":
            os.system('cls')
            list_username.append(username_sign_in)
            list_password.append(password_sign_in)
            print("Akun berhasil dibuat!")
            go_out = False
        elif simpan_akun.strip().lower() == "tidak":
            pass
        else:
            os.system('cls')
            print("=====Login gagal. Silakan coba lagi.=====")
            time.sleep(2)






# AKUN ADMIN
    if status_login:    
        for i in range(len(list_username)):
            if username_log_in == admin_username and password_log_in == admin_password:

# Menu Utama
                go_back_menu_utama = False
                while not go_back_menu_utama:
                    go_out = False
                    status_login = False
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
                    if pilihan_menu.strip() == '4':
                        go_back_menu_utama = True

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
                            print('2. Tambahkan Produk')
                            print('3. Kembali')
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
                                    list_nama_produk = [produk[0] for produk in list_produk]
                                # Tidak Ada Produk Yang Ditambahkan
                                    if not list_nama_produk:
                                        print("Belum ada produk yang ditambahkan.")
                                        kembali = input('Tekan Enter Untuk Kembali')
                                        break
                                # List Semua Produk Yang Ada
                                    else:
                                        for produk in list_produk:
                                            print(f'- {produk[0]}')
                                    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                # Menampilkan Informasi Produk
                                    for produk in list_produk:
                                        if produk[0].strip().lower() == pilih_produk.strip().lower():
                                            os.system('cls')
                                            print('=' * 40)
                                            print('             DAFTAR PRODUK             ')
                                            print('=' * 40)
                                            print(f'Nama Produk: {produk[0]}')
                                            print(f'Harga Produk: {produk[1]}')
                                            print(f'Kategori Produk: {produk[2]}')
                                            print(f'Detail Produk: {produk[3]}')
                                            print(f'Deskripsi Produk: {produk[4]}')
                                            print(f'Variasi Produk: {produk[5]}')
                                            print(f'Kondisi Produk: {produk[6]}')
                                            print(f'Stok Produk: {produk[7]}')
                                            print(f'Berat Produk: {produk[8]}')
                                            print(f'Opsi Asuransi Pengiriman: {produk[9]}')
                                            print(f'Detail Pengiriman: {produk[10]}')
                                    # Jika Produk Yang Dicari Tidak Ada Dalam Daftar Produk    
                                        if produk[0].strip().lower() != pilih_produk.strip().lower():
                                            print("Produk tidak ditemukan.")

                                # Opsi Kembali ke Menu Utama atau Menu Produk
                                    print('=' * 40)
                                    kembali = input('Kembali Ke Menu Utama? (Ya/Tidak): ')
                                    if kembali.strip().lower() == 'ya':
                                        go_back_produk = True
                                    elif kembali.strip().lower() == 'tidak':
                                        pass
                                    else:
                                        os.system('cls')
                                        print('=====Pilihan tidak valid. Silakan masukkan kembali=====')
                                        time.sleep(2)

# Menu Utama > Menu Produk > Tambahkan Produk
                            elif pilihan_menu_produk.strip() == '2':
                                go_back_produk = False
                                while not go_back_produk:
                                # Input Data Produk
                                    os.system('cls')
                                    list_produk_sementara = []
                                    print('=' * 40)
                                    print('             TAMBAH PRODUK             ')
                                    print('=' * 40)
                                    nama_produk = input('Masukkan Nama Produk: ')
                                    harga_produk = int(input('Masukkan Harga Produk (Rp): '))
                                    kategori_produk = input('Masukkan Kategori Produk: ')
                                    detail_produk = input('Masukkan Detail Produk: ')
                                    deskripsi_produk = input('Masukkan Deskripsi Produk: ')
                                    variasi_produk = input('Masukkan Variasi Produk: ')
                                    kondisi_produk = input('Masukkan Kondisi Produk (Baru/Bekas): ')
                                    print('=' * 40)
                                    print('             BANYAK PRODUK             ')
                                    print('=' * 40)
                                    stok_produk = int(input('Masukkan Stok Produk: '))
                                    print('=' * 40)
                                    print('             PENGIRIMAN PRODUK             ')
                                    print('=' * 40)
                                    berat_produk = int(input('Masukkan Berat Produk (gram): '))
                                    opsi_asuransi_pengiriman = input('Opsi Asuransi Pengiriman? (Wajib/Opsional): ')
                                    detail_pengiriman = input('Masukkan Detail Pengiriman: ')
                                    print('=' * 40)
                                # Menambahkan Produk ke List Sementara
                                    list_produk_sementara.append(nama_produk)
                                    list_produk_sementara.append(str(harga_produk))
                                    list_produk_sementara.append(kategori_produk)
                                    list_produk_sementara.append(detail_produk)
                                    list_produk_sementara.append(deskripsi_produk)
                                    list_produk_sementara.append(variasi_produk)
                                    list_produk_sementara.append(kondisi_produk)
                                    list_produk_sementara.append(str(stok_produk))
                                    list_produk_sementara.append(str(berat_produk))
                                    list_produk_sementara.append(opsi_asuransi_pengiriman)
                                    list_produk_sementara.append(detail_pengiriman)
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
                                    print(f'Variasi Produk: {variasi_produk}')
                                    print(f'Kondisi Produk: {kondisi_produk}')
                                    print(f'Stok Produk: {stok_produk}')
                                    print(f'Berat Produk: {berat_produk}')
                                    print(f'Opsi Asuransi Pengiriman: {opsi_asuransi_pengiriman}')
                                    print(f'Detail Pengiriman: {detail_pengiriman}')
                                    print('=' * 40)
                                # Opsi Simpan dan Kembali ke Menu Produk
                                    kembali = input('Simpan dan Kembali? (Ya/Tidak): ')
                                    if kembali.strip().lower() == 'ya':
                                        os.system('cls')
                                        list_produk.append(list_produk_sementara)
                                        print('Produk berhasil ditambahkan!')
                                        kembali = input('Tekan Enter Untuk Kembali')
                                        go_back_produk = True
                                    elif kembali.strip().lower() == 'tidak':
                                        print('Pengisian dibatalkan.')
                                        pengulangan = input('Apakah Anda ingin mengisi ulang data produk? (Ya/Tidak): ')
                                        if pengulangan.strip().lower() == 'ya':
                                            pass
                                        elif pengulangan.strip().lower() == 'tidak':
                                            go_back_produk = True
                                    else:
                                        os.system('cls')
                                        print('Pilihan tidak valid. Silakan masukkan kembali')
                                        time.sleep(2)
                            elif pilihan_menu_produk.strip() == '3':
                                go_back_produk = False

        # Menu Utama > Menu Produk > Kembali                
                            elif pilihan_menu_produk.strip() == '3':
                                go_back_menu_utama = True

        # Menu Utama > Menu Produk > Pilihan Tidak Valid
                            else:
                                os.system('cls')
                                print("Pilihan tidak valid!")
                                time.sleep(2)


        # Menu Utama > Menu Pesanan
                    elif pilihan_menu.strip() == "2":
                        go_back_menu_pesanan = False
                        while not go_back_menu_pesanan:
                            print('=' * 40)
                            print('             MENU PESANAN             ')
                            print('=' * 40)
                            print('1. Edit Pesanan')
                            print('2. Kembali')
                            opsi_menu_pesanan = input('Pilih Opsi: ')
                            if opsi_menu_pesanan == '1':
                                list_nama_produk = [produk[0] for produk in list_produk]
                                if not list_pesanan:
                                    print("Belum ada pesanan.")
                                    kembali = input('Tekan Enter Untuk Kembali')
                                else:
                                    for produk in list_pesanan:
                                        print(f'- {produk[0]}')
                                    pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                                    for produk in list_pesanan:
                                        if produk[0].strip().lower() == pilih_produk.strip().lower():
                                            print(f'{produk[0]} : {produk[1]}')
                                            edit_status_pesanan = input('Edit Status Pesanan? (Ya/Tidak): ')
                                            if edit_status_pesanan.strip().lower() == 'ya':
                                                produk[1] = input('Status Pesanan: ')
                                                print('Status pesanan berhasil diubah!')
                                                kembali = input('Tekan Enter Untuk Kembali')
                            elif opsi_menu_pesanan == '2':
                                go_back_menu_pesanan = True
                            else:
                                os.system('cls')
                                print('Pilihan tidak valid. Silakan masukkan kembali.')
                                time.sleep(2)
                            
                                



        # Menu Utama > Kelola Akun
                    elif pilihan_menu.strip() == "3":
                        go_back_kelola_akun = False
                        while not go_back_kelola_akun:
                            os.system('cls')
                            print('=' * 40)
                            print('             AKUN ADMIN             ')
                            print('=' * 40)
                            print('1. Ubah Username')
                            print('2. Ubah Password')
                            print('3. Kembali')
                            opsi_kelola_akun = input('Pilih Opsi (1/2/3): ')
                            if opsi_kelola_akun.strip() == '1':
                                admin_username = input('Masukkan Username Baru Admin: ')
                                print('Username berhasil diganti!')
                            elif opsi_kelola_akun.strip() == '2':
                                admin_password = input('Masukkan Password Baru Admin: ')
                                print('Password berhasil diganti!')
                            elif opsi_kelola_akun.strip() == '3':
                                go_back_kelola_akun = True
                            else:
                                os.system('cls')
                                print('Pilihan tidak valid.  Silakan masukkan kembali.')
                                time.sleep(2)
                            
                            

        # Menu Utama > Log Out
                    elif pilihan_menu.strip() == "4":
                        break

        # Menu Utama > Pilihan Tidak Valid
                    else:
                        os.system('cls')
                        print("Pilihan tidak valid! Silakan masukkan kembali.")
                        time.sleep(2)
                





        # AKUN PENGGUNA
            elif username_log_in == list_username[i] and password_log_in == list_password[i]:
        # Menu Utama
                go_back_menu_utama = False
                while not go_back_menu_utama:
                    os.system('cls')
                    print('=' * 40)
                    print('               MENU UTAMA               ')
                    print('=' * 40)
                    print('1. Halaman Produk')
                    print('2. Keranjang Belanja')
                    print('3. Status Pesanan')
                    print('4. Kelola Akun')
                    print('5. Log Out')
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
                            list_nama_produk = [produk[0] for produk in list_produk]
                            if not list_nama_produk:
                                print("Belum ada produk yang tersedia.")
                            else:
                                for produk in list_produk:
                                    print(f'- {produk[0]}')
                            pilih_produk = input("Masukkan nama produk yang ingin ditampilkan: ")
                        # Menampilkan Informasi Produk
                            go_back_informasi_produk = False
                            for produk in list_produk:
                                if produk[0].strip().lower() == pilih_produk.strip().lower():
                                    while not go_back_informasi_produk:
                                        os.system('cls')
                                        print(f'Nama Produk: {produk[0]}')
                                        print(f'Harga Produk: {produk[1]}')
                                        print(f'Kategori Produk: {produk[2]}')
                                        print(f'Detail Produk: {produk[3]}')
                                        print(f'Deskripsi Produk: {produk[4]}')
                                        print(f'Variasi Produk: {produk[5]}')
                                        print(f'Kondisi Produk: {produk[6]}')
                                        print(f'Stok Produk: {produk[7]}')
                                        print(f'Berat Produk: {produk[8]}')
                                        print(f'Opsi Asuransi Pengiriman: {produk[9]}')
                                        print(f'Detail Pengiriman: {produk[10]}')
                                    # Memesan Produk
                                        print('=' * 40)
                                        list_pesanan_sementara = []
                                        pesanan = input("Apakah Anda ingin memesan produk ini? (Ya/Tidak): ")
                                        if pesanan.strip().lower() == 'ya':
                                            print('=' * 40)
                                            print('             OPSI PEMESANAN             ')
                                            print('=' * 40)
                                            print('1. Tambahkan ke Keranjang Belanja')
                                            print('2. Langsung Bayar')
                                            opsi_keranjang = input("Opsi Pemesanan (1/2): ")
                                            if opsi_keranjang.strip().lower() == '1':
                                                jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
                                                if jumlah_pesanan > int(produk[7]):
                                                    print("Stok tidak mencukupi. Silakan masukkan kembali jumlah pesanan anda.")
                                                elif jumlah_pesanan > 0:
                                                    list_keranjang_belanja.append([produk, jumlah_pesanan])
                                                    print("Produk berhasil ditambahkan ke keranjang belanja.")
                                                else:
                                                    os.system('cls')
                                                    print("Jumlah pesanan tidak valid. Silakan masukkan kembali jumlah pesanan anda.")
                                                    time.sleep(2)
                                                go_back_informasi_produk = True
                                            elif opsi_keranjang.strip().lower() == '2':
                                                jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
                                                if jumlah_pesanan > int(produk[7]):
                                                    print("Stok tidak mencukupi. Silakan masukkan kembali jumlah pesanan anda.")
                                                elif jumlah_pesanan > 0:
                                                    total_harga = jumlah_pesanan * int(produk[1])
                                                    print(f'Total Harga: {total_harga}')
                                                    konfirmasi_pesanan = input("Apakah Anda ingin melanjutkan ke pembayaran? (Ya/Tidak): ")
                                                    if konfirmasi_pesanan.strip().lower() == 'ya':
                                                    # Pembayaran Produk
                                                        pembayaran = False
                                                        while not pembayaran:
                                                            uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
                                                            if uang_bayar >= total_harga:
                                                                kembalian = uang_bayar - total_harga
                                                                print(f'Pembayaran berhasil! Kembalian: {kembalian}')
                                                                produk[7] = str(int(produk[7]) - jumlah_pesanan)
                                                                penyimpanan_uang_admin += total_harga
                                                                status_pesanan = 'Menunggu'
                                                                list_pesanan_sementara.append(produk[0])
                                                                list_pesanan_sementara.append(status_pesanan)
                                                                list_pesanan.append(list_pesanan_sementara)
                                                                pembayaran = True
                                                                go_back_informasi_produk = True
                                                            elif uang_bayar < total_harga:
                                                                print("Uang yang dibayarkan tidak mencukupi.")
                                                                ulang_pembayaran = input("Apakah Anda ingin mengulangi pembayaran? (Ya/Tidak): ")
                                                                if ulang_pembayaran.strip().lower() == 'ya':
                                                                    pass
                                                                elif ulang_pembayaran.strip().lower() == 'tidak':
                                                                    pembayaran = True
                                                                    go_back_informasi_produk = True
                                                                else:
                                                                    os.system('cls')
                                                                    print("Pilihan tidak valid. Silakan masukkan kembali.")
                                                                    time.sleep(2)
                                                    else:
                                                        print("Pesanan dibatalkan.")
                                                else:
                                                    os.system('cls')
                                                    print("Jumlah pesanan tidak valid. Silakan masukkan kembali jumlah pesanan anda.")
                                                    time.sleep(2)
                                elif produk[0].strip().lower() != pilih_produk.strip().lower():
                                    print("Produk tidak ditemukan.")
                        # Opsi Kembali ke Menu Produk
                            print('=' * 40)
                            kembali = input('Kembali? (Ya/Tidak): ')
                            os.system('cls')
                            if kembali.strip().lower() == 'ya':
                                go_back_produk = True
                            elif kembali.strip().lower() == 'tidak':
                                pass
                            else:
                                os.system('cls')
                                print('Pilihan tidak valid. Silakan masukkan kembali')
                                time.sleep(2)

        # Menu Utama > Keranjang Belanja
                    elif pilihan_menu.strip() == "2":
                        go_back_keranjang_belanja = False
                        while not go_back_keranjang_belanja:
                            os.system('cls')
                            print('=' * 40)
                            print('             KERANJANG BELANJA             ')
                            print('=' * 40)
                            for produk in list_keranjang_belanja:
                                print(f'- {produk[0]}')
                            list_nama_produk_keranjang = [produk[0] for produk in list_keranjang_belanja]
                            if not list_nama_produk_keranjang:
                                print('Keranjang belanja kosong.')
                                kembali = input('Kembali? (Ya/Tidak) :')
                                if kembali.strip().lower() == 'ya':
                                    go_back_keranjang_belanja = True
                                else:
                                    pass
                            else:
                                print('=' * 40)
                                for produk in list_produk:
                                    print(f'- {produk[0]}')
                                print('=' * 40)
                                print('1. Beli Produk')
                                print('2. Beli Semua')
                                print('3. Hapus Produk')
                                print('4. Kembali')
                                print('=' * 40)
                                opsi_keranjang = input('Pilih Opsi (1/2/3/4): ')
                                list_pesanan_sementara = []
                                if opsi_keranjang == '1':
                                    pilih_produk_keranjang = input("Masukkan nama produk yang ingin dibayar: ")
                                    go_back_beli_produk = False
                                    for produk in list_keranjang_belanja:
                                        if produk[0].strip().lower() == pilih_produk_keranjang.strip().lower():
                                            while not go_back_beli_produk:
                                                os.system('cls')
                                                print(f'Nama Produk: {produk[0]}')
                                                print(f'Harga Produk: {produk[1]}')
                                                print(f'Kategori Produk: {produk[2]}')
                                                print(f'Detail Produk: {produk[3]}')
                                                print(f'Deskripsi Produk: {produk[4]}')
                                                print(f'Variasi Produk: {produk[5]}')
                                                print(f'Kondisi Produk: {produk[6]}')
                                                print(f'Stok Produk: {produk[7]}')
                                                print(f'Berat Produk: {produk[8]}')
                                                print(f'Opsi Asuransi Pengiriman: {produk[9]}')
                                                print(f'Detail Pengiriman: {produk[10]}')
                                                uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
                                                if uang_bayar >= total_harga:
                                                    kembalian = uang_bayar - total_harga
                                                    print(f'Pembayaran berhasil! Kembalian: {kembalian}')
                                                    produk[7] = str(int(produk[7]) - jumlah_pesanan)
                                                    penyimpanan_uang_admin += total_harga
                                                    status_pesanan = 'Menunggu'
                                                    list_pesanan_sementara.append(produk[0])
                                                    list_pesanan_sementara.append(status_pesanan)
                                                    list_pesanan.append(list_pesanan_sementara)
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
                                                        print("Pilihan tidak valid. Silakan masukkan kembali.")
                                                        time.sleep(2)
                                elif opsi_keranjang == '2':
                                    for produk in list_keranjang_belanja:
                                        print(f'Nama Produk: {produk[0]}')
                                        print(f'Harga Produk: {produk[1]}')
                                        print('=' * 40)
                                        total_harga = 0
                                        for item in list_keranjang_belanja:
                                            produk = item[0]
                                            jumlah_pesanan = item[1]
                                            subtotal = jumlah_pesanan * int(produk[1])
                                            total_harga += subtotal
                                            print(f'Total Harga: {total_harga}')
                                            konfirmasi_pesanan = input("Apakah Anda ingin melanjutkan ke pembayaran? (Ya/Tidak): ")
                                            if konfirmasi_pesanan.strip().lower() == 'ya':
                                            # Pembayaran Produk
                                                pembayaran = False
                                                while not pembayaran:
                                                    uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
                                                    if uang_bayar >= total_harga:
                                                        kembalian = uang_bayar - total_harga
                                                        os.system('cls')
                                                        print(f'Pembayaran berhasil! Kembalian: {kembalian}')
                                                        print('=' * 40)
                                                        kembali = input('Tekan Enter Untuk Kembali')
                                                        produk[7] = str(int(produk[7]) - jumlah_pesanan)
                                                        penyimpanan_uang_admin += total_harga
                                                        status_pesanan = 'Menunggu'
                                                        list_pesanan_sementara.append(produk[0])
                                                        list_pesanan_sementara.append(status_pesanan)
                                                        list_pesanan.append(list_pesanan_sementara)
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
                                                            print("Pilihan tidak valid. Silakan masukkan kembali.")
                                                            time.sleep(2)


        # Menu Utama > Status Pesanan
                    elif pilihan_menu.strip() == "3":
                        os.system('cls')
                        print('=' * 40)
                        print('             STATUS PESANAN             ')
                        print('=' * 40)
                        if status_pesanan == 'none':
                            print('Anda belum memesan produk')
                            print('=' * 40)
                            kembali = input('Tekan Untuk Kembali')
                            os.system('cls')
                        else:
                            os.system('cls')
                            for produk in list_pesanan:
                                print(f'{produk[0]} : {produk[1]}')
                                print('=' * 40)
                            kembali = input('Tekan Untuk Kembali')

        # Menu Utama > Kelola Akun
                    elif pilihan_menu.strip() == "4":
                        go_back_kelola_akun = False
                        while not go_back_kelola_akun:
                            os.system('cls')
                            print('=' * 40)
                            print('             AKUN PENGGUNA             ')
                            print('=' * 40)
                            print('1. Ubah Username')
                            print('2. Ubah Password')
                            print('3. Kembali')
                            opsi_kelola_akun = input('Pilih Opsi (1/2/3): ')
                            if opsi_kelola_akun.strip() == '1':
                                for i in range(len(list_username)):
                                    username_log_in == list_username[i]
                                    list_username[i] = input('Masukkan Username Baru: ')
                            elif opsi_kelola_akun.strip() == '2':
                                for i in range(len(list_username)):    
                                    password_log_in == list_password[i]
                                    list_password[i] = input('Masukkan Password Baru: ')
                                    print('Password berhasil diganti!')
                            elif opsi_kelola_akun.strip() == '3':
                                go_back_kelola_akun = True
                            else:
                                os.system('cls')
                                print('Pilihan tidak valid.  Silakan masukkan kembali.')
                                time.sleep
                        
                            

        # Menu Utama > Log Out
                    elif pilihan_menu.strip() == "5":
                        go_back_menu_utama = True