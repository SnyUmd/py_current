# import os
from PIL import Image
from numpy import true_divide
import SysCtrl as SCtrl

# *****************************************************************
# Tesseractのインストールが必要
# Windows
# https://github.com/UB-Mannheim/tesseract/wiki

# インストールの注意
# 　■Additional script data(download)を設定
# 　　「Japanese script」と「Japanese vertical script」にチェック
# 　
# 　■Additional language data(download)を設定
# 　　「Japanese」と「Japanese(Vertical)」にチェック
def GetImgText_File(img_file, lang_ = "jpn", tesseract_path_ = "C:\\Program Files\\Tesseract-OCR"):
    import pyocr
    #インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
    #OS自体に設定してあれば以下の2行は不要
    # path='C:\\Program Files\\Tesseract-OCR'
    SCtrl.AddPath(tesseract_path_)
    # os.environ['PATH'] = os.environ['PATH'] + path
    
    #pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    tool = tools[0]
    
    #OCR対象の画像ファイルを読み込む
    img = Image.open(img_file)
    
    #画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    result_text = tool.image_to_string(img, lang=lang_, builder=builder)
    return result_text

# *****************************************************************
# Tesseractのインストールが必要
# Windows
# https://github.com/UB-Mannheim/tesseract/wiki

# インストールの注意
# 　■Additional script data(download)を設定
# 　　「Japanese script」と「Japanese vertical script」にチェック
# 　
# 　■Additional language data(download)を設定
# 　　「Japanese」と「Japanese(Vertical)」にチェック
def GetImgText_Image(img_, lang_ = "jpn", tesseract_path_ = "C:\\Program Files\\Tesseract-OCR"):
    #インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
    #OS自体に設定してあれば以下の2行は不要
    # path='C:\\Program Files\\Tesseract-OCR'
    
    import pyocr
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
def GetClipImg():
    from SysCtrl import CheckClipBoad_Img
    from PIL import ImageGrab, Image
    if CheckClipBoad_Img():
        resultImg = ImageGrab.grabclipboard()
    else:
        resultImg = "err"
    return resultImg

# ********************************************************************
def SaveClipImg(save_dir):
    import os
    import datetime
    from PIL import ImageGrab, Image

    # 保存先ディレクトリの指定
    directory = save_dir

    # クリップボード内の情報を取得する
    clipboard_image = ImageGrab.grabclipboard()

    # ファイルネームをを指定する。
    file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(directory, "{}.png".format(file_name))

    # clioboard_imageがImage.Image型の場合は保存する
    if isinstance(clipboard_image, Image.Image):
        clipboard_image.save(file_name, optimize=True, quality=20)
        print("saved to {}".format(file_name))
        return True
    else:
        print("no image")
        return False
