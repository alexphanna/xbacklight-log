import math
import pickle
import subprocess
import sys

def get_measured():
    return int(subprocess.run(['xbacklight', '-get'], capture_output=True, text=True).stdout)

def get_perceived():
    with open('/home/alex/Brightness/perceived_brightness', 'rb') as fi:
        return pickle.load(fi)
        
def set_brightness(perceived):
    with open('/home/alex/Brightness/perceived_brightness', 'wb') as fi:
        pickle.dump(perceived, fi)
    subprocess.run(['xbacklight', '-set', str(perceived_to_measured(perceived))])

def perceived_to_measured(perceived):
    if perceived == 0: return 0
    else: return round(10**((perceived / 100) * 2 - 2) * 100)

def measured_to_perceived(measured):
    return round((math.log10(measured / 100) + 2) / 2 * 100)

if (len(sys.argv) == 2):
    if (sys.argv[1] == "-inc" and get_perceived() < 100): set_brightness(get_perceived() + 5)
    elif (sys.argv[1] == "-dec" and get_perceived() > 0): set_brightness(get_perceived() - 5)
    elif (sys.argv[1] == "-get"): print(get_perceived())