import shutil
import os
import zipfile
import pytest


@pytest.fixture
def test_add_in_zip_file():
        os.chdir('resources')
        with zipfile.ZipFile('arhiv.zip', 'w') as zipf:
            zipf.write('print.txt')
            zipf.write('exceltest.xlsx')
            zipf.write('foto.jpg')
            zipf.write('color_map.pdf')

        if not os.path.isdir('../tmp'):
            os.mkdir('../tmp')
        shutil.move('arhiv.zip', os.path.join('../tmp', 'arhiv.zip'))
        yield