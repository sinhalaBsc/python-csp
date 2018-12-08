
#  sudo python3.6 -m pip install pycsp
#import pycsp.parallel as pycsp
import time
import multiprocessing
import sys
from pycsp.parallel import *
#from pycsp import *

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

c= Channel() # channel_var= Channel('channel_name')

Parallel(send(c,200),recv(c))

shutdown()



