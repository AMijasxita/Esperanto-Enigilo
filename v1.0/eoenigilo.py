# Version 1.0

import tkinter as tk
from tkinter import ttk
import json

### 準備 ###

# ユーザーの設定を読み込む関数
def config(key):
    # user-config.json 読み込み
    userConfig = open(r'include\config\user-config.json', 'r')
    userConfigJson = json.load(userConfig)
    # default-config.json 読み込み
    defaultConfig = open(r'include\config\default-config.json', 'r')
    defaultConfigJson = json.load(defaultConfig)
    
    # key から取り出す
    try:
        return userConfigJson[key]
    except KeyError:
        return defaultConfigJson[key]

# メッセージを読み込む関数
def msg(key, lang = None):
    if lang != 'zxx':
        if lang == None:
            lang = config('language')
        msgFile = open(r'include\msg\\' + lang + '.json', 'r')
        msgJson = json.load(msgFile)
        return msgJson[key]
    return '<' + str(key) + '>'

### メイン ###

# ウィジェット定義
class EEToolbarButton(ttk.Button):
    def __init__(self, *args):
        super().__init__()

# ウィンドウ
class EERoot(tk.Tk):
    _themeColor = {
            'bg-normal': '#ffffff',
            'fg-normal': '#000000',
            'light-g1': '#00ff00',
            'light-g2': '#aaffaa',
            'light-g3': '#ccffcc',
            'normal-g': '#00bb00',
            'dark-g1': '#00aa00',
            'dark-g2': '#009900',
            'dark-g3': '#008800',
        }
    
    # init
    def __init__(self, *args):
        super().__init__()

        self.title(msg('tool-name', 'mul'))
        self.iconbitmap(default = 'include\icon.ico')
        self.config(bg = EERoot._themeColor['bg-normal'])

        # スタイル定義
        ttk.Style().configure(
            'EEToolbarButton',
            bg = EERoot._themeColor['bg-normal'],
            relief = 'flat',
            cursor = 'hand2',
        )
    
        # ウィジェット配置
        widToolbar = ttk.Frame()
        widToolbar.pack(fill = tk.X)
        widToolbarFile = EEToolbarButton(widToolbar)
        widToolbarFile.config(
            text = msg('toolbar-caption-template', 'mul') \
                .replace('$1', msg('toolbar-file-caption')) \
                .replace('$2', msg('toolbar-file-caption-accesskey', 'mul'))
        )
        widToolbarFile.pack(anchor = tk.W)
        ### 作業中 ###

    # 入力モード
    def inputMode(self):
        # サイズ変更
        self.geometry('600x300')
    
    # 変換モード
    def convertMode(self):
        # サイズ変更
        self.geometry('600x300')

# メイン
def main():
    root = EERoot()
    root.inputMode()
    root.mainloop()

main()