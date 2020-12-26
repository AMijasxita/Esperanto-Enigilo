import tkinter as tk
from tkinter import ttk

from program_core.import_config_msg import *

# ウィジェット定義
class EEToolbarButton(tk.Button):
    def __init__(self, *args):
        super().__init__(*args)
        self.config(
            bg = EERoot._themeColor['bg-normal'],
            activebackground = EERoot._themeColor['light-green3'],
            relief = 'flat'
        )
        self.bind(
            '<Enter>',
            lambda e:
                self.config(bg = EERoot._themeColor['light-green3'])
        )
        self.bind(
            '<Leave>',
            lambda e:
                self.config(bg = EERoot._themeColor['bg-normal'])
        )

# ウィンドウ
class EERoot(tk.Tk):
    _themeColor = {
            # デフォルトの背景色・文字色
            'bg-normal': '#fff',
            'fg-normal': '#000',
            # 緑色系
            'light-green1': '#0f0',
            'light-green2': '#afa',
            'light-green3': '#cfc',
            'normal-green': '#0b0',
            'dark-green1': '#0a0',
            'dark-green2': '#090',
            'dark-green3': '#080',
            # 灰色系
            'gray1': '#aaa',
            'gray2': '#ccc',
            'gray3': '#eee',
        }
    
    # init
    def __init__(self, *args):
        super().__init__()

        self.title(msg('tool-name'))
        self.iconbitmap(default = 'include\icon.ico')
        self.config(bg = EERoot._themeColor['bg-normal'])
    
        # ウィジェット配置
        ## ツールバー
        widToolbar = tk.Frame(height = 25, background = EERoot._themeColor['bg-normal'])
        widToolbar.pack(anchor = tk.N, side = tk.TOP, fill = tk.X)
        ### [ファイル]
        widToolbarTab_file = EEToolbarButton(widToolbar)
        widToolbarTab_file.config(
            text = msg('toolbar-caption-template') \
                .replace('$1', msg('toolbar-file-caption')) \
                .replace('$2', msg('toolbar-file-caption-accesskey'))
        )
        widToolbarTab_file.pack(anchor = tk.N, side = tk.LEFT)
        ### [表示]
        widToolbarTab_view = EEToolbarButton(widToolbar)
        widToolbarTab_view.config(
            text = msg('toolbar-caption-template') \
                .replace('$1', msg('toolbar-view-caption')) \
                .replace('$2', msg('toolbar-view-caption-accesskey'))
        )
        widToolbarTab_view.pack(anchor = tk.N, side = tk.LEFT)
        ### [ヘルプ]
        widToolbarTab_help = EEToolbarButton(widToolbar)
        widToolbarTab_help.config(
            text = msg('toolbar-caption-template') \
                .replace('$1', msg('toolbar-help-caption')) \
                .replace('$2', msg('toolbar-help-caption-accesskey'))
        )
        widToolbarTab_help.pack(anchor = tk.N, side = tk.LEFT)
        ### 一覧辞書
        dict_toolbarTabs = {
            'file': widToolbarTab_file,
            'view': widToolbarTab_view,
            'help': widToolbarTab_help,
        }
        ### 下側の枠線
        widToolbar_borderBottom = tk.Frame(background = EERoot._themeColor['gray3'], height = 1)
        widToolbar_borderBottom.pack(anchor = tk.N, fill = tk.X)

    # 入力モード
    def inputMode(self):
        # サイズ変更
        self.geometry('600x300')
    
    # 変換モード
    def convertMode(self):
        # サイズ変更
        self.geometry('600x300')
