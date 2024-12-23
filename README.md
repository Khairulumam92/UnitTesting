# Program Unit Test
# Database Nilai Mahasiswa

## Deskripsi Program
Program ini dirancang untuk mengelola **database nilai mahasiswa** menggunakan Python dan library **pandas**. Data mahasiswa seperti nama, NIM, semester, mata kuliah, dan nilai dapat ditambahkan, ditampilkan, diedit, atau dihapus. Selain itu, data dapat disimpan ke dalam file Excel (`data_mahasiswa.xlsx`) untuk keperluan penyimpanan.



## Fitur Program
1. **Input Nilai Mahasiswa**  
   Tambahkan data mahasiswa baru ke dalam sistem, termasuk validasi untuk menghindari duplikasi NIM.

2. **Tampilkan Data**  
   Menampilkan seluruh data mahasiswa yang telah dimasukkan.

3. **Simpan Data**  
   Menyimpan data mahasiswa ke dalam file Excel (`data_mahasiswa.xlsx`).

4. **Hapus atau Edit Data**  
   Menghapus atau mengedit data mahasiswa berdasarkan NIM.

5. **Keluar dari Program**  
   Mengakhiri eksekusi program dengan aman.

---

## Prasyarat
- Python 3.x.x
- Library **pandas**
- Library **openpyxl** (untuk menyimpan file Excel)

---

## Instalasi
1. Pastikan Python 3.x telah terinstal di komputer Anda.
2. Install library **pandas** dan **openpyxl** dengan perintah berikut:
   ```bash
   pip install pandas openpyxl
   ```

---

## Cara Menggunakan
1. Jalankan program dengan perintah:
   ```bash
   python SystemManajemenMahasiswa.py
   ```
2. Ikuti menu yang tersedia:
   - Pilih `1` untuk menambahkan data mahasiswa.
   - Pilih `2` untuk menampilkan data mahasiswa.
   - Pilih `3` untuk menyimpan data ke file Excel.
   - Pilih `4` untuk mengedit atau menghapus data berdasarkan NIM.
   - Pilih `5` untuk keluar dari program.

---

## Format Input
- **Nama**: String (contoh: "John Doe").
- **NIM**: String (contoh: "12345678").
- **Semester**: Integer (contoh: `2`).
- **Mata Kuliah**: String (contoh: "Matematika Dasar").
- **Nilai**: Float (contoh: `85.5`).

---

## File Output
Data yang disimpan akan ditulis ke file **data_mahasiswa.xlsx** dengan kolom:
- Nama
- NIM
- Semester
- Mata Kuliah
- Nilai

---

## Contoh Penggunaan
1. Tambahkan data mahasiswa:
   ```
   Masukkan Nama: John Doe
   Masukkan NIM: 12345678
   Masukkan Semester: 1
   Masukkan Mata Kuliah: Matematika Dasar
   Masukkan Nilai: 90.5
   ```
2. Tampilkan data mahasiswa:
   ```
   NIM: 12345678, Nama: John Doe, Semester: 1, Mata Kuliah: Matematika Dasar, Nilai: 90.5
   ```
3. Simpan data ke file Excel:
   ```
   Data telah disimpan ke dalam file data_mahasiswa.xlsx
   ```

---

## Catatan
- Jika file `data_mahasiswa.xlsx` tidak ditemukan saat program dijalankan, program akan membuat data kosong secara otomatis.
- Pastikan NIM tidak duplikat untuk menghindari konflik data.
- Masukkan nilai yang valid (misalnya, nilai berupa angka).

---

## Lisensi
Program ini dilisensikan di bawah lisensi **MIT License**. Silakan gunakan dan modifikasi sesuai kebutuhan.

--- 

**Dibuat oleh:** Moh. Khairul Umam  
**Kontak:** khairulumamku92@gmail.com