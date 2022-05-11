


# ********************************************************************
#インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
#OS自体に設定してあれば以下の2行は不要
def AddPath(str_path):
    import os
    os.environ['PATH'] = os.environ['PATH'] + str_path

# ********************************************************************
def TextCopyToClip(target_text, bl_message_box = False, str_message = "クリップボードにコピーしました。"):
    import pyperclip
    import WindowCtrl as wCtrl
    pyperclip.copy(target_text)
    if bl_message_box:
        wCtrl.MsgBox_Inf("", str_message)

# ********************************************************************
def GetPrcsTime():
    import time
    result_time = time.process_time()#開始時間をセット
    return result_time

    
