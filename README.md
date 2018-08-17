# Performance boost using cython

The aim of this code is to compare performance of pure python implementation with that of cython.

I have implemented a simple function that uses a large loop using three methods

Pure python

Basic cython

Cython with cdef types

The basic cython implementation provides a time boost of about 50%.

However when you introduce cdef type in the cython code, the performance increases significantly by several hundred times for this simple.

Behold the power of C! 
