#!/usr/bin/python

import time

def reg_func():
    for i in range(100000000):
        i = i+1
    print i

def main():
    start_time = time.time()
    func()
    print ("Total time")
    print (time.time() - start_time)

if __name__=="__main__":
    main()
