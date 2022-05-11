# -*- coding: utf-8 -*-

# from posixpath import dirname
#import tkinter
#from tkinter import filedialog

file_ = 'myfile.txt'
folder_ = './test'

#*****************************************************************************
#※選択ダイアログを出した時にウインドウが残らないようにする為のもの
def SetWindow():
    import tkinter
    win_tki = tkinter.Tk()
    win_tki.geometry('0x0+0+0')
    win_tki.title('')
    win_tki.withdraw()
    return win_tki
#*****************************************************************************
def HideWindow_tk(win_tk):
    win_tk.withdraw()

#*****************************************************************************
def CloseWindow_tk(win_tk):
    win_tk.destroy()

#*****************************************************************************
# スクリプトフォルダの取得
def GetScriptDir():
    import pathlib
    return pathlib.Path(__file__).parent.absolute()

#*****************************************************************************
#ファイルの存在をチェック
def FileCheck(file_path):
    import os
    # import os
    return os.path.isfile(file_path)

def GetCurrentDirectory():
    import os
    return os.getcwd()

#*****************************************************************************
#フォルダの存在をチェック
def FolderCheck(dir_):
    import os
    os.path.isdir(dir_)

#*****************************************************************************
#ファイル選択ダイアログを表示
#FileSelect('C:\\Users', 'TextFile', '*.txt')
def FileSelect(dir_name, txt_type = '', extension = ''):
    from tkinter import filedialog
    win_ = SetWindow()
    typ = [(txt_type, extension)]
    dir = dir_name
    result_dir = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
    CloseWindow_tk(win_)
    return result_dir

#*****************************************************************************
# フォルダ選択ダイアログ表示
def FolderSelect(dir_name = ''):
    from tkinter import filedialog
    win_ = SetWindow()
    fld = filedialog.askdirectory(initialdir=dir_name)
    CloseWindow_tk(win_)
    return fld

#*****************************************************************************
#Pythonフォルダを取得
def Get_ScriptDir():
    return Get_DirName(f'{__file__}')

#*****************************************************************************
#pathからファイル名部を取得
def Get_FileName(txt_path):
    import os
    return os.path.basename(txt_path)

#*****************************************************************************
#pathからフォルダ部を抽出
def Get_DirName(txt_path):
    import os
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
def SaveFile_decide(dir_name = '', txt_type = '', extension = '', bl_save = False):
    from tkinter import filedialog
    typ = [(txt_type, extension)]
    dir = dir_name
    filename = filedialog.asksaveasfilename(filetypes = typ, initialdir = dir)

    if bl_save:
        if filename.find(extension) < 0:
            filename += extension
        return filename
    else:
        return dir

#*****************************************************************************
def ReadFileTxt(file_path):
    f = open(file_path)
    result = f.read()
    # print(result)
    f.close()
    return result

#*****************************************************************************
if __name__ == "__main__":
    a = 1
