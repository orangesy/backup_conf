#!/usr/bin/env python
import commands, sys, getopt, time, os
STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2

def main():
	d = sys.argv
	if d[1]=="1":
		print "warning"
		sys.exit(STATE_WARNING)	
	elif d[1]=="2":
		print "critical"
		sys.exit(STATE_CRITICAL)
	else:
		print "ok"
		sys.exit(STATE_OK)

if __name__ == "__main__":
    main()
