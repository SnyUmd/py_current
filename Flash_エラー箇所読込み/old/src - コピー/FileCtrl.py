# -*- coding: utf-8 -*-

import os
#import tkinter
#from tkinter import filedialog

file_ = 'myfile.txt'
folder_ = './test'


#*****************************************************************************
#ファイルの存在をチェック
def FileCheck(file_path):
    # import os
    return os.path.isfile(file_path)

def GetCurrentDirectory():
    return os.getcwd()

#*****************************************************************************
#フォルダの存在をチェック
def FolderCheck(dir_):
    os.path.isdir(dir_)

#*****************************************************************************
#ファイル選択ダイアログを表示
#FileSelect('C:\\Users', 'TextFile', '*.txt')
def FileSelect(dir_name, txt_type = '', extension = ''):
    from tkinter import filedialog
    typ = [(txt_type, extension)]
    dir = dir_name
    return filedialog.askopenfilename(filetypes = typ, initialdir = dir)

#*****************************************************************************
#Pythonフォルダを取得
def Get_ScriptDir():
    return Get_DirName(f'{__file__}')

#*****************************************************************************
#pathからファイル名部を取得
def Get_FileName(txt_path):
    return os.path.basename(txt_path)

#*****************************************************************************
#pathからフォルダ部を抽出
def Get_DirName(txt_path):
    return os.path.dirname(txt_path)

#*****************************************************************************
#ファイル作成
def CreateFile(file_path, value_ = '', extension = ''):
    import os
    file_p = file_path
    if file_p.find(extension) < 0:
        file_p += extension

    f = open(file_p, 'w')
    f.write(value_)
    f.close()

    return os.path.isfile(file_p)

#*****************************************************************************
#ファイル保存ダイアログを表示
#SaveFile('C:\\Users', 'TextFile', '*.txt')
def SaveFile_decide(dir_name = '', txt_type = '', extension = ''):
    from tkinter import filedialog
    typ = [(txt_type, extension)]
    dir = dir_name
    filename = filedialog.asksaveasfilename(filetypes = typ, initialdir = dir)
    if filename.find(extension) < 0:
        filename += extension
    return filename

#*****************************************************************************
def ReadFileTxt(file_path):
    f = open(file_path)
    result = f.read()
    # print(result)
    f.close()
    return result

#*****************************************************************************
if __name__ == "__main__":
    #SaveFile_decide('C:\\Users\\E324595\\Documents\\_umd\\soft\\Flash_エラー箇所読込み\\scr', '', '.txt')
    text = FileSelect('', 'TextFile', '*.txt')
    #text = FileSelect('C:\\Users\\E324595\\Documents\\_umd\\soft\\Flash_エラー箇所読込み\\scr', 'TextFile', '*.txt')
    #print('********************** ' + text + ' *********************')
    #print(Get_DirName('C:\\Users\\E324595\\Documents\\_umd\\soft\\Flash_エラー箇所読込み\\scr\\test.txt'))
