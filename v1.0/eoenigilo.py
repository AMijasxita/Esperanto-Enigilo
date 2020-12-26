# Version 1.0

import tkinter as tk
from tkinter import ttk
import sched, time

from program_core.import_config_msg import *

class EENowLoadingRoot(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)

        self.title(msg('nowloading-window-title'))
        self.iconbitmap(default = 'include\icon.ico')
        self.config(bg = '#fff')

        # ウィジェット
        widStatusLabel = tk.Label(self, anchor = tk.W, text = msg('nowloading-window-title'))
        widStatusLabel.pack(anchor = tk.NW, padx = 5, pady = 5)
        widPB = ttk.Progressbar(self, mode = 'indeterminate', orient = tk.HORIZONTAL)
        widPB.pack(padx = 5, fill = tk.X)
        widPB.start()

        # メイン
        s = sched.scheduler(time.time, time.sleep)
        s.enter(0, 1, main)
        s.run()

        nowloading_root.destroy()

def main():
    from program_core import eoenigilo_core
    root = eoenigilo_core.EERoot()
    root.inputMode() # 仮
    root.mainloop()

nowloading_root = EENowLoadingRoot()
nowloading_root.mainloop()
