import time
import numpy as np
import matplotlib.pyplot as plt
consum_time=np.array([0, 0, 0, 0, 0, 0,0, 0, 0],dtype=np.float64)
loop=np.array([0, 0, 0, 0, 0, 0,0, 0, 0])


for i in range(1,9):

    pivot=10**i
    loop[i]=pivot

    sum=0

    start=time.time()

    for j in range(1,pivot): sum+=j

    consum_time[i] = time.time()-start

    #print(ar[i])

##print(consum_time)
#print(loop)
plt.plot(consum_time)
plt.show()