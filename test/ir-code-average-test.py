from unittest import TestCase
from ir_code_average import get_args
from ir_code_average import read_data_file
import os

class test_IR_data_parser(TestCase):
    def test_get_args(self):
        dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data/test'
        files = [ 'test2', 'test3', 'test4']
        dir_files = [os.path.join(dir, file_) for file_ in files]
        exp = dir_files
        rec = get_args(dir_files)
        self.assertItemsEqual(exp, rec)

        files = ['test1', 'test2', 'test3', 'test4']
        dir_files = [os.path.join(dir, file_) for file_ in files]
        dir_files.pop(0)
        rec = get_args(dir_files)
        exp = dir_files
        self.assertItemsEqual(exp, rec)


    def test_read_data_file(self):
        dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data/test'
        file_ = 'test2'
        dir_file = os.path.join(dir, file_)

        rec = read_data_file(dir_file)
        exp = [[1, 1], [2, 2], [3, 3]]
        self.assertItemsEqual(exp, rec.values.tolist())
