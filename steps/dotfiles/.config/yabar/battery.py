#!/usr/bin/env python3

import subprocess as sub

def get_battery():
	p = sub.Popen(['acpi', '-b'],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()

	output = str(output)[2:-3].split(",")

	percent = output[1][1:]
	if (len(output) > 2):
		remaining = " (" + output[2].split(" ")[1][:-3] + ")"
	else:
		remaining = " (--:--)"

	return " " + percent + remaining

print(get_battery())
