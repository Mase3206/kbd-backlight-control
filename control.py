import sys, does_shit, argparse

s_err = sys.stderr


parser = argparse.ArgumentParser(prog="Keyboard Brightness Controller", description="Increase, decrease, or set the keyboard brightness level in Linux + GNOME\nThis functionality is missing from GNOME Desktop, so I made it myself.", epilog="Keyboard Brightness Controller is subject to copyright under the GNU General Public License (v3). See LICENSE for details.")

parser.add_argument('mode', choices=['inc', 'dec', 'set'], default='set', help='Selects the mode of operation: inc to increase by the specified amount; dec to decrease by the specified amount; set to snap to the specified amount.')
parser.add_argument("percent", choices=range(1,100), type=int, help="percentage to increase/decrease by or to set to", default=10)

args = parser.parse_args()


max = does_shit.max_brightness()
value = int(args.percent / 100 * max)


if args.mode == "set":
    output = does_shit.set_brightness(value)
    if output < 0:
        s_err.write("ERROR: failed to write brightness value to file")
        raise Exception("ERROR: failed to write brightness value to file")
    else:
        print(output)


if args.mode == "inc":
    current = does_shit.current_brightness()
    if current + value <= max:
        does_shit.set_brightness(value)
    else:
        does_shit.set_brightness(255)


if args.mode == "dec":
    current = does_shit.current_brightness()
    if current - value >= 0:
        does_shit.set_brightness(value)
    else:
        does_shit.set_brightness(0)
