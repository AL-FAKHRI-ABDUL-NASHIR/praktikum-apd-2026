umur = int(input("Masukkan Umur Anda: "))
if umur >= 13:
 nama = input("Masukkan Nama Anda: ")

 jenis_tiket = input("Masukkan Jenis Tiket Anda (Reguler / Premium / VIP): ")
 if jenis_tiket == "Reguler":
  harga_tiket = 50000
 elif jenis_tiket == "Premium":
  harga_tiket = 75000
 elif jenis_tiket == "VIP":
   harga_tiket = 100000
 else:
  pass

 if jenis_tiket == "Reguler" or jenis_tiket == "Premium" or jenis_tiket == "VIP":
  member = input("Apakah Anda Sudah Terdaftar Sebagai Member? (Ya / Tidak): ")
  nominal_diskon = harga_tiket * 0.2 if member == "Ya" else 0 if member == "Tidak" else member == "Invalid"
  biaya_admin = 0 if member == "Ya" else 2000 if member == "Tidak" else member == "Invalid"

  if member == "Ya" or member == "Tidak":
   total_bayar = harga_tiket - nominal_diskon + biaya_admin
   uang_bayar = int(input("Masukkan Uang Yang Dibayarkan: "))
   kembalian = uang_bayar - total_bayar

   if uang_bayar >= total_bayar:
    print("Nama: ", nama)
    print("Umur: ", umur)
    print("Jenis Tiket: ", jenis_tiket)
    print("Status Member: ", member)
    print("Total Bayar: ", total_bayar)
    print("Uang Kembalian: ", kembalian)
   else:
    print("Uang Anda tidak mencukupi. Silahkan masukkan kembali.")

  else:
   print("Pilihan Tidak Valid.")

 else:
  print("Jenis tiket tidak valid. Silahkan masukkan kembali.")

else:
 print("Mohon maaf, anda belum cukup umur untuk menonton")