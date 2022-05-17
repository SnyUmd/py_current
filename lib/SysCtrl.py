


# ********************************************************************
#インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
#OS自体に設定してあれば以下の2行は不要
def AddPath(str_path):
    import os
    
    path_str = os.environ['PATH']
    # print(path_str.find(str_path))
    
    if path_str.find(str_path) >= 0:#※エラー回避　既にpathが存在する場合は、追加をキャンセル
        print('add path cancel')
        return
    else:
        os.environ['PATH'] = os.environ['PATH'] + str_path
    print('add path')


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

# *****************************************************************
def CheckClipBoad_Img():
    from PIL import ImageGrab, Image
    # クリップボード内の情報を取得する
    clipboard_image = ImageGrab.grabclipboard()
    # clioboard_imageがImage.Image型の場合は保存する
    if isinstance(clipboard_image, Image.Image):
        return True
    else:
        return False

# *****************************************************************
def CheckClipBoad_Str():
    from pyperclip import paste
    # クリップボード内の情報を取得する
    clipboard_Str = paste()
    if type(clipboard_Str) == str and not clipboard_Str == "": return True
    else: return False

# *****************************************************************
def getClipBoad_str():
    from pyperclip import paste
    return paste()
