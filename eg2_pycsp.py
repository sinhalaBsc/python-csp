# put reader() and writer() functions inside method

import time
import multiprocessing
import sys
from pycsp.parallel import *


@process
def send(cout, idata): 
    wrt=cout.writer()
    wrt(idata)

@process
def recv(cin):
    rdr=cin.reader()
    time.sleep(1)
    msg=rdr()
    print('Got: ',msg)

c= Channel()                   # define channel

Parallel(send(c,200),recv(c))  # execute the parallel process

shutdown()



