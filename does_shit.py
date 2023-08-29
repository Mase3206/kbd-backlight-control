import subprocess, sys


if __name__ == "__main__":
    raise Exception("This program should not be run directly. Exiting...")




s_err = sys.stderr

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
        subprocess.run("pkexec chmod 666 /sys/class/leds/kbd_backlight/brightness", shell=False, check=True)
    
    try: 
        bright = open("/sys/class/leds/kbd_backlight/brightness", "rw")
        bright.write(str(value))
    except:
        return -1
    else:
        return str(value)
    finally:
        bright.close()
