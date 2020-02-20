from pynput import mouse
import pyautogui
import time
from datetime import datetime
import pandas as pd

out = []
def get_now():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return now
class Monitor:
    def __init__(self):
        self.counter = 0
        self.over_count = 5

    def count(self):
        self.counter += 1
        
        print('Count:{0}'.format(self.counter))

    def is_over(self):
        return True if self.counter >= self.over_count else False

    def call(self):
        self.count()
        if self.is_over():
            out_data = pd.DataFrame()
            out_data['time'] = [item[0] for item in out]
            out_data['x'] = [item[1] for item in out]
            out_data['y'] = [item[2] for item in out]
            out_data['file_name'] = [item[3] for item in out]
            out_data.to_csv("click_log/"+ get_now() +".csv")
            print('Done')
            self.listener.stop() # 規定回数過ぎたら終了
            exit()

    def on_click(self, x, y, button, pressed):
        file_name = 'screen_shot'+ str(self.counter) +'.png'
        pyautogui.screenshot('click_log/screenshot/' + file_name)
        out.append([get_now(),x,y,file_name])
        if pressed:
            self.call()

    def start(self):
        with mouse.Listener(
            on_click=self.on_click) as self.listener:
            self.listener.join()
if __name__ == '__main__':
    monitor = Monitor()
    monitor.start()
    