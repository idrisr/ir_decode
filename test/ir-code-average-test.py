from unittest import TestCase
from ir_code_average import get_file_arg
from ir_code_average import average_ir_signal
from ir_code_average import split_data_file
from ir_code_average import str_list_to_int
from ir_code_average import str_to_int
import os

class test_IR_data_parser(TestCase):
    def test_get_file_arg(self):
        dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data'
        file_ = 'test2'
        dir_file = os.path.join(dir, file_)
        exp = dir_file
        rec = get_file_arg(dir_file)
        self.assertItemsEqual(exp, rec)

        dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data'
        file_ = 'file_does_not_exist'
        dir_file = os.path.join(dir, file_)

        with self.assertRaises(SystemExit) as cm:
            get_file_arg(dir_file)

        self.assertEqual(cm.exception.code, 1)


    def test_split_data_file(self):
        dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data'
        file_ = 'test2'
        dir_file = os.path.join(dir, file_)
        exp = [['-1, 1', 
                '1, 2',
                '2, 3',
                '3, 5000'],
                ['4, 4',
                '5, 5',
                '6, 6']]

        rec = split_data_file(dir_file)
        self.assertItemsEqual(exp, rec)


    def test_str_list_to_int(self):
        input_ = ['-1, 1', 
                '1, 2',
                '2, 3',
                '3, 5000']

        exp = [[-1, 1], 
               [1, 2],
               [2, 3],
               [3, 5000]]

        rec = str_list_to_int(input_)
        self.assertItemsEqual(exp, rec)


    def test_str_to_int(self):
        input_ = '-1, 1'
        exp = [-1, 1]
        rec = str_to_int(input_)
        self.assertItemsEqual(exp, rec)

        input_ = '-1,        1         '
        exp = [-1, 1]
        rec = str_to_int(input_)
        self.assertItemsEqual(exp, rec)


    #def test_read_data_file(self):
        #dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data/test'
        #file_ = 'test2'
        #dir_file = os.path.join(dir, file_)

        #rec = read_data_file(dir_file)
        #exp = [[1, 1], [2, 2], [3, 3]]
        #self.assertItemsEqual(exp, rec.values.tolist())


    #def test_average_ir_signal(self):
        #dir = '/Users/idris/projects/Arduino/ir_lamp/rawirdecode/data/test'
        #files = [ 'test2', 'test3', 'test4']
        #dir_files = [os.path.join(dir, file_) for file_ in files]
        #dfs = read_data_files(dir_files)

        #exp = [[2, 2], [3, 3], [4, 4]]
        #rec = average_ir_signal(dfs)
        #self.assertItemsEqual(exp, rec.values.tolist())

        #files = [ 'test3', 'test4']
        #dir_files = [os.path.join(dir, file_) for file_ in files]
        #dfs = read_data_files(dir_files)

        #exp = [[2.5, 2.5], [3.5, 3.5], [4.5, 4.5]]
        #rec = average_ir_signal(dfs)
        #self.assertItemsEqual(exp, rec.values.tolist())
