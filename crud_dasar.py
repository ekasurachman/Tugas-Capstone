# Tugas 1 Capstone
# Eka Surachman
# Sample data
data = [
    {'NIM': '12A', 'Nama': 'Reefy', 'Gender': 'Pria', 'Kota': 'Cirebon', 'Agama': 'Islam'},
    {'NIM': '12B', 'Nama': 'Yusuf', 'Gender': 'Pria', 'Kota': 'Cirebon', 'Agama': 'Islam'},
    {'NIM': '12C', 'Nama': 'Nita', 'Gender': 'Wanita', 'Kota': 'Purwakarta', 'Agama': 'Islam'}
]


# data.index = pd.RangeIndex(start=1, stop=len(data)+1) # Memulai index dari 1
# data.index.name = 'No.'

# Warna Header Tabel pada Data Siswa
GREEN = "\033[32m"
RESET = "\033[0m"

# Fungsi Membuat Tabel dengan Header Berwarna
def gt(data):
    if not data:
        print("Data tidak tersedia.")
        return

    # Determine column names and widths
    col_names = data[0].keys()  # Get column names from the first dictionary
    col_widths = [max(len(str(item[col])) for item in data) for col in col_names]

    def row_separator():
        return "+-" + "-+-".join(["-" * width for width in col_widths]) + "-+"

    print(row_separator())
    
    # Print header with color
    colored_header = " | ".join([f"{GREEN}{col:{col_widths[i]}}{RESET}" for i, col in enumerate(col_names)])
    print(f"| {colored_header} |")
    
    print(row_separator())
    
    for item in data:
        row_str = " | ".join([f"{str(item[col]):{col_widths[i]}}" for i, col in enumerate(col_names)])
        print(f"| {row_str} |")
        print(row_separator())

# Fungsi agar pilihan menu dimasukkan ke dalam tabel
def pilihan(menu_items):
    # Calculate the width of the columns
    max_item_length = max(len(item) for item in menu_items)
    column_width = max_item_length + 3  # Add padding for borders

    def row_separator():
        return "+-" + "-+-".join(["-" * column_width]) + "-----+"

    # Print the top border
    print(row_separator())

    # Print the header row with center alignment
    header_no = "No."
    header_pilihan = "Pilihan"
    print(f"| {header_no:^3} | {header_pilihan:^{column_width - 2}} |")
    
    # Print the separator line after the header
    print(row_separator())

    # Print each menu item
    for index, item in enumerate(menu_items, start=1):
        print(f"| {index:^3} | {item:<{column_width - 2}} |")
    
    # Print the bottom border
    print(row_separator())

# Membuat judul menu agar berada di tengah 
def judul_tengah(text, lebar):
    centered_text = text.center(lebar)
    print()
    print('='*lebar)
    print(centered_text)
    print('='*lebar)

def read():
    while True:
        judul_tengah('Menampilkan Data Siswa', 36)
        menu1 = [
            'Menampilkan Seluruh Data',
            'Menampilkan Data Tertentu',
            'Kembali ke Menu Utama'
        ]
        pilihan(menu1)

        i1 = input('Pilih menu [1-3]: ')

        if i1 == '1':
            gt(data)  # Display all student data
        elif i1 == '2':
            while True:
                judul_tengah('Pilih Metode Pencarian Data', 30)
                menu1_2 = [
                    'NIM',
                    'Nama',
                    'Kembali'
                ]
                pilihan(menu1_2)
                i12 = input("Pilih menu [1-3]: ")

                if i12 == '1':
                    input_nim = input('Masukkan NIM Mahasiswa: ').upper()
                    filtered_data = [student for student in data if student['NIM'] == input_nim]
                    if filtered_data:
                        gt(filtered_data)
                    else:
                        print()
                        judul_tengah(f'Data {input_nim} tidak ditemukan', 25)
                elif i12 == '2':
                    input_nama = input('Masukkan Nama Mahasiswa: ').capitalize()
                    filtered_data = [student for student in data if input_nama in student['Nama']]
                    if filtered_data:
                        gt(filtered_data)
                    else:
                        print()
                        judul_tengah(f'Data {input_nama} tidak ditemukan', 30)
                        print()
                elif i12 == '3':
                    break  # Exit the inner loop
                else:
                    print()
                    judul_tengah("Pilihan tidak valid. Silakan pilih antara 1-3.", 50)
                    print()
        elif i1 == '3':
            break  # Exit the outer loop
        else:
            judul_tengah("Pilihan tidak valid. Silakan pilih antara 1-3.", 50)
            print()



def create():
    global data
    while True:
        judul_tengah('Menambah Data Siswa', 32)
        menu2 = ['Tambah Data Siswa', 'Kembali ke Menu Utama']
        pilihan(menu2)
        i2 = input('Pilih menu [1-2]: ')

        if i2 == '1':
            judul_tengah('Masukkan Biodata Baru', 30)
            nim = input('Masukkan NIM Mahasiswa: ').upper()
            if any(student['NIM'] == nim for student in data):
                judul_tengah(f'Data NIM {nim} sudah ada', 30)
            else:
                nama = input('Masukkan Nama Mahasiswa: ').capitalize()
                gender = input('Masukkan Gender [Pria/Wanita]: ').capitalize()
                if gender not in ['Pria', 'Wanita']:
                    judul_tengah('Input tidak valid', 20)
                else:
                    kota = input('Masukkan Kota Asal: ').capitalize()
                    agama = input('Masukkan Agama: ').capitalize()

                # Create a new dictionary with the new data
                new_data = {
                    'NIM': nim,
                    'Nama': nama,
                    'Gender': gender,
                    'Kota': kota,
                    'Agama': agama
                }

                # Append the new data to the existing list
                data.append(new_data)
                print()
                judul_tengah(f"Data siswa atas nama {nama} berhasil ditambahkan.", 40)
        elif i2 == '2':
            break



def update():
    global data
    while True:
        input_nim = input('Masukkan NIM Mahasiswa: ').upper()
        # Find the student based on NIM
        student = next((s for s in data if s['NIM'] == input_nim), None)

        if student:
            gt([student])  # Display the current student data
            print()
            judul_tengah("Pilih data yang akan diubah", 28)
            menu3_1 = [
                'Nama',
                'Gender',
                'Kota',
                'Agama',
                'Kembali'
            ]
            pilihan(menu3_1)
            i31 = input('Pilih menu [1-5]: ')

            if i31 == '1':
                new_nama = input('Masukkan Nama Mahasiswa: ').capitalize()
                q = input('Apakah yakin nama akan diubah? [Y/N]: ').upper()
                if q == 'Y':
                    student['Nama'] = new_nama
                    print(f"Data siswa atas nama {new_nama} berhasil diubah.")
                    break
                elif q == 'N':
                    break

            elif i31 == '2':
                new_gender = input('Masukkan Gender [Pria/Wanita]: ').capitalize()
                if new_gender not in ['Pria', 'Wanita']:
                    print("Input tidak valid. Gender harus 'Pria' atau 'Wanita'.")
                    continue
                q = input('Apakah yakin gender akan diubah? [Y/N]: ').upper()
                if q == 'Y':
                    student['Gender'] = new_gender
                    print(f"Data gender siswa berhasil diubah menjadi {new_gender}.")
                    break
                elif q == 'N':
                    break

            elif i31 == '3':
                new_kota = input('Masukkan Kota Asal: ').capitalize()
                q = input('Apakah yakin kota akan diubah? [Y/N]: ').upper()
                if q == 'Y':
                    student['Kota'] = new_kota
                    print(f"Data kota asal siswa berhasil diubah menjadi {new_kota}.")
                    break
                elif q == 'N':
                    break

            elif i31 == '4':
                new_agama = input('Masukkan Agama: ').capitalize()
                q = input('Apakah yakin agama akan diubah? [Y/N]: ').upper()
                if q == 'Y':
                    student['Agama'] = new_agama
                    print(f"Data agama siswa berhasil diubah menjadi {new_agama}.")
                    break
                elif q == 'N':
                    break

            elif i31 == '5':
                break  # Exit the update function

            else:
                print()
                judul_tengah("Pilihan tidak valid.", 30)
                print()
        else:
            print()
            judul_tengah("NIM tidak ditemukan.", 30)
            print()

def delete():
    global data
    while True:
        judul_tengah('Menghapus Data Siswa', 32)
        menu4 = [
            'Hapus Data Siswa',
            'Kembali ke Menu Utama'
        ]
        pilihan(menu4)
        i4 = input('Pilih menu [1-2]: ')

        if i4 == '1':
            input_nim = input('Masukkan NIM Mahasiswa: ').upper()
            student_index = next((index for index, s in enumerate(data) if s['NIM'] == input_nim), None)

            if student_index is not None:
                gt([data[student_index]])  
                q = input('Apakah yakin data akan dihapus? [Y/N]: ').upper()
                if q == 'Y':
                    del data[student_index] 
                    print(f"Data dengan NIM {input_nim} berhasil dihapus.")
                elif q == 'N':
                    print("Penghapusan data dibatalkan.")
                    break
            else:
                judul_tengah(f'Data NIM {input_nim} tidak ditemukan.', 26)
                print()

        elif i4 == '2':
            break  

        else:
            judul_tengah("Pilihan tidak valid. Silakan pilih antara 1-2.", 45)
            print()

def crud_dasar():
    a = True
    while a:
        menu = [
        "Menampilkan Data Siswa",
        "Menambahkan Data Siswa",
        "Mengubah Data Siswa",
        "Menghapus Data Siswa",
        "Keluar"
        ]
        pilihan(menu)
        i = input("Pilih menu: ")

        try:
            i = int(i)
        except ValueError:
            print("Input tidak valid. Silakan masukkan nomor menu yang benar.", 50)
            print()
            continue

        if i == 1:
            read()
        elif i == 2:
            create()
        elif i == 3:
            update()
        elif i == 4:
            delete()
        elif i == 5:
            break
        else:
            judul_tengah("Menu tidak valid. Silakan pilih menu yang tersedia.", 45)
            print()

crud_dasar()