# This script show how getting error when work parallel process share common memory

import time
import multiprocessing
import sys
from pycsp.parallel import *


shareData=100

@process
def padd():
    global shareData
    var =shareData
    time.sleep(1.5)
    var+=1              # add plus one to 'shareData'
    shareData=var

@process
def madd():
    global shareData
    var =shareData
    var-=1             #  plus minus one to 'shareData'
    shareData=var

    
   


Parallel(padd() ,madd())



shutdown()

print(shareData)


 




 

