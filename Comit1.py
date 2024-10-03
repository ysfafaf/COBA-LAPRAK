class PembelianBuku:
    
    def __init__(self, buku, harga):
        self.buku = buku
        self.harga = harga
        self.status = ""
        self.nama = ""

    def indentitas_pembeli(self):
        self.nama = input("masukan nama : ")
        self.status = input("Anda Berasal dari prodi apa? : ")
        
    def pilihan_buku(self):
        print("Matematika           = Rp90.000")
        print("Fisika               = Rp80.000")
        print("Kalkulus             = Rp85.000")
        print("Aljabar              = Rp80.000")
        print("kimia                = Rp90.000")
        print("Elektronika Dasar    = Rp85.000")

        print("==================================================")

    def RekomendasiBuku(self):
        Komputer = "Kalkulus, Aljabar"
        Elektro = "Kimia, Eldas"
        Sipil = "Fisika, Matematika"
        Arsitektur = "Fisika, Matematika"
    
        if self.status.lower() == "komputer":
            print("Rekomendasi Buku Untuk Jurusan Teknik Komputer:")
            print(Komputer)
            print("=============================================")
        elif self.status.lower() == "elektro":
            print("Rekomendasi Buku Untuk Jurusan Teknik Elektro:")
            print(Elektro)
            print("=============================================")
        elif self.status.lower() == "sipil":
            print("Rekomendasi Buku Untuk Jurusan Teknik Sipil:")
            print(Sipil)
            print("=============================================")
        elif self.status.lower() == "arsitektur":
            print("Rekomendasi Buku Untuk Jurusan Arsitektur:")
            print(Arsitektur)
            print("=============================================")

    def MilihBuku(self):
        self.Dipilih = []
        self.Buku = ["matematika", "fisika", "kalkulus", "aljabar", "kimia", "eldas"]
        while True:
            Milih = input("Mau Buku Yang Mana (ketik 'selesai' jika sudah selesai): ")
            if Milih.lower() == "selesai":
                break
            if Milih.lower() in self.Buku:
                self.Dipilih.append(Milih.lower())
                print("Baik, Kamu telah memilih buku", self.Dipilih)
            else:
                print("Buku tidak tersedia, silakan pilih lagi.")

    def KonfirmasiBayar(self):
        harga_buku = {"matematika": 90000, 
                      "fisika": 80000, 
                      "kalkulus": 85000, 
                      "aljabar" : 80000, 
                      "kimia" : 90000, 
                      "eldas" : 85000}
        total = sum([harga_buku[buku] for buku in self.Dipilih])
        print("Kamu telah memilih buku", self.Dipilih)
        print("Maka, total harganya adalah:", "Rp.",total)
        Bayar = input("Apakah kamu bersedia membayarnya (ya/tidak) : ")
        if Bayar == "ya":
            print("Terima Kasih Telah Berbelanja di Toko Kami! ")
        if Bayar == "tidak":
            print("Baik, semoga diberikan rezeki yang berlimpah yaa")

    def JalankanProgram(self):
        print("Selamat Datang di Toko Kami". center(120,"="))
        print("Disini Kami Menjual Buku untuk Mahasiswa Fakultas Teknik, Khususnya Teknik Komputer, Elektro, Sipil, dan Arsitektur")
        
        while True:

            print("1. Identitas ")
            print("2. Pilihan Buku")
            print("3. Beli Buku")
            print("4. Keluar")
            opsi = input("Pilih Opsi (1-4) : ")
            if opsi == "1":
                self.IdentitasPembeli()
            elif opsi == "2":
                self.PilihanBuku()
                self.RekomendasiBuku()
            elif opsi == "3":
                self.MilihBuku()
                self.KonfirmasiBayar()
                break
            elif opsi == '4':
                break
            else:
                print("Opsi tidak valid, silakan pilih lagi.")

pembelian = PembelianBuku([], [])

pembelian.JalankanProgram()
