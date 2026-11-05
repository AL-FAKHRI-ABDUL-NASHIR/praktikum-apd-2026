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
    'nama_pengguna' : [],
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
    'nama_pengguna' : [],
    'jumlah_pesanan' : [],
    'uang_bayar' : [],
    'kembalian' : []
}

# Database Riwayat Transaksi
list_riwayat_transaksi = {
    'nama_pengguna' : [],
    'nama_produk' : [],
    'harga_produk' : [],
    'kategori_produk' : [],
    'detail_produk' : [],
    'deskripsi_produk' : [],
    'kondisi_produk' : [],
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