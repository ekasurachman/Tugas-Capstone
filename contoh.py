# Data Mahasiswa, menggunakan list untuk menyimpan beberapa dictionary (data mahasiswa)
data_mahasiswa = []

# Fungsi untuk menambahkan data mahasiswa (Create)
def tambah_mahasiswa():
    print("\n=== Tambah Data Mahasiswa ===")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    usia = input("Masukkan Usia: ")
    jurusan = input("Masukkan Jurusan: ")
    semester = input("Masukkan Semester: ")
    ipk = input("Masukkan IPK: ")

    mahasiswa = {
        "NIM": nim,
        "Nama": nama,
        "Usia": usia,
        "Jurusan": jurusan,
        "Semester": semester,
        "IPK": ipk
    }
    
    data_mahasiswa.append(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan!\n")

# Fungsi untuk menampilkan seluruh data mahasiswa (Read)
def lihat_mahasiswa():
    if len(data_mahasiswa) == 0:
        print("\nTidak ada data mahasiswa.\n")
    else:
        print("\n=== Data Mahasiswa ===")
        for index, mahasiswa in enumerate(data_mahasiswa, start=1):
            print(f"Mahasiswa {index}")
            print(f"NIM       : {mahasiswa['NIM']}")
            print(f"Nama      : {mahasiswa['Nama']}")
            print(f"Usia      : {mahasiswa['Usia']}")
            print(f"Jurusan   : {mahasiswa['Jurusan']}")
            print(f"Semester  : {mahasiswa['Semester']}")
            print(f"IPK       : {mahasiswa['IPK']}\n")

# Fungsi untuk mengedit data mahasiswa berdasarkan NIM (Update)
def edit_mahasiswa():
    nim = input("\nMasukkan NIM mahasiswa yang akan diedit: ")
    
    for mahasiswa in data_mahasiswa:
        if mahasiswa['NIM'] == nim:
            print("\n=== Edit Data Mahasiswa ===")
            mahasiswa['Nama'] = input("Masukkan Nama baru: ")
            mahasiswa['Usia'] = input("Masukkan Usia baru: ")
            mahasiswa['Jurusan'] = input("Masukkan Jurusan baru: ")
            mahasiswa['Semester'] = input("Masukkan Semester baru: ")
            mahasiswa['IPK'] = input("Masukkan IPK baru: ")
            print("Data mahasiswa berhasil diperbarui!\n")
            return
    print("Data mahasiswa tidak ditemukan.\n")

# Fungsi untuk menghapus data mahasiswa berdasarkan NIM (Delete)
def hapus_mahasiswa():
    nim = input("\nMasukkan NIM mahasiswa yang akan dihapus: ")
    
    for index, mahasiswa in enumerate(data_mahasiswa):
        if mahasiswa['NIM'] == nim:
            del data_mahasiswa[index]
            print("Data mahasiswa berhasil dihapus!\n")
            return
    print("Data mahasiswa tidak ditemukan.\n")

# Fungsi untuk menampilkan menu pilihan
def tampilkan_menu():
    print("=== Aplikasi Data Mahasiswa ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Lihat Data Mahasiswa")
    print("3. Edit Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Keluar")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            lihat_mahasiswa()
        elif pilihan == "3":
            edit_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# Menjalankan program
main()
