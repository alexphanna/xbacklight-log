from math import log10

import subprocess
import sys

def get_brightness():
    return int(subprocess.run(['xbacklight', '-get'], capture_output=True, text=True, check=True).stdout)

def set_brightness(backlight):
    subprocess.run(['xbacklight', '-set', str(backlight)])

def signal_to_level(signal):
    return int(10**((signal / 100) * 2 - 2) * 100)

def level_to_signal(level):
    return int((log10(level / 100) + 2) / 2 * 100)

if (sys.argv[1] == "-inc"): 
    if (signal_to_level(level_to_signal(get_brightness()) + 1) == get_brightness()):
        set_brightness(signal_to_level(level_to_signal(get_brightness()) + 5) + 1)
    set_brightness(signal_to_level(level_to_signal(get_brightness()) + 5))
elif (sys.argv[1] == "-dec"): 
    if (signal_to_level(level_to_signal(get_brightness()) - 1) == get_brightness()):
        set_brightness(signal_to_level(level_to_signal(get_brightness()) + 5) - 1)
    set_brightness(signal_to_level(level_to_signal(get_brightness()) - 5))
elif (sys.argv[1] == "-get"): print(level_to_signal(get_brightness()))