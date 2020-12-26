import json

# ユーザーの設定を読み込む関数
def config(key):
    # user-config.json 読み込み
    userConfig = open(r'include\config\user-config.json', mode = 'r', encoding = 'utf-8')
    userConfigJson = json.load(userConfig)
    # default-config.json 読み込み
    defaultConfig = open(r'include\config\default-config.json', mode = 'r', encoding = 'utf-8')
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
        msgFile = open(r'include\msg\\' + lang + '.json', mode = 'r', encoding = 'utf-8')
        msgJson = json.load(msgFile)
        try:
            return msgJson[key]
        except KeyError:
            mulLang = 'mul'
            mulMsgFile = open(r'include\msg\\' + mulLang + '.json', mode = 'r', encoding = 'utf-8')
            mulMsgJson = json.load(mulMsgFile)
            return mulMsgJson[key]
    return '<' + str(key) + '>'