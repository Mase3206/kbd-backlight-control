import sys, does_shit

s_in = sys.stdin
s_out = sys.stdout
s_err = sys.stderr

modes = {
    "inc": 0,
    "dec": 1,
    "set": 2,
    "help": 3,
    "?": 3
}
mode = modes[s_in[0]]
max = does_shit.max_brightness()
value = int(s_in[1] / 100 * max)


if mode == 3:
    print("""
          Keyboard Brightness Controller
          by Noah S. Roberts, copyright via GPLv3

          --- SYNTAX ---
          control.py inc|dec|set|help <value>

              inc - increase brightness by <value> percent
              dec - decrease brightness by <value> percent
              set - set brightness to <value> percent
              help|? - display this help output
          
          Keyboard Brightness Controller is subject to copyright under the GNU General Public License (v3). See LICENSE for details.
    """)


if mode == 2:
    output = does_shit.set_brightness(value)
    if output < 0:
        s_err.write("ERROR: failed to write brightness value to file")
        raise Exception("ERROR: failed to write brightness value to file")
    else:
        print(output)


if mode == 1:
    current = does_shit.current_brightness()
    if current + value <= max:
        does_shit.set_brightness(value)
    else:
        does_shit.set_brightness(255)


if mode == 0:
    current = does_shit.current_brightness()
    if current - value >= 0:
        does_shit.set_brightness(value)
    else:
        does_shit.set_brightness(0)
