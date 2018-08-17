#!/usr/bin/python

import sys
import os
sys.path.append(os.getcwd())
import pyximport; pyximport.install()
import reg_python
import cython_basic
import cython_types
import time

def main():
    start_time = time.time()
    reg_python.reg_func()
    print ("Time for regular python")
    print (time.time() - start_time)

    start_time = time.time()
    cython_basic.func()
    print ("Time for cython")
    print (time.time() - start_time)

    start_time = time.time()
    cython_types.func_type()
    print ("Time for cython types")
    print (time.time() - start_time)

if __name__=="__main__":
    main()
