# cx_Freeze6.5.3、Python3.9.1で動作確認しました。
# cx_Freeze、実行ファイル作成用 


import sys
from cx_Freeze import setup, Executable
 
base = None
 
# Ubuntuの場合、sys.platform='linux'です
# GUI=有効, CUI=無効 にする
# if sys.platform == 'win32' : base = 'Win32GUI'
 
# 実行ファイルにしたいPythonスクリプトファイルを指定
exe = Executable(script = 'Check_FlashBinary.py', base = base)#ここを編集"script = []"
 
# セットアップ
setup(name = 'Check_FlashBinary',#ここを編集"name = []"
    version = '0.1',
    description = 'converter',
    executables = [exe])