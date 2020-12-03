from multiprocessing import Pool
from functools import partial


def add(x):
    for i in range(20000):
        x+=1
    return x


if __name__ == "__main__":
    pool = Pool(4) # 池的大小为4
    origin = [_ for _ in range(2520)]
    b=pool.map(add, origin)
    #close the pool and wait for the worker to exit
    print (b)
    pool.close()
    pool.join()