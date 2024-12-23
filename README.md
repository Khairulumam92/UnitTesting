# Program Unit Test
# Sistem Manajemen Pesanan Restoran

Program ini adalah aplikasi berbasis terminal untuk mengelola pesanan di restoran. Aplikasi ini memungkinkan pengguna untuk membuat, melihat, mengubah, menghapus, dan mencari pesanan. Data pesanan disimpan dalam file teks (`pesanan.txt`) dan dapat diekspor ke file dokumen Word (`pesanan.docx`).

## Fitur Utama
1. **Buat Pesanan**: Menambahkan pesanan baru, termasuk makanan, minuman, dan gambar terkait.
2. **Tampilkan Semua Pesanan**: Melihat daftar semua pesanan yang sudah dibuat.
3. **Ubah Status Pesanan**: Mengubah status pesanan menjadi `diproses`, `selesai`, atau `batal`.
4. **Hapus Pesanan**: Menghapus pesanan dengan status `batal`.
5. **Cari Pesanan**: Mencari pesanan berdasarkan nama pelanggan.
6. **Ekspor Pesanan ke Word**: Semua pesanan secara otomatis disimpan ke file Word (`pesanan.docx`).

## Prasyarat
- Python 3.x
- Modul Python: `python-docx`
  - Instalasi: `pip install python-docx`

## Cara Menjalankan Program
1. **Kloning atau Unduh Repository**: 
   Pastikan Anda memiliki file `pesanan.txt` (jika tidak, program akan membuatnya secara otomatis).
2. **Jalankan Program**:
   ```bash
   python nama_file_program.py
   ```
3. **Ikuti Menu di Terminal**:
   Pilih opsi yang tersedia dari menu utama.

## Struktur Data Pesanan
Setiap pesanan memiliki atribut:
- `name`: Nama pelanggan.
- `items`: Daftar makanan/minuman yang dipesan (dengan nama dan path gambar).
- `status`: Status pesanan (`diproses`, `selesai`, atau `batal`).

Contoh:
```json
{
    "name": "John Doe",
    "items": [
        {"name": "Ayam Krispi", "image": "path/to/image1.jpg"},
        {"name": "Es Teh", "image": "path/to/image2.jpg"}
    ],
    "status": "diproses"
}
```

## Menu Utama
1. **Buat Pesanan**: Masukkan nama pelanggan, pilih makanan/minuman, dan tambahkan path gambar.
2. **Tampilkan Semua Pesanan**: Menampilkan semua pesanan yang ada di file.
3. **Ubah Status Pesanan**: Pilih nomor pesanan dan ubah statusnya.
4. **Hapus Pesanan**: Hanya pesanan dengan status `batal` yang dapat dihapus.
5. **Cari Pesanan**: Masukkan nama pelanggan untuk mencari pesanan.
6. **Keluar**: Menutup program.

## Ekspor ke File Word
Setiap perubahan pesanan akan otomatis diperbarui di file `pesanan.docx`, yang berisi:
- Nama pelanggan.
- Daftar makanan/minuman.
- Path gambar (jika ditemukan).
- Status pesanan.

## Catatan
- Gambar harus ada di path yang valid untuk ditampilkan di file Word.
- File `pesanan.txt` digunakan untuk menyimpan data pesanan dalam format teks sederhana.
- Pastikan memiliki izin baca/tulis di direktori tempat file berada.

## Pengembang
- Dibuat oleh: Moh. Khairul Umam
- Versi: 1.0
- Bahasa: Python

## Lisensi
Proyek ini dilisensikan di bawah khairulmamku92@gmail.com . Anda bebas menggunakan dan memodifikasi program ini.