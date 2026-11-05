# {Persiapan Error-Handling Tambah Produk}
def test_angka(nama_produk, test_harga, harga_produk, test_harga_selesai, kategori_produk, detail_produk, deskripsi_produk, kondisi_produk, test_stok, stok_produk, test_stok_selesai, test_berat, berat_produk, test_berat_selesai):
    print("=" * 40)
    print("             TAMBAH PRODUK             ")
    print("=" * 40)
    print("=" * 40)
    print("            INFORMASI PRODUK            ")
    print("=" * 40)
    print(f"Masukkan Nama Produk: {nama_produk}")
    if not test_harga:
        return False
    print(f"Masukkan Harga Produk (Rp): {harga_produk}")
    if not test_harga_selesai:
        return True
    print(f"Masukkan Kategori Produk: {kategori_produk}")
    print(f"Masukkan Detail Produk: {detail_produk}")
    print(f"Masukkan Deskripsi Produk: {deskripsi_produk}")
    print(f"Masukkan Kondisi Produk (Baru/Bekas): {kondisi_produk}")
    print("=" * 40)
    print("             BANYAK PRODUK             ")
    print("=" * 40)
    if not test_stok:
        return False
    print(f"Masukkan Stok Produk: {stok_produk}")
    if not test_stok_selesai:
        return True
    print("=" * 40)
    print("             PENGIRIMAN PRODUK             ")
    print("=" * 40)
    if not test_berat:
        return False
    print(f"Masukkan Berat Produk (gram): {berat_produk}")
    if not test_berat_selesai:
        return True