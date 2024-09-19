#Tugas Capstone 1 CRUD Dasar
#Eka Surachman
import pandas as pd

# Sample data
data = pd.DataFrame({
    'NIM': ['12A', '12B'],
    'Nama': ['Reefy', 'Yusuf'],
    'Gender': ['Pria', 'Pria'],
    'Kota': ['Cirebon', 'Cirebon'],
    'Agama': ['Islam', 'Islam']
})


data.index = pd.RangeIndex(start=1, stop=len(data)+1) # Memulai index dari 1
data.index.name = 'No.'

# Warna Header Tabel pada Data Siswa
GREEN = "\033[32m"
RESET = "\033[0m"

# Fungsi Membuat Tabel dengan Header Berwarna
def gt(df, color=GREEN):
    # Untuk mengetahui lebar kolom
    col_widths = [max(df[col].astype(str).map(len).max(), len(col)) for col in df.columns]
    
    # Membuat garis pemisah antar baris
    def row_separator():
        return "+-" + "-+-".join(["-" * width for width in col_widths]) + "-+"

    # Print header separator
    print(row_separator())
    
    # Print header with color
    colored_header = " | ".join([f"{color}{col:{col_widths[i]}}{RESET}" for i, col in enumerate(df.columns)])
    print(f"| {colored_header} |")
    
    # Print row separator
    print(row_separator())
    
    # Print rows with border lines
    for _, row in df.iterrows():
        row_str = " | ".join([f"{str(row[col]):{col_widths[i]}}" for i, col in enumerate(df.columns)])
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
    a1 = True
    while a1:
        judul_tengah('Menampilkan Data Siswa', 36)
        menu1 =[
        'Menampilkan Seluruh Data',
        'Menampilkan Data Tertentu',
        'Kembali ke Menu Utama'
        ]
        pilihan(menu1)

        i1 = input('Pilih menu [1-3]: ')

        try:
            i1 = int(i1)
        except ValueError:
            print()
            print('='*50)
            print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
            print('='*50)
            continue

        if i1 == 1:
            gt(data)
        elif i1 == 2:
            a12 = True
            while a12:
                judul_tengah('Pilih Metode Pencarian Data', 30)
                menu1_2 = [
                    'NIM',
                    'Nama',
                    'Kembali'
                ]
                pilihan(menu1_2)
                i12 = input("Pilih menu [1-3]: ")

                try:
                    i12 = int(i12)
                except ValueError:
                    print()
                    print('='*50)
                    print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
                    print('='*50)
                    continue

                if i12 == 1:
                    input_nim = input('Masukkan NIM Mahasiswa: ').upper() #memasukkan nim siswa
                    filtered_data = data[data['NIM'] == input_nim]
                    if not filtered_data.empty:
                        gt(filtered_data)
                    else:
                        print()
                        judul_tengah(f'Data {input_nim} tidak ditemukan',25)
                elif i12 == 2:
                    input_nama = input('Masukkan Nama Mahasiswa: ').capitalize() #memasukkan nim siswa
                    filtered_data = data[data['Nama'].str.contains(input_nama, case=False, na=False)]
                    if not filtered_data.empty:
                        gt(filtered_data)
                    else:
                        print()
                        print('='*50)
                        print(f'Data {input_nama} tidak ditemukan')
                        print('='*50)
                elif i12 == 3:
                    a12 = False
        elif i1 == 3:
            a1 = False
        else:
            print()
            print('='*50)
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")
            print('='*50)



def create():
    global data
    a2 = True
    while a2:
        judul_tengah('Menambah Data Siswa', 32)
        menu2 = [
        'Tambah Data Siswa',
        'Kembali ke Menu Utama'
        ]
        pilihan(menu2)
        i2 = input('Pilih menu [1-2]: ')

        try:
            i2 = int(i2)
        except ValueError:
            print()
            print('='*50)
            print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
            print('='*50)
            continue

        if i2 == 1:
            judul_tengah('Masukkan Biodata Baru', 30)
            nim = input('Masukkan NIM Mahasiswa: ').upper()
            if nim in data['NIM'].values:
                judul_tengah(f'Data NIM {nim} sudah ada', 30)
            else:
                nama = input('Masukkan Nama Mahasiswa: ').capitalize()
                gender = input('Masukkan Gender [Pria/Wanita]: ').capitalize()
                if gender not in ['Pria','Wanita']:
                    judul_tengah('Input tidak valid', 20)
                else:
                    kota = input('Masukkan Kota Asal: ').capitalize()
                    agama = input('Masukkan Agama: ').capitalize()

                # Create a new DataFrame with the new data
                    new_data = pd.DataFrame({
                        'NIM': [nim],
                        'Nama': [nama],
                        'Gender': [gender],
                        'Kota': [kota],
                        'Agama': [agama]
                    })

                # Append the new data to the existing DataFrame
                    data = pd.concat([data, new_data], ignore_index=True)
                    print()
                    judul_tengah(f"Data siswa atas nama {nama} berhasil ditambahkan.", 50)

        elif i2 == 2:
            a2 = False
        else:
            print()
            print('='*50)
            print("Pilihan tidak valid. Silakan pilih antara 1-2.")
            print('='*50)


def update(): # FUNGSI MENGEDIT DATA
    global data
    a31 = True
    while a31:
        input_nim = input('Masukkan NIM Mahasiswa: ').upper()
        if input_nim in data['NIM'].values:
        # Select row to update
            row_index = data[data['NIM'] == input_nim].index[0]
            gt(data[data['NIM']==input_nim])
            print()            
            judul_tengah("Pilih data yang akan diubah", 28)
            print()
            menu3_1 = [
                'Nama',
                'Gender',
                'Kota',
                'Agama',
                'Kembali'
            ]
            pilihan(menu3_1)
            i31 = input('Pilih menu [1-5]: ')
            i31 = int(i31)

            if i31 == 1:
                print('Masukkan Data Terbaru')
                new_nama = input('Masukkan Nama Mahasiswa: ').capitalize()
                q = input('Apakah yakin nama akan diubah? [Y/N]: ').upper()
                try:
                    if q == 'Y':
                        data.loc[row_index, 'Nama'] = new_nama
                        print(f"Data siswa atas nama {new_nama} berhasil diubah.")
                        a31 = False
                    elif q == 'N':
                        a31 = False
                except ValueError:
                    print()
                    print('='*50)
                    print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
                    print('='*50)
                    continue

            elif i31 == 2:
                print('Masukkan Data Terbaru')
                new_gender = input('Masukkan Gender [L/P]: ').upper()
                q = input('Apakah yakin gender akan diubah? [Y/N]: ').upper()
                try:
                    if q == 'Y':
                        data.loc[row_index, 'Gender'] = new_gender
                        print(f"Data gender siswa berhasil diubah menjadi {new_gender}.")
                        a31 = False
                    elif q == 'N':
                        a31 = False
                except ValueError:
                    print()
                    print('='*50)
                    print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
                    print('='*50)
                    continue
            elif i31 == 3:
                print('Masukkan Data Terbaru')
                new_kota = input('Masukkan Kota Asal: ').capitalize()
                q = input('Apakah yakin nama akan diubah? [Y/N]: ').upper()
                try:
                    if q == 'Y':
                        data.loc[row_index, 'Kota'] = new_kota
                        print(f"Data kota asal siswa berhasil diubah menjadi {new_kota}.")
                        a31 = False
                    elif q == 'N':
                        a31 = False
                except ValueError:
                    print()
                    print('='*50)
                    print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
                    print('='*50)
                    continue
            elif i31 == 4:
                print('Masukkan Data Terbaru')
                new_agama = input('Masukkan Agama: ').capitalize()
                q = input('Apakah yakin nama akan diubah? [Y/N]: ').upper()
                try:
                    if q == 'Y':
                        data.loc[row_index, 'Agama'] = new_agama
                        print(f"Data agama siswa berhasil diubah menjadi {new_agama}.")
                        a31 = False
                    elif q == 'N':
                        a31 = False
                except ValueError:
                    print()
                    print('='*50)
                    print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
                    print('='*50)
                    continue
            elif i31 == 5:
                a31 = False

            else:
                print()
                print('='*50)
                print("Pilihan tidak valid.")
                print('='*50)
        else:
            print()
            print('='*20)
            print("Input tidak valid.")
            print('='*20)

def delete():
    a4 = True
    while a4:
        judul_tengah('Menghapus Data Siswa', 32)
        menu4 = [
            'Hapus Data Siswa',
            'Kembali ke Menu Utama'
        ]
        pilihan(menu4)
        i4 = input('Pilih menu [1-2]: ')

        try:
            i4 = int(i4)
        except ValueError:
            print()
            print('='*50)
            print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
            print('='*50)
            continue
        
        if i4 == 1:
            a41 = True
            while a41:
                input_nim = input('Masukkan NIM Mahasiswa: ').upper()
                filtered_data = data[data['NIM'] == input_nim]
                if not filtered_data.empty:
                    # Select row to update
                    row_index = data[data['NIM'] == input_nim].index[0]
                    gt(data[data['NIM']==input_nim])
                    q = input('Apakah yakin data akan dihapus? [Y/N]: ').upper()
                    try:
                        if q == 'Y':
                            data.drop(row_index, inplace=True)
                            print(f"Data berhasil dihapus.")
                            a41 = False
                        elif q == 'N':
                            a41 = False
                    except ValueError:
                        print()
                        print('='*50)
                        print("Input tidak valid. Silakan masukkan input menu yang benar.")
                        print('='*50)
                        continue                        
                else:
                    print()
                    print('='*26)
                    print(f'Data NIM {input_nim} tidak ditemukan')
                    print('='*26)

        elif i4 == 2:
            a4 = False
        else:
            print()
            print('='*50)
            print("Pilihan tidak valid. Silakan pilih antara 1-2.")
            print('='*50)

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
            print()
            print('='*50)
            print("Input tidak valid. Silakan masukkan nomor menu yang benar.")
            print('='*50)
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
            print()
            print('='*50)
            print("Menu tidak valid. Silakan pilih menu yang tersedia.")
            print('='*50)

crud_dasar()