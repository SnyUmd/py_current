#!python3.9

# cx_Freeze6.5.3、Python3.9.1で動作確認しました。
# cx_Freeze、実行ファイル作成用 

# exeファイル作成コマンド
# python setup.py build

import sys
from cx_Freeze import setup, Executable

'''
base = None

# Ubuntuの場合、sys.platform='linux'です
# GUI=有効, CUI=無効 にする
# if sys.platform == 'win32' : base = 'Win32GUI'

# 実行ファイルにしたいPythonスクリプトファイルを指定
exe = Executable(script = 'ReadImgFile_Text.py', base = base, icon='Text3.ico')#ここを編集"script = []"

# セットアップ
setup(name = 'ReadImgFile_Text',#ここを編集"name = []"
    version = '0.1',
    description = 'converter',
    executables = [exe])
'''