#!/usr/bin/python

from multiprocessing import Process, Value, Array
from random import shuffle,randint
from ctypes import c_char_p
import time
import argparse,sys,os

parser = argparse.ArgumentParser(description='MegaMillions Random Number generator')
parser.add_argument('-t', dest='tickets', type=int, default=1, help='Number of Tickets')

args = parser.parse_args()
tickets=1
def shuffle_balls(vB):
        Ctr=0
        while (True):
                shuffle(vB)
                time.sleep(0.01)

def popb(vB, fval):
        Ctr=1
        values=""
        BallsCnt=len(vB)
        while (Ctr <= 5):
                rgen=randint(1, int(BallsCnt))-1
                rlist=list(vB)
                rval=rlist.pop(rgen)
                vB=Array('i', rlist)
                values=values + " " + str(rval)
                BallsCnt=BallsCnt-1
                Ctr=Ctr+1
                time.sleep(1)
        #fval.value=StringVar(values)
        print ("Ticket " + values)

while (tickets <= args.tickets):

        Balls=Array('i', range(1,71))
        MBalls=Array('i', range(1,26))

        final_nums=Value(c_char_p, b"")
        p1 = Process(target=shuffle_balls,args=(Balls,))
        p1.start()
        p2 = Process(target=shuffle_balls,args=(MBalls,))
        p2.start()
        time.sleep(2)
        p = Process(target=popb,args=(Balls, final_nums,))
        p.start()

        p.join()

        #print ("MegaBall: ")
        #print (MBalls[randint(1, 25)-1])
        fv = "---------> MegaB: "  + str(MBalls[randint(1, 25)-1])
        print (fv)
        p1.terminate()
        p2.terminate()
