import unittest
import app.load_file_helper as hlp


class TestLoadFileHelper(unittest.TestCase):

    def test_argument_correct(self):
        pass


    def test_wrong_file_path(self):
        file_path = "wrong/path"
        self.assertEqual(('Error Unable to read file:', file_path),  hlp.get_header_row(file_path))

# data/oscar_age_male.csv
