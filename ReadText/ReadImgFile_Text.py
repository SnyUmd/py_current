# from sklearn import tree
import ImgCtrl as iCtrl
import WindowCtrl as WCtrl
import SysCtrl as SCtrl
# import FileCtrl as FCtrl

import tkinter as tk0

SelectFilePath = ''
InitDir = ''

def ClickFile():
    WCtrl.ClickFileRead(TxbFileTK,'Image file','*.jpg *.Png *.png *.ico')

def ClickTextRead():
    text_ = iCtrl.GetImgText_File(TxbFileTK.get())
    SCtrl.TextCopyToClip(text_, True, str_message="抽出したテキストを、クリップボードにコピーしました。\n\n\n %s" % text_)
    # WCtrl.MsgBox_Inf(mess_=text_, title_="")

WinSts = [600, 80, 10, 10, "テキスト抽出"]

# エリア1----------------------------------------
LblFileSts = [10, 10, '選択ファイル']
TxbFileSts = [WinSts[0] - 150, 20, LblFileSts[0] + 70, LblFileSts[1], True, ""]
BtnFileSts = [50, 20, TxbFileSts[2] + TxbFileSts[0] + 10, TxbFileSts[3], ClickFile, "File"]

# エリア2----------------------------------------
BtnTextReadSts = [WinSts[0] - 50, 20, 25, LblFileSts[1] + 30, ClickTextRead, 'テキスト抽出']


WinTK = WCtrl.SetWindow(WinSts[0], WinSts[1], WinSts[2], WinSts[3], WinSts[4])
LblFileTK = WCtrl.SetLabel(LblFileSts[0], LblFileSts[1], LblFileSts[2])
TxbFileTK = WCtrl.SetTxbEntry(TxbFileSts[0], TxbFileSts[1], TxbFileSts[2], TxbFileSts[3], TxbFileSts[4], TxbFileSts[5])
BtnFileTK = WCtrl.SetBtn(BtnFileSts[0], BtnFileSts[1], BtnFileSts[2], BtnFileSts[3], BtnFileSts[4], BtnFileSts[5])

BtnTextRead = WCtrl.SetBtn(BtnTextReadSts[0], BtnTextReadSts[1], BtnTextReadSts[2], BtnTextReadSts[3], BtnTextReadSts[4], BtnTextReadSts[5])

WCtrl.WindowLoopStart(tk0)






