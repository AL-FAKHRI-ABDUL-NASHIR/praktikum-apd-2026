import os
import time

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