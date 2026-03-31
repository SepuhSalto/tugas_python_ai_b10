# --- 1. Deklarasi Variabel dan Tipe Data ---
nama = "Mirza"             # string
umur = 20                  # integer
berat_badan = 90.5         # float
status_mahasiswa = True    # boolean
hobi = ["gym", "game", "fotografi", "nonton", "koding"] # list

# --- 2. Manipulasi String ---
print("=== Manipulasi String ===")
# Menggabungkan teks
teks_perkenalan = "Halo, " + nama + " ada di sini."
print(teks_perkenalan)

# Menghitung panjang huruf
print("Jumlah huruf pada nama:", len(nama))

# Mengubah ukuran huruf
print("Huruf besar semua:", nama.upper())
print("Huruf kecil semua:", nama.lower())
print()

# --- 3. Operasi Matematika Sederhana ---
print("=== Operasi Matematika ===")
angka1 = 15
angka2 = 4

print("Hasil tambah (+):", angka1 + angka2)
print("Hasil kurang (-):", angka1 - angka2)
print("Hasil kali (*):", angka1 * angka2)
print("Hasil bagi (/):", angka1 / angka2)
print("Bagi bulat (//):", angka1 // angka2) 
print("Sisa bagi (%):", angka1 % angka2) 
print()

# --- 4. List dan Akses Elemen ---
print("=== Operasi List ===")
buah = ["apel", "jeruk", "mangga", "pisang", "melon"]
print("Daftar buah awal:", buah)

# Mengambil elemen tertentu (ingat, hitungan dimulai dari 0)
print("Buah urutan ketiga (index 2):", buah[2])

# Menambahkan item baru
buah.append("semangka")
print("Setelah ditambah:", buah)

# Menghapus item
buah.remove("jeruk")
print("Setelah dihapus:", buah)
print()

# --- 5. Penggunaan Input dari User ---
print("=== Input User ===")
nama_input = input("Masukkan nama Anda: ")
umur_input = input("Masukkan umur Anda: ")

print(f"Halo, nama saya {nama_input} dan umur saya {umur_input} tahun.")