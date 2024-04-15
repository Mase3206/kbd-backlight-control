#!/usr/bin/env python3

import argparse
import subprocess



def userOwns() -> bool:
	owner = subprocess.run(['ls', '-n', '/sys/class/leds/kbd_backlight/brightness', '|', 'awk', "'{print", "$3}'"], capture_output=True, text=True)
	user = subprocess.run(['id', '-u'], capture_output=True, text=True)
	return bool(user == owner)



def getCurrent() -> int:
	with open("/sys/class/leds/kbd_backlight/brightness", "r") as f:
		return int(f.read())



def getMax() -> int:
	with open("/sys/class/leds/kbd_backlight/max_brightness", "r") as f:
		return int(f.read())



def setBright(value: int) -> int:
	if not userOwns():
		subprocess.run(['pkexec', 'chmod', '666', '/sys/class/leds/kbd_backlight/brightness'])
	
	with open("/sys/class/leds/kbd_backlight/brightness", "w") as f:
		f.write(str(value))	

	return value



def inc(value: int) -> int:
	if (new := getCurrent() + value) <= getMax():
		return setBright(new)
	else:
		return setBright(getMax())



def dec(value: int) -> int:
	if (new := getCurrent() - value) >= 0:
		return setBright(new)
	else:
		return 0



def cli():
	parser = argparse.ArgumentParser(
		description='Increase, decrease, or set the keyboard brightness level in Linux + GNOME\nThis functionality is missing from GNOME Desktop, so I made it myself.',
		epilog='Keyboard Brightness Controller is subject to copyright under the GNU General Public License (v3). See LICENSE for details.'
	)

	parser.add_argument(
		'mode', 
		choices=['inc', 'dec', 'set'], 
		help='Selects the mode of operation: inc to increase by the specified amount; dec to decrease by the specified amount; set to snap to the specified amount.'
	)
	parser.add_argument(
		'value',
		type=int, 
		help='percentage to increase/decrease by or to set to (0 to 100)', 
	)

	args = parser.parse_args()


	if args.mode == 'set':
		print(setBright(args.value))
	elif args.mode == 'inc':
		print(inc(args.value))
	elif args.mode == 'dec':
		print(dec(args.value))



if __name__ == '__main__':
	cli()
