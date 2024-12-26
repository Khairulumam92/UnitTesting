import unittest
from unittest.mock import patch
import sys
sys.path.append('/d:/Kuliah/3. Semester 3/Proglan/Teori/Tugas/UnitTesting/Test Case')
from SystemManajemenMahasiswa import input_nilai, cek_nilai, simpan_nilai, hapus_edit_nilai

class TestSystemManajemenMahasiswa(unittest.TestCase):

    @patch('builtins.input', side_effect=['John Doe', '12345', '1', 'Math', '90'])
    def test_input_nilai(self, mock_input):
        data = []
        result = input_nilai(data)
        expected = {'Nama': 'John Doe', 'NIM': '12345', 'Semester': 1, 'Mata Kuliah': 'Math', 'Nilai': 90.0}
        self.assertEqual(result, expected)

    @patch('builtins.print')
    def test_cek_nilai(self, mock_print):
        data = [{'Nama': 'John Doe', 'NIM': '12345', 'Semester': 1, 'Mata Kuliah': 'Math', 'Nilai': 90.0}]
        cek_nilai(data)
        mock_print.assert_called_with("NIM: 12345, Nama: John Doe, Semester: 1, Mata Kuliah: Math, Nilai: 90.0")

    @patch('pandas.DataFrame.to_excel')
    @patch('builtins.print')
    def test_simpan_nilai(self, mock_print, mock_to_excel):
        data = [{'Nama': 'John Doe', 'NIM': '12345', 'Semester': 1, 'Mata Kuliah': 'Math', 'Nilai': 90.0}]
        simpan_nilai(data)
        mock_to_excel.assert_called_once_with('data_mahasiswa.xlsx', index=False)
        mock_print.assert_called_once_with("Data telah disimpan ke dalam file data_mahasiswa.xlsx")

    @patch('builtins.input', side_effect=['12345', '1', 'John Smith', '2', 'Physics', '85'])
    @patch('builtins.print')
    def test_hapus_edit_nilai_edit(self, mock_print, mock_input):
        data = [{'Nama': 'John Doe', 'NIM': '12345', 'Semester': 1, 'Mata Kuliah': 'Math', 'Nilai': 90.0}]
        hapus_edit_nilai(data)
        expected = {'Nama': 'John Smith', 'NIM': '12345', 'Semester': 2, 'Mata Kuliah': 'Physics', 'Nilai': 85.0}
        self.assertEqual(data[0], expected)
        mock_print.assert_any_call("Data berhasil diedit.")

    @patch('builtins.input', side_effect=['12345', '2'])
    @patch('builtins.print')
    def test_hapus_edit_nilai_hapus(self, mock_print, mock_input):
        data = [{'Nama': 'John Doe', 'NIM': '12345', 'Semester': 1, 'Mata Kuliah': 'Math', 'Nilai': 90.0}]
        hapus_edit_nilai(data)
        self.assertEqual(data, [])
        mock_print.assert_any_call("Data berhasil dihapus.")

if __name__ == '__main__':
    unittest.main()
