import pytest
from unittest.mock import patch
from SystemManajemenMahasiswa import input_nilai, cek_nilai, simpan_nilai, hapus_edit_nilai

@pytest.fixture
def sample_data():
    """Sample data for testing."""
    return [
        {'Nama': 'Alice', 'NIM': '123', 'Semester': 1, 'Mata Kuliah': 'Math', 'Nilai': 85.0},
        {'Nama': 'Bob', 'NIM': '124', 'Semester': 2, 'Mata Kuliah': 'Physics', 'Nilai': 90.0}
    ]

def test_input_nilai(sample_data):
    """Test input_nilai function."""
    mock_inputs = ['Charlie', '125', 3, 'Chemistry', 78.5]
    with patch('builtins.input', side_effect=mock_inputs):
        result = input_nilai()
        assert result == {'Nama': 'Charlie', 'NIM': '125', 'Semester': 3, 'Mata Kuliah': 'Chemistry', 'Nilai': 78.5}

def test_cek_nilai(capsys, sample_data):
    """Test cek_nilai function."""
    cek_nilai(sample_data)
    captured = capsys.readouterr()
    assert 'Alice' in captured.out
    assert 'Bob' in captured.out
    assert 'Math' in captured.out
    assert 'Physics' in captured.out

def test_simpan_nilai(tmpdir, sample_data):
    """Test simpan_nilai function."""
    # Simpan file ke directory sementara
    test_file = tmpdir.join("data_mahasiswa.xlsx")
    with patch('SystemManajemenMahasiswa.pd.DataFrame.to_excel') as mock_to_excel:
        simpan_nilai(sample_data)
        mock_to_excel.assert_called_once()
        args, kwargs = mock_to_excel.call_args
        assert 'data_mahasiswa.xlsx' in args

def test_hapus_edit_nilai(sample_data):
    """Test hapus_edit_nilai function."""
    # Test hapus data
    mock_inputs = ['123', 2]  # Pilih NIM '123' dan opsi Hapus
    with patch('builtins.input', side_effect=mock_inputs):
        hapus_edit_nilai(sample_data)
        assert len(sample_data) == 1  # Data berkurang
        assert all(d['NIM'] != '123' for d in sample_data)

    # Test edit data
    mock_inputs = ['124', 1, 'Robert', 3, 'Biology', 95.0]  # Edit NIM '124'
    with patch('builtins.input', side_effect=mock_inputs):
        hapus_edit_nilai(sample_data)
        assert sample_data[0]['Nama'] == 'Robert'
        assert sample_data[0]['Semester'] == 3
        assert sample_data[0]['Mata Kuliah'] == 'Biology'
        assert sample_data[0]['Nilai'] == 95.0
