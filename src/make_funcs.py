import glob
import sys
import os
import subprocess

dir = sys.argv[1]
dir_file = os.path.join(dir, '*')

for file_ in glob.glob(dir_file):
    if os.path.isfile(file_) and file_.find('test') == -1:
        print 'void Send%s(){' % (file_, )
        command = "./ir_code_average.py %s" % (file_, )
        os.system(command)
        print '};'
