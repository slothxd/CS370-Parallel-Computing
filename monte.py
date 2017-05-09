import random
import time
from mpi4py import MPI

def monte_carlo_pi(nsize):

        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        size = comm.Get_size()
        begin = time.time()

        counter = 0.0

        for k in range(nsize):
                x = random.random()
                y = random.random()
                if (((x * x) + (y * y)) < 1.0):
                        counter = counter + 1

        print("Time: ", time.time() - begin)
        mypi = (float) (counter / nsize)

        myreduce = comm.reduce(mypi, MPI.SUM)

        pi = 4.0 / size

        if myreduce is None:
                return 3.14

        pi = pi * myreduce
        return pi

if __name__ == "__main__":
        # Change this to increase Processes
        pi = monte_carlo_pi(1000000)
        comm = MPI.COMM_WORLD
        if comm.Get_rank() == 0:
                print ("Value of pi from ", comm.Get_size(), " processors outputs a value of ", pi)
