# this script written for following rules in 'pycsp'

'''
 * you can store(write) only one data at one time on the channel.when read that
   written data then only you can write your next data on channel.

 * If channel haven't any data to read that process will waiting until that
   channel get write data from somewhere(from other process) to read.

 * In the program, only Parallel() method's inside functions are working as multiprocess.

'''

import time
import multiprocessing
import sys
from pycsp.parallel import *


shareData=100

@process
def send(cout, idata):
    print('send 1')
    time.sleep(1)
    print('send 2')
    wrt=cout.writer()
    wrt(idata+1)
    print('send 3')
    wrt(idata)
    print('send 4')
    #wrt(idata-1)

@process
def recv(cin):
    print('recv 1')
    rdr=cin.reader()
    print('recv 2')
    msg=rdr()
    print('Got: ',msg)
    print('recv 3')
    time.sleep(2)
    msg=rdr()
    print('Got: ',msg)

l= Channel() # channel_var= Channel('channel_name')

print('start process')
Parallel(send(l,200) ,recv(l))
print('end process')


shutdown()
