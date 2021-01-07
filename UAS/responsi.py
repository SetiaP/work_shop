import csv
import os

csv_filename = 'data_barang.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI DATA BARANG ===")
    print("[1] Lihat Daftar Barang")
    print("[2] Masukan Data Barang Baru")
    print("[3] Perbaharui Data Barang ")
    print("[4] Hapus Barang")
    print("[5] Cari Barang")
    print("[0] Selesai")
    print("------------------------")
    selected_menu = input("Pilih Menu> ")
    
    if(selected_menu == "1"):
        show_barang()
    elif(selected_menu == "2"):
        create_barang()
    elif(selected_menu == "3"):
        edit_barang()
    elif(selected_menu == "4"):
        delete_barang()
    elif(selected_menu == "5"):
        search_barang()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_barang():
    clear_screen()
    barangs = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            barangs.append(row)

    if (len(barangs) > 0):
        labels = barangs.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in barangs:
            print(f'{data[0]} \t {data[1]} \t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_barang():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA', 'FUNGSI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        no = input("No urut: ")
        nama = input("Nama Barang: ")
        fungsi = input("Fungsi Barang: ")

        writer.writerow({'NO': no, 'NAMA': nama, 'FUNGSI': fungsi})
        print("Berhasil disimpan!")

    back_to_menu()


def search_barang():
    clear_screen()
    barangs = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            barangs.append(row)

    no = input("Cari berdasrakan nomer urut> ")

    data_found = []

    indeks = 0
    for data in barangs:
        if (data['NO'] == no):
            data_found = barangs[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Fungsi Barang: {data_found['FUNGSI']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()


def edit_barang():
    clear_screen()
    barangs = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            barangs.append(row)

    print("NO \t NAMA \t\t FUNGSI")
    print("-" * 32)

    for data in barangs:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['FUNGSI']}")

    print("-----------------------")
    no = input("Pilih nomer > ")
    nama = input("nama barang baru: ")
    fungsi = input("fungsi barang baru: ")

    
    indeks = 0
    for data in barangs:
        if (data['NO'] == no):
            contacts[indeks]['NAMA'] = nama
            contacts[indeks]['FUNGSI'] = fungsi
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'FUNGSI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in barangs:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'FUNGSI': new_data['FUNGSI']}) 

    back_to_menu()


def delete_barang():
    clear_screen()
    barangs = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            barangs.append(row)

    print("NO \t NAMA \t\t FUNGSI")
    print("-" * 32)

    for data in barangs:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['FUNGSI']}")

    print("-----------------------")
    no = input("Hapus nomer> ")

   
    indeks = 0
    for data in barangs:
        if (data['NO'] == no):
            barangs.remove(barangs[indeks])
        indeks = indeks + 1

    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'FUNGSI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in barangs:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'FUNGSI': new_data['FUNGSI']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()