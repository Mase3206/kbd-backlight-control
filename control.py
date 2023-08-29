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
value = int(s_in[1] / 100 * 255)

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
    does_shit.set_brightness(value)
    
