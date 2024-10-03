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
