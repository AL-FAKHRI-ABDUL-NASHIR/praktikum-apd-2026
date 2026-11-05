import setup_variables as setvar
import setup_list_produk as setlpr

def tampilan_komentar(halaman_komentar):
    for produk_komen in halaman_komentar["nama_produk"]:
        if produk_komen == setvar.list_produk["nama_produk"][setlpr.indeks_list_produk]:
            isi_komentar = halaman_komentar["komentar_produk"].index(produk_komen)
            print(produk_komen)
            print(produk_komen[isi_komentar])