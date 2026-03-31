# ==========================================
# 1. List – Akses & Manipulasi
# ==========================================
print("--- 1. LIST ---")
alat_gym = ["dumbbell", 15, "barbell", 20.5, "matras", 10]

print("Elemen pertama:", alat_gym[0])
print("Elemen terakhir:", alat_gym[-1])
print("Slicing [1:5:2]:", alat_gym[1:5:2])

print("\nSebelum manipulasi:", alat_gym)
alat_gym.append("treadmill")         # Tambah di akhir
alat_gym.insert(2, "pullup_bar")     # Sisipkan di index 2
alat_gym.extend(["sabuk", "plate"])  # Gabung list baru
print("Setelah ditambah:", alat_gym)

alat_gym.pop()                       # Hapus elemen terakhir
alat_gym.remove("barbell")           # Hapus berdasarkan nama
print("Setelah dihapus:", alat_gym)
print()

# ==========================================
# 2. Tuple – Immutability & Unpacking
# ==========================================
print("--- 2. TUPLE ---")
film_nolan = ("Interstellar", "Inception", "Dunkirk", "Memento", "Tenet")

print("Panjang tuple:", len(film_nolan))
print("Akses indeks ke-2:", film_nolan[2])

# Unpacking dengan *rest
film_pertama, *film_tengah, film_terakhir = film_nolan
print("Film pertama:", film_pertama)
print("Film tengah:", film_tengah)
print("Film terakhir:", film_terakhir)
print()

# ==========================================
# 3. Set – Keunikan & Operasi Himpunan
# ==========================================
print("--- 3. SET ---")
# Menunjukkan bahwa duplikat otomatis hilang (kata "kamera" ada dua)
tas_kamera1 = {"kamera", "lensa", "tripod", "baterai", "kamera"}
tas_kamera2 = {"lensa", "filter", "sd_card", "tripod"}

print("Isi tas kamera 1 (duplikat hilang):", tas_kamera1)
print("Isi tas kamera 2:", tas_kamera2)

print("Union (|) - Gabungan semua alat:", tas_kamera1 | tas_kamera2)
print("Intersection (&) - Alat yang ada di kedua tas:", tas_kamera1 & tas_kamera2)
print("Difference (-) - Ada di tas 1 tapi tidak di tas 2:", tas_kamera1 - tas_kamera2)
print("Symmetric Difference (^) - Alat yang tidak tumpang tindih:", tas_kamera1 ^ tas_kamera2)
print()

# ==========================================
# 4. Dictionary – Key/Value Dasar
# ==========================================
print("--- 4. DICTIONARY ---")
data_mahasiswa = {
    "nama": "Mirza",
    "nim": "2400112233",
    "angkatan": 2024,
    "kota": "Gianyar"
}

# Operasi ubah, tambah, hapus
data_mahasiswa["kota"] = "Jimbaran"      # Ubah nilai
data_mahasiswa["jurusan"] = "Informatika" # Tambah key baru
del data_mahasiswa["angkatan"]           # Hapus key

print("Keys:", data_mahasiswa.keys())
print("Values:", data_mahasiswa.values())
print("Items:", data_mahasiswa.items())

print("\nIterasi Dictionary:")
for kunci, nilai in data_mahasiswa.items():
    print(f"{kunci}: {nilai}")
print()

# ==========================================
# 5. Nested Structures
# ==========================================
print("--- 5. NESTED STRUCTURES ---")
daftar_komik = [
    {"judul": "Solo Leveling", "penulis": "Chugong", "tahun": 2018},
    {"judul": "Jujutsu Kaisen", "penulis": "Gege Akutami", "tahun": 2018},
    {"judul": "Berserk", "penulis": "Kentaro Miura", "tahun": 1989},
    {"judul": "Vagabond", "penulis": "Takehiko Inoue", "tahun": 1998}
]

print("Daftar Judul:")
for komik in daftar_komik:
    print("-", komik["judul"])

# Filter tahun >= 2000 dengan list comprehension
komik_modern = [komik["judul"] for komik in daftar_komik if komik["tahun"] >= 2000]
print("Komik terbitan tahun 2000 ke atas:", komik_modern)
print()

# ==========================================
# 6. Comprehension & Utilitas
# ==========================================
print("--- 6. COMPREHENSION ---")
# List comprehension
list_genap = [angka for angka in range(1, 21) if angka % 2 == 0]
list_kuadrat = [angka**2 for angka in range(1, 21)]
print("List genap 1-20:", list_genap)
print("List kuadrat 1-20:", list_kuadrat)

# Dict comprehension
status_angka = {angka: ("genap" if angka % 2 == 0 else "ganjil") for angka in range(1, 11)}
print("Dict genap/ganjil:", status_angka)

# Set comprehension (Huruf unik lowercase, mengabaikan spasi)
kalimat = "Bintang Di Langit Malam"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf != " "}
print("Huruf unik dari kalimat:", huruf_unik)
print()

# ==========================================
# 7. Keanggotaan & Pencarian Sederhana
# ==========================================
print("--- 7. KEANGGOTAAN & PENCARIAN ---")
# Cek keanggotaan
cek_lensa = "lensa" in tas_kamera1
print("Apakah 'lensa' ada di tas kamera 1?", cek_lensa)

# Pencarian indeks
judul_dicari = "Inception"
if judul_dicari in film_nolan:
    posisi = film_nolan.index(judul_dicari)
    print(f"Film '{judul_dicari}' ditemukan pada indeks ke-{posisi}.")
else:
    print(f"Film '{judul_dicari}' tidak ditemukan.")