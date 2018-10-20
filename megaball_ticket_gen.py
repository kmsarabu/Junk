#!/usr/bin/python

from random import shuffle,randint
import time
import argparse,sys,os

parser = argparse.ArgumentParser(description='MegaMillions Random Number generator')
parser.add_argument('-t', dest='tickets', type=int, default=1, help='Number of Tickets')

args = parser.parse_args()

tickets=1

while (tickets <= args.tickets):

	Balls=list(range(1,71))
	MBalls=list(range(1,26))

	LottoBalls=""
	BallsCnt=70
	BCtr=0
	while (BCtr < 5):
		i=0
		BCtr=BCtr+1
		while ( i <= 9 ):
			time.sleep(1)
			i=i+1
			shuffle(Balls)
		rgen=randint(1,BallsCnt)
		LottoBalls = LottoBalls + " " + str(Balls[rgen])
		Balls.pop(rgen)
		BallsCnt=BallsCnt-1
	i=0
	while ( i <= 9 ):
		time.sleep(1)
		i=i+1
		shuffle(MBalls)

	LottoBalls = LottoBalls + " MegaBall: " + str(MBalls[randint(1,25)])

	print ("Ticket " + str(tickets) + ":---> " + LottoBalls)
	tickets=tickets+1
