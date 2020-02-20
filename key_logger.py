from pynput.keyboard import Key, Listener
import time
from datetime import datetime
import numpy
import pandas as pd
def get_now():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return now
FILE_NAME = 'text.txt'
out = []

def on_press(key):
    try:
        char = key.char
    except:
        #char = key
        char = key
    finally:
        out.append([get_now(),char])
def on_release(key):
    if str(key) == 'Key.esc':
        out_data = pd.DataFrame()
        out_data['time'] = [item[0] for item in out]
        out_data['value'] = [item[1] for item in out]
        out_data.to_csv("keyborad_log/"+ get_now() +".csv")
        exit()
    pass
 
if __name__ == '__main__': 
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join() 