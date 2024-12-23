import unittest
import logging
from datetime import datetime
from io import StringIO
from unittest.mock import patch
import pandas as pd

# Konfigurasi logging dengan timestamps
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Import fungsi dari program utama (pastikan nama modul sesuai)
from SystemManajemenMahasiswa import input_nilai, cek_nilai, simpan_nilai, hapus_edit_nilai

class TestSystemManajemenMahasiswa(unittest.TestCase):
    def setUp(self):
        # Logging saat memulai test case
        logging.info(f"Starting test case at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.data = [
            {'Nama': 'Alice', 'NIM': '001', 'Semester': 3, 'Mata Kuliah': 'Math', 'Nilai': 85.0},
            {'Nama': 'Bob', 'NIM': '002', 'Semester': 2, 'Mata Kuliah': 'Science', 'Nilai': 90.0}
        ]

    def test_cek_nilai(self):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            cek_nilai(self.data)
            output = fake_out.getvalue()
        logging.info(f"Output of cek_nilai: {output}")
        self.assertIn('Alice', output)
        self.assertIn('Bob', output)

    def test_simpan_nilai(self):
        simpan_nilai(self.data)
        df = pd.read_excel('data_mahasiswa.xlsx')
        logging.info(f"Data saved to Excel: {df.to_dict('records')}")
        self.assertEqual(len(df), len(self.data))

    def test_hapus_edit_nilai(self):
        with patch('builtins.input', side_effect=['002', '2']):
            hapus_edit_nilai(self.data)
        logging.info(f"Data after deletion: {self.data}")
        self.assertEqual(len(self.data), 1)
        self.assertNotIn({'Nama': 'Bob', 'NIM': '002', 'Semester': 2, 'Mata Kuliah': 'Science', 'Nilai': 90.0}, self.data)

    def test_input_nilai(self):
        with patch('builtins.input', side_effect=['Charlie', '003', '1', 'History', '75.0']):
            result = input_nilai(self.data)  # Kirim self.data sebagai argumen
            logging.info(f"New entry from input_nilai: {result}")
            self.assertEqual(result, {'Nama': 'Charlie', 'NIM': '003', 'Semester': 1, 'Mata Kuliah': 'History', 'Nilai': 75.0})




    def tearDown(self):
        # Logging saat test case selesai
        logging.info(f"Ending test case at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

if __name__ == '__main__':
    unittest.main()
