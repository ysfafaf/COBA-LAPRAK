print("Halo Gais")

class PembelianBuku:
    def __init__(self, buku, harga):
        self.buku = buku
        self.harga = harga
        self.status = ""
        self.nama = ""

    def IdentitasPembeli(self):
        self.nama = input("Masukan Nama Anda: ")
        self.status = input("Anda Berasal dari Prodi Teknik Apa?: ")
