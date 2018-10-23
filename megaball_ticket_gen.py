#!/usr/bin/python

from multiprocessing import Process, Manager
from random import shuffle,randint
import time
import argparse,sys,os

parser = argparse.ArgumentParser(description='MegaMillions Random Number generator')
parser.add_argument('-t', dest='tickets', type=int, default=1, help='Number of Tickets')

args = parser.parse_args()
tickets=1

def shuffle_balls(vB):
 try:
	Ctr=0
	while (True):
		try:
			shuffle(vB)
		except Exception, e:
			pass
		time.sleep(0.001)
 except Exception, e:
	print ("Error in shuffleballs")
	print (len(vB))
	
def popb(vB, Res):
	Ctr=0
	values=""
	BallsCnt=len(vB)
	while (Ctr < 5):
		rgen=randint(1, int(BallsCnt))-1
		rval=vB.pop(rgen)
		Res[Ctr]=rval
		values=values + " " + str(rval)
		BallsCnt=BallsCnt-1
		Ctr=Ctr+1
		time.sleep(1)

while (tickets <= args.tickets):

	with Manager() as manager:
		Balls = manager.list( range(1,71) )
		MBalls = manager.list( range(1,26) )
		Res = manager.list( range(1,7) )

		p1 = Process(target=shuffle_balls,args=(Balls,))
		p1.start()
		p2 = Process(target=shuffle_balls,args=(MBalls,))
		p2.start()
		time.sleep(2)
		p = Process(target=popb,args=(Balls, Res,))
		p.start()

		p.join()

		ri = randint(1, 25)-1
		rval = MBalls[ri]
		Res[5] = rval
		print (Res)
		p1.terminate()
		p2.terminate()

		tickets=tickets+1
