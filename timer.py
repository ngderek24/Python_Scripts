import os
import threading
import time

print "Timer has launched"

def ring_alarm():
	os.startfile('C:/Users/Derek/Documents/Growl.mp3')
	print "Time's up! Thank you for using Timer"

status = 0
minutes = -1;
seconds = -1;
while True:
	while minutes < 0 or minutes > 59:
		minutes = input('Enter how many minutes (must be valid): ')
	while seconds < 0 or seconds > 59:
		seconds = input('Enter how many seconds (must be valid): ')

	if seconds < 10 and minutes < 10:
		print "The time for the timer is 0" + `minutes` + ":0" + `seconds`
	elif seconds < 10:
		print "The time for the timer is " + `minutes` + ":0" + `seconds`
	elif minutes < 10:
		print "The time for the timer is 0" + `minutes` + ":" + `seconds`
	else:
		print "The time for the timer is " + `minutes` + ":" + `seconds`
	
	while status != 1 and status != 2:
		status = input("To start the clock type \"1\", to edit the time type \"2\": ")
	if status == 1:
		break
	else:
		status = 0
		minutes = -1;
		seconds = -1;

total_sec = 60*minutes + seconds
t = threading.Timer(total_sec, ring_alarm)
t.start()
print "The timer has started"
