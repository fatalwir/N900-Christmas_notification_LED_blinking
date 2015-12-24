#!/usr/bin/python

import os
import time

def r(val):
	os.system("echo "+str(val)+" > /sys/class/leds/lp5523:r/brightness")

def g(val):
        os.system("echo "+str(val)+" > /sys/class/leds/lp5523:g/brightness")

def b(val):
        os.system("echo "+str(val)+" > /sys/class/leds/lp5523:b/brightness")

def s(val):
	time.sleep(val)

while True:
	r(255)
	s(0.25)
	r(0)
	g(255)
	s(0.25)
	g(0)
	b(255)
	s(0.25)
	b(0)
	r(255)
	g(255)
	s(0.25)
	g(0)
	b(255)
	s(0.25)
	b(0)
