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
def GetClipImg():
    from SysCtrl import CheckClipBoad_Img
    from PIL import ImageGrab, Image
    if CheckClipBoad_Img():
        resultImg = ImageGrab.grabclipboard()
    else:
        resultImg = "err"
    return resultImg

# ********************************************************************
def TextCopyToClip(target_text, bl_message_box = False, str_message = "クリップボードにコピーしました。"):
    import pyperclip
    import WindowCtrl as wCtrl
    pyperclip.copy(target_text)
    if bl_message_box:
        wCtrl.MsgBox_Inf("", str_message)

# *****************************************************************
def GetImgText_Image(img_, lang_ = "jpn", tesseract_path_ = "C:\\Program Files\\Tesseract-OCR"):
    #インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
    #OS自体に設定してあれば以下の2行は不要
    # path='C:\\Program Files\\Tesseract-OCR'
    
    import pyocr
    import SysCtrl as SCtrl

    SCtrl.AddPath(tesseract_path_)

    # os.environ['PATH'] = os.environ['PATH'] + path
    #pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    tool = tools[0]
    
    #画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    result_text = tool.image_to_string(img_, lang=lang_, builder=builder)
    return result_text


# *****************************************************************
def SerchText_ClipImg():
    # try:
        # raise ValueError("error!")
    # print('クリップボード内のイメージよりテキストを抽出')
    isImage = CheckClipBoad_Img()#クリップボードがイメージであるか判定
    if not isImage:#イメージでは無いとき
        result_ = "-----"
    else:#イメージだった時、イメージ内のテキストを判定
        Img_ = GetClipImg()
        if Img_ == "err":
            print("err")
            
        else:
            text_ = GetImgText_Image(Img_)
            if not text_ == "":
                result_ = text_
                TextCopyToClip(text_, False)#クリップボードに保存
            else:
                result_ = "-----"
    return result_




print(SerchText_ClipImg())