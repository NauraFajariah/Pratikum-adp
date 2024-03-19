print("Selamat datang di pemesanan tiket Bus PT ANS Lintas-Sumatera")
print("Tujuan yang dipilih:")
print("1. Medan: Rp70000")
print("2. Padang: Rp50000")
print("3. Jambi: Rp30000")
print("4. Pekanbaru: Rp40000")
print("5. Bengkulu: Rp60000")
print("6. Palembang: Rp80000")
tujuan = int(input("Pilih (1-6): "))

if tujuan == 1:
    harga = 70000
    ntujuan = "Medan"
elif tujuan == 2:
    harga = 50000
    ntujuan = "Padang"
elif tujuan == 3:
    harga = 30000
    ntujuan = "Jambi"
elif tujuan == 4:
    harga = 40000
    ntujuan = "Pekanbaru"
elif tujuan == 5:
    harga = 60000
    ntujuan = "Bengkulu"
elif tujuan == 6:
    harga = 80000
    ntujuan = "Palembang"
else:
    print("Error")
    exit()

print("---------------------------------------------------------------------------------------------------------------")

print("Kelas yang dipilih:")
print("1. Ekonomi Class: Rp10000")
print("2. Bisnis Class: Rp20000")
print("3. First Class: Rp30000")
kelas = int(input("Pilih (1-3): "))

if kelas == 1:
    hkelas = 10000
    nclass = "Ekonomi Class"
elif kelas == 2:
    hkelas = 20000
    nclass = "Bisnis Class"
elif kelas == 3:
    hkelas = 30000
    nclass = "First Class"
else:
    print("Error")
    exit()

print("---------------------------------------------------------------------------------------------------------------")

tiket = int(input("Jumlah Tiket: "))

print("---------------------------------------------------------------------------------------------------------------")

if tiket >= 3 and tiket <= 5:
    hargad = tiket * (harga + hkelas) * 95 / 100
    ndiskon = "5%"
elif tiket > 5:
    hargad = tiket * (harga + hkelas) * 90 / 100
    ndiskon = "10%"
else:
    hargad = tiket * (harga + hkelas)
    ndiskon = "0%"

print("Tujuan               :", ntujuan)
print("Kelas                :", nclass)
print("Jumlah Tiket         :", tiket)
print("Total                : Rp", tiket * (harga + hkelas))
print("Diskon               :", ndiskon)
print("Total Setelah Diskon : Rp", hargad)