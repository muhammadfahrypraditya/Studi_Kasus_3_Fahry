#1. inisialisasi data 
batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedi = []

#2. perulangan nilai dan dan berhenti input
print("= Input Nilai Mahasiswa ==")
print("Ketik 'selesai' untuk mengakhiri input.")
print("minimal nilai yang harus dimasukkan adalah 5, dengan minimal 1 nilai lulus dan 1 nilai remedi.")
print("Ketik 'hapus' untuk menghapus nilai yang sudah dimasukkan.")

while True:
    input_nilai = input("masukkan nilai ujian mahasiswa (atau 'selesai'): ")

    if input_nilai.lower() == 'selesai':
        if len(nilai_masuk) == 0:
            print("Input tidak valid. Harus ada minimal 5 nilai, dan harus ada minimal 1 nilai lulus dan 1 nilai remedi.")
            continue
        else:
            break

#3. menghapus nilai yang sudah dimasukkan
    if input_nilai.lower() == "hapus":
        if len(nilai_masuk) == 0:
            print("Belum ada data untuk dihapus.\n")
            continue
        print("Data saat ini:", nilai_masuk)
        nilai_hapus = input("Masukkan nilai yang ingin dihapus: ")
        try:
            nilai_hapus = int(nilai_hapus)
            if nilai_hapus in nilai_masuk:
                nilai_masuk.remove(nilai_hapus)
                if nilai_hapus in lulus:
                    lulus.remove(nilai_hapus)
                elif nilai_hapus in remedi:
                    remedi.remove(nilai_hapus)
                print(f"Nilai {nilai_hapus} berhasil dihapus.\n")
            else:
                print("Nilai tidak ditemukan dalam data.\n")
        except ValueError:
            print("Input tidak valid.\n")
        continue
#4. pengelompokan nilai menjadi lulus dan remedi
    try:
        nilai = int(input_nilai)

        nilai_masuk.append(nilai)
        if nilai >= batas_nilai[0]: 
            lulus.append(nilai)
            print(f"Nilai {nilai} -> LULUS\n")
        else:
            remedi.append(nilai)
            print(f"Nilai {nilai} -> REMEDI\n")
    except ValueError:
            print("Input tidak valid! Masukkan angka, 'hapus', atau 'selesai'.\n")

# tampilkan hasil akhir
print("\n= Hasil Akhir Input Nilai Mahasiswa =")
print("Nilai yang dimasukkan:", nilai_masuk)
print("Nilai lulus:", lulus)
print("Nilai remedi:", remedi)