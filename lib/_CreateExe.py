
# cx_Freeze6.5.3、Python3.9.1で動作確認しました。
# cx_Freeze、実行ファイル作成用 
 
import sys
from cx_Freeze import setup, Executable
 
base = None
 
# Ubuntuの場合、sys.platform='linux'です
# GUI=有効, CUI=無効 にする
# if sys.platform == 'win32' : base = 'Win32GUI'
 
# 実行ファイルにしたいPythonスクリプトファイルを指定
exe = Executable(script = 'Check_FlashBinary.py', base = base)
 
# セットアップ
setup(name = 'Check_FlashBinary_1_0_0',
    version = '1.0.0',
    description = 'converter',
    executables = [exe])