#!/usr/bin/python

import pyximport; pyximport.install()
import time

cpdef func_type():
    cdef int x = 0
    for i in range(100000000):
        x = x+1
    print x

def main():
    start_time = time.time()
    func_type()
    print ("Total time")
    print (time.time() - start_time)

if __name__=="__main__":
    main()
