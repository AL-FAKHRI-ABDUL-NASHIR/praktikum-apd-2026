username_pengirim = "Al Fakhri"
password = "009"
username_pengirim_verif = input("Masukkan Username : ")
password_verif = input("Masukkan Password : ")
if username_pengirim_verif == username_pengirim and password_verif == password:
    pass
else:
    kesempatan = 1
    while username_pengirim_verif != username_pengirim or password_verif != password: 
        if kesempatan < 3:
            if username_pengirim_verif != username_pengirim and password_verif != password:
                print("\nUsername dan Password anda salah. Silahkan masukkan kembali")
                username_pengirim_verif = input("Masukkan Username : ")
                password_verif = input("Masukkan Password : ")
                kesempatan = kesempatan + 1
            elif username_pengirim_verif != username_pengirim:
                print("\nUsername anda salah. Silahkan masukkan kembali")
                username_pengirim_verif = input("Masukkan Username : ")
                password_verif = input("Masukkan Password : ")
                kesempatan = kesempatan + 1
            elif password_verif != password:
                print("\nPassword anda salah. Silahkan masukkan kembali")
                username_pengirim_verif = input("Masukkan Username : ")
                password_verif = input("Masukkan Password : ")
                kesempatan = kesempatan + 1
            else:
              pass
        else:
          exit("\nPengisian salah. Anda diblokir sementara untuk keamanan.")

saldo = 5000000
konfirm_lanjut = "n"
pilihan_menu = "0"
while konfirm_lanjut == "n" or pilihan_menu != "2":
    print("\n===== Menu Utama =====")
    print("1. Transfer Uang")
    print("2. Logout")
    pilihan_menu = input("Pilih Opsi : ")
    while pilihan_menu != "1" and pilihan_menu != "2":
        print("\nPilihan tidak valid. Silahkan masukkan kembali.")
        print("Menu Utama")
        print("1. Transfer Uang")
        print("2. Logout")
        pilihan_menu = input("Pilih Opsi : ")
    konfirm_lanjut = "y"
    if pilihan_menu == "1":
        while konfirm_lanjut == "y":
            print("\nSaldo anda : " + str(saldo))
            username_penerima = input("Masukkan Username Penerima : ")
            nominal_transfer = int(input("Masukkan nominal transfer (min. 50000 & maks. 1000000): "))
            if nominal_transfer >= 50000 and nominal_transfer <= 1000000 and nominal_transfer <= saldo:
                pass
            else:
                while nominal_transfer < 50000 or nominal_transfer > 1000000 or nominal_transfer > saldo:
                    print("Kesalahan. Nominal transfer tidak sesuai ketentuan. Silahkan masukkan kembali.")
                    nominal_transfer = int(input("Masukkan nominal transfer (min. 50000 & maks. 1000000): "))
            PIN = "009009"
            PIN_verif = input("Masukkan PIN anda : ")
            kesempatan = 1
            while PIN_verif != PIN:
                if kesempatan < 3:
                    print("PIN salah. Silahkan masukkan kembali.")
                    PIN_verif = input("Masukkan PIN anda : ")
                    kesempatan = kesempatan + 1
                else:
                    exit("\nPIN salah. Anda diblokir sementara untuk keamanan.")
            saldo = saldo - nominal_transfer
            print("\nSisa saldo anda : " + str(saldo))
            print("\n===== STRUK BUKTI TRANSFER =====")
            print("Username Pengirim : " + username_pengirim)
            print("Username Penerima : " + username_penerima)
            print("Nominal Transaksi : " + str(nominal_transfer))
            konfirm_lanjut = input("\nApakah anda ingin melakukan transfer lagi (y/n)?")
    else:
        exit("\nAnda telah logout.")