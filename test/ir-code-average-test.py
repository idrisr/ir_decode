from unittest import TestCase
from ir_code_average import get_args
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
