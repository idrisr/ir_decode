#!/usr/bin/env python

import glob
import sys
import os
from subprocess import Popen, PIPE, STDOUT
import subprocess

dir = sys.argv[1]
dir_file = os.path.join(dir, '*')

for file_ in glob.glob(dir_file):
    if os.path.isfile(file_) and file_.find('test') == -1:
        filename = file_.split('/')[-1]
        print 'void Send%s(){' % (filename, )

        command = "./ir_code_average.py %s" % (file_, )
        p = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
        stdout, stderr = p.communicate()
        print stdout
        print '};'
