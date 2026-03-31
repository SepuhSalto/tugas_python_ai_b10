import numpy as np
import pandas as pd
import os

# Set seed agar hasil acak selalu konsisten setiap kali program dijalankan
np.random.seed(42)

# ==========================================
# OOP: CLASS GRADEBOOK
# ==========================================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def average(self) -> float:
        """Menghitung rata-rata dari kolom nilai."""
        return round(self.df["nilai"].mean(), 2)
        
    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase mahasiswa yang lulus."""
        total_siswa = len(self.df)
        if total_siswa == 0:
            return 0.0
        jumlah_lulus = len(self.df[self.df["nilai"] >= threshold])
        persentase = (jumlah_lulus / total_siswa) * 100
        return round(persentase, 2)
        
    def save_summary(self, path: str):
        """Menulis ringkasan dataframe ke dalam file .txt."""
        jumlah_baris = len(self.df)
        jumlah_lulus = len(self.df[self.df["status"] == "LULUS"])
        jumlah_gagal = jumlah_baris - jumlah_lulus
        
        # Mode "a" (append) agar tidak menimpa ringkasan NumPy yang sudah ditulis sebelumnya
        with open(path, "a") as file:
            file.write("\n=== RINGKASAN DATAFRAME (GRADEBOOK) ===\n")
            file.write(f"Total Mahasiswa : {jumlah_baris}\n")
            file.write(f"Rata-rata Kelas : {self.average()}\n")
            file.write(f"Jumlah Lulus    : {jumlah_lulus}\n")
            file.write(f"Jumlah Gagal    : {jumlah_gagal}\n")
            file.write(f"Tingkat Kelulusan: {self.pass_rate()}%\n")
            
    def __str__(self) -> str:
        return f"GradeBook(Total Data: {len(self.df)}, Rata-rata: {self.average()})"

# ==========================================
# DEMO EKSEKUSI UTAMA
# ==========================================
if __name__ == "__main__":
    # Tentukan nama file output
    file_output = "ringkasan_tugas6.txt"
    
    # --- 1. NUMPY ---
    print("=== NUMPY ===")
    # Membuat 10 data nilai ujian acak dari rentang 50 sampai 100
    nilai_ujian = np.random.randint(50, 101, size=10)
    print("Array Nilai:", nilai_ujian)
    
    # Kalkulasi statistik dasar menggunakan NumPy
    rata_rata_np = np.mean(nilai_ujian)
    median_np = np.median(nilai_ujian)
    std_np = np.std(nilai_ujian)
    min_np = np.min(nilai_ujian)
    max_np = np.max(nilai_ujian)
    
    print(f"Rata-rata : {rata_rata_np}")
    print(f"Median    : {median_np}")
    print(f"Std Dev   : {round(std_np, 2)}")
    print(f"Min - Max : {min_np} - {max_np}\n")
    
    # Menulis hasil NumPy ke file .txt (mode "w" untuk menimpa file baru)
    with open(file_output, "w") as file:
        file.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        file.write(f"Rata-rata : {rata_rata_np}\n")
        file.write(f"Median    : {median_np}\n")
        file.write(f"Std Dev   : {round(std_np, 2)}\n")
        file.write(f"Min - Max : {min_np} - {max_np}\n")

    # --- 2. PANDAS ---
    print("=== PANDAS ===")
    # Membuat DataFrame untuk 5 mahasiswa. Nilai diambil dari sebagian array NumPy tadi.
    data = {
        "nama": ["Mirza", "Budi", "Siti", "Agus", "Dewi"],
        "nim": ["24001", "24002", "24003", "24004", "24005"],
        "nilai": nilai_ujian[:5] # Mengambil 5 nilai pertama dari array NumPy
    }
    df = pd.DataFrame(data)
    
    # Menambahkan kolom status dengan logika list comprehension (sederhana & efisien)
    df["status"] = ["LULUS" if n >= 70 else "TIDAK LULUS" for n in df["nilai"]]
    
    print("Menampilkan 5 baris pertama:")
    print(df.head())
    print()
    
    # --- 3. OOP: GRADEBOOK ---
    print("=== OOP: GRADEBOOK ===")
    # Menginisialisasi objek GradeBook dengan DataFrame yang baru saja dibuat
    kelas_ai = GradeBook(df)
    
    print(kelas_ai) # Menguji method __str__
    print(f"Rata-rata Kelas : {kelas_ai.average()}")
    print(f"Persentase Lulus: {kelas_ai.pass_rate()}%\n")
    
    # Menyimpan ringkasan ke file teks
    kelas_ai.save_summary(file_output)
    print(f">> Semua ringkasan telah diekspor secara otomatis ke '{file_output}'.")