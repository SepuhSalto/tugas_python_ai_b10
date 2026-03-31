# ==========================================
# FUNCTIONS
# ==========================================

def greet(nama: str) -> str:
    """Mengembalikan teks sapaan sederhana."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan dua angka. Angka kedua opsional."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """Menghitung rata-rata dari list angka. Mengembalikan 0.0 jika list kosong."""
    if not angka: # Logika pertahanan jika list tidak memiliki elemen
        return 0.0
    
    total = sum(angka)
    banyak_angka = len(angka)
    # round(..., 2) membulatkan hasil menjadi 2 angka di belakang koma
    return round(total / banyak_angka, 2)

# ==========================================
# CLASS STUDENT
# ==========================================

class Student:
    """Blueprint untuk entitas mahasiswa."""
    
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = [] # Diinisialisasi sebagai list kosong
        
    def tambah_nilai(self, skor: float):
        """Menambahkan satu nilai ke dalam list memori mahasiswa."""
        self.nilai.append(skor)
        
    def rata_nilai(self) -> float:
        """Menghitung rata-rata nilai menggunakan fungsi global rata_rata()."""
        return rata_rata(self.nilai)
        
    def status(self, threshold: float = 70.0) -> str:
        """Mengevaluasi apakah mahasiswa lulus berdasarkan ambang batas nilai."""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"
            
    def __str__(self) -> str:
        """Representasi string dari objek agar mudah dibaca oleh sistem/manusia."""
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

# ==========================================
# DEMO EKSEKUSI
# ==========================================

if __name__ == "__main__":
    # --- Demo Functions ---
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    
    print(f"Hasil tambah(5, 7) = {tambah(5, 7)}")
    print(f"Hasil tambah(10) = {tambah(10)}") # Akan memakai nilai default b = 0.0
    
    print(f"Hasil rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"Hasil rata_rata([]) = {rata_rata([])}")
    print()

    # --- Demo Class ---
    print("=== CLASS STUDENT ===")
    
    # Inisialisasi Objek Mahasiswa 1
    mhs1 = Student("Mirza", "2400112233")
    mhs1.tambah_nilai(85.5)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(88.0)
    
    print("Data Mahasiswa 1:")
    print(mhs1) # Ini akan secara otomatis memicu method __str__
    print(f"Rata-rata spesifik: {mhs1.rata_nilai()}")
    print(f"Status kelulusan: {mhs1.status()}")
    print()
    
    # Inisialisasi Objek Mahasiswa 2 (Skenario tidak lulus)
    mhs2 = Student("Budi", "A123")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.5)
    mhs2.tambah_nilai(70.0)
    
    print("Data Mahasiswa 2:")
    print(mhs2)
    print(f"Rata-rata spesifik: {mhs2.rata_nilai()}")
    print(f"Status kelulusan: {mhs2.status()}")