import subprocess, sys


if __name__ == "__main__":
    print("This program should not be run directly. Exiting...")
    exit(1)




s_err = sys.stderr
s_in = sys.stdin

def current_brightness():
    current = open("/sys/class/leds/kbd_backlight/brightness", "rt")
    c = int(current.read())
    current.close()
    return c


def max_brightness():
    max = open("/sys/class/leds/kbd_backlight/max_brightness", "rt")
    m = int(max.read())
    max.close()
    return m



def set_brightness(value):
    owner = subprocess.run("ls -ln /sys/class/leds/kbd_backlight/brightness | awk '{print $3}'", shell=True, check=True, executable="/bin/bash")
    user = subprocess.run("id -u", shell=False, check=True)
    if owner != user:
        subprocess.run(["pkexec", "chown", user, "/sys/class/leds/kbd_backlight/brightness"], shell=False, check=True)
        subprocess.run("chmod 666 /sys/class/leds/kbd_backlight/brightness", shell=False, check=True)
    
    try: 
        bright = open("/sys/class/leds/kbd_backlight/brightness", "rw")
        bright.write(str(value))
    except:
        s_err.write("Tried to write keyboard brightness value to unwritable file. Check permissions?")
        raise Exception("Tried to write keyboard brightness value to unwritable file. Check permissions?")
    else:
        return str(value)
    finally:
        bright.close()
