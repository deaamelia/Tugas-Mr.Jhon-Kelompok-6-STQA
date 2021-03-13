#fungsi hitung gaji per minggu
def hitung_gaji(hours):
    if hours > 40:
        per_week = (40 * 15000) + ((hours - 40) * 22500)
    elif hours < 0: 
        print("Jam kerja harus lebih dari 0")
        per_week = 0
    else: 
        per_week = hours * 15000
    return per_week

#fungsi pengeluaran dan jumlah tabungan 
def Pengeluaran(pengeluaran, per_week):
    if pengeluaran < 0:
        tabungan = per_week
        print("Pengeluaran harus lebih dari 0!")
    elif pengeluaran < per_week and per_week > pengeluaran:
        tabungan = per_week - pengeluaran
        print("Bisa menabung!!")
    elif pengeluaran == per_week:
        tabungan = 0
        print("Tidak bisa menabung!!")
    else:
        tabungan = 0
        print("Cari tambahan!")
    return tabungan

print("---------- PROGRAM HITUNG GAJI KARYAWAN PER MINGGU ----------")
count = "y"
while(count.lower() == "y"):
    #INPUT
    nama = input("Masukkan nama karyawan: ")
    if nama == "":
        nama = "No Name"
    jam_kerja = int(input("Jumlah jam kerja per minggu: "))
    total_gaji = hitung_gaji(jam_kerja)
    total_pengeluaran = int(input("Masukkan total pengeluaran: "))
    pengeluaran_perminggu = Pengeluaran(total_pengeluaran, total_gaji)
    print()

    #OUTPUT
    print("Nama karyawan: ", nama)
    print("Total gaji minggu ini: Rp", total_gaji)
    print("Total pengeluaran minggu ini: Rp", total_pengeluaran)
    print("Total tabungan minggu ini: Rp", pengeluaran_perminggu)
    count = input("Lakukan perhitungan kembali? (tekan y untuk lanjut)")
    print()

print("Good Bye!!")










