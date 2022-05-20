# from sklearn import tree
# タスクトレイアイコンについての参考
# https://blog2.k05.biz/2021/09/python-pystray.html

#翻訳Webアプリ作成手順
# https://qiita.com/satto_sann/items/be4177360a0bc3691fdf

from logging import exception
import threading
import pystray
from pystray import Icon, Menu, MenuItem
from PIL import Image
import sys

from argparse import Action
import ImgCtrl as iCtrl
import WindowCtrl as wCtrl
import SysCtrl as sCtrl
import KeyCtrl as kCtrl

global soft_version

global ActionSts
global pressCnt
global Loop_Main
global t_main
global t_icon
global icon_
global sys_sts
global aryKeys
global aryMsg
# global Loop_icon

soft_version = 'software version 1.1.0'

ActionSts = 0
pressCnt = [0, 0, 0, 0, 0, 0]
Loop_Main = True
sys_sts = True
aryKeys = ["/", "\\", ":", "h", "esc", "]"]

aryMsg = ["[win] + [ctrl] + %s  =  クリップボードの画像からテキストを抽出" % aryKeys[0],
           "[win] + [ctrl] + %s  =  クリップボードの英語を翻訳" % aryKeys[1],
           "[win] + [ctrl] + %s  =  選択画像内のテキストを抽出(ウインドウ)" % aryKeys[2],
           "[win] + [ctrl] + %s  =  ヘルプ" % aryKeys[3],
           "[win] + [ctrl] + %s  =  終了" % aryKeys[4]]

# # *******************************************************************************
# def ClickFile():
#     wCtrl.ClickFileRead(TxbFileTK,'Image file','*.jpg *.Png *.png *.ico')

# # *******************************************************************************
# def ClickTextRead():
#     text_ = iCtrl.GetImgText_File(TxbFileTK.get())
#     sCtrl.TextCopyToClip(text_, True, str_message="抽出したテキストを、クリップボードにコピーしました。\n\n\n %s" % text_)
#     # WCtrl.MsgBox_Inf(mess_=text_, title_="")


# *******************************************************************************
def SerchText_ClipImg():
    try:
        print('クリップボード内のイメージよりテキストを抽出')
        isImage = sCtrl.CheckClipBoad_Img()#クリップボードがイメージであるか判定
        if not isImage:#イメージでは無いとき
            wCtrl.MsgBox_err('errer', 'not image')
        else:#イメージだった時、イメージ内のテキストを判定
            Img_ = iCtrl.GetClipImg()

            if Img_ == "err":
                print("err")
                
            else:
                text_ = iCtrl.GetImgText_Image(Img_)
                if not text_ == "":
                    msg_ = text_
                    sCtrl.TextCopyToClip(text_, True)#クリップボードに保存
                else:
                    msg_ = "イメージの中に、テキスト判定できるものがありませんでした"
                
                wCtrl.MsgBox_Inf(mess_=msg_, title_="")#メッセージボックス表示
    except:
        print('Error　SerchText_ClipImg')
        print('Error　クリップボードイメージ テキスト抽出')
        wCtrl.MsgBox_err('Error', 'クリップボードイメージ内のテキスト抽出に失敗しました。')

    resetSts()
    print('SerchText clipImg end')
    # pressCnt = [0, 0, 0, 0]
    # ActionSts = 0

# *******************************************************************************
def Translat_ja_to_en():
    try:
        print('クリップボード内の英語テキストを日本語に翻訳')
        isStr = sCtrl.CheckClipBoad_Str()#クリップボードがテキストであるか確認
        if not isStr:#テキストでは無いとき
            wCtrl.MsgBox_err('errer', 'not text')
        else:#イメージだった時、翻訳を実行
            import Translation
            wCtrl.MsgBox_Inf('', 'Webブラウザに翻訳結果を表示します。')
            cStr = sCtrl.getClipBoad_str()
            Translation.GetTR(cStr)
    except:
        print('Error　Translat_ja_to_en')
        print('Error　翻訳')
        wCtrl.MsgBox_err('Error', '翻訳に失敗しました。')
        
    print('Translat ja to en end')
    resetSts()
    

# *******************************************************************************
def SerchText_Window():
    import tkinter as tk0
                
    # ----------------------------------------------------------------------
    def ClickFile():
        wCtrl.ClickFileRead(TxbFileTK,'Image file','*.jpg *.Png *.png *.ico')

    # ----------------------------------------------------------------------
    def ClickTextRead():
        text_ = iCtrl.GetImgText_File(TxbFileTK.get())
        sCtrl.TextCopyToClip(text_, True, str_message="抽出したテキストを、クリップボードにコピーしました。\n\n\n %s" % text_)
        # WCtrl.MsgBox_Inf(mess_=text_, title_="")

    print('選択画像内のテキストを抽出')
    WinSts = [600, 80, 10, 10, "テキスト抽出"]

    # エリア1----------------------------------------
    LblFileSts = [10, 10, '選択ファイル']
    TxbFileSts = [WinSts[0] - 150, 20, LblFileSts[0] + 70, LblFileSts[1], True, ""]
    BtnFileSts = [50, 20, TxbFileSts[2] + TxbFileSts[0] + 10, TxbFileSts[3], ClickFile, "File"]

    # エリア2----------------------------------------
    BtnTextReadSts = [WinSts[0] - 50, 20, 25, LblFileSts[1] + 30, ClickTextRead, 'テキスト抽出']


    WinTK = wCtrl.SetWindow(WinSts[0], WinSts[1], WinSts[2], WinSts[3], WinSts[4])
    LblFileTK = wCtrl.SetLabel(LblFileSts[0], LblFileSts[1], LblFileSts[2])
    TxbFileTK = wCtrl.SetTxbEntry(TxbFileSts[0], TxbFileSts[1], TxbFileSts[2], TxbFileSts[3], TxbFileSts[4], TxbFileSts[5])
    BtnFileTK = wCtrl.SetBtn(BtnFileSts[0], BtnFileSts[1], BtnFileSts[2], BtnFileSts[3], BtnFileSts[4], BtnFileSts[5])

    BtnTextRead = wCtrl.SetBtn(BtnTextReadSts[0], BtnTextReadSts[1], BtnTextReadSts[2], BtnTextReadSts[3], BtnTextReadSts[4], BtnTextReadSts[5])
    try:
        wCtrl.WindowLoopStart(tk0)

    
    except:
        print('Error　SerchText_Window')
        print('Error　選択イメージ テキスト抽出')
        wCtrl.MsgBox_err('Error', '選択イメージ内のテキスト抽出に失敗しました。')
    print('SerchText windownd end')
    resetSts()
    
# *******************************************************************************
def displayHelp(bl_msgbox):
    global aryMsg
    global soft_version
    # print("%s\r\n%s\r\n%s\r\n%s" % (aryMsg[0], aryMsg[1], aryMsg[2], aryMsg[3], aryMsg[4]))
    # wCtrl.MsgBox_Inf('help', "%s\r\n%s\r\n%s\r\n%s\r\n%s" % (aryMsg[0], aryMsg[1], aryMsg[2], aryMsg[3], aryMsg[4]))
    msg_str = ""
    loop_num = len(aryMsg)
    
    for i in range(loop_num):
        msg_str += aryMsg[i]
        msg_str += "\r\n" if not i >= loop_num else ""
    
    msg_str += "\r\n\r\n%s" % soft_version
        
    print(msg_str)
    if bl_msgbox:
        wCtrl.MsgBox_Inf('help', msg_str)
    resetSts()
    
# *******************************************************************************
def resetSts():
    global pressCnt
    global ActionSts
    for i in range(len(pressCnt)):
        pressCnt[i] = 0

    ActionSts = 0
    # print(pressCnt)
    
# *******************************************************************************
def quit_system():
    global Loop_Main
    global t_main
    global icon_
    global sys_sts

    Loop_Main = False
    sys_sts = False
    icon_._hide()
    icon_.stop()
    print('system quit')
    


# *******************************************************************************
def Translat_en_to_ja_Win():
    import tkinter as TK1
    global TxbMultiJaSts

    #----------------------------------------
    def ClickRun():
        import Translation

        ja_txt = wCtrl.GetValue_ScrolledText(TxbMultiJa_TK)
        Translation.GetTR(ja_txt, 'ja', 'en')
        # wCtrl.DelValue_ScrolledText(TxbMultiEn_TK)
        # wCtrl.AddValue_ScrolledText(TxbMultiEn_TK, en_txt)
        print('日本語→英語　実行')
        # print(en_txt)

    print('英語変換ツール起動')
    WinSts = [600, 130, 10, 10, "テキスト抽出"]
    LblFileSts = [10, 10, '日本語']
    TxbMultiJaSts = [WinSts[0] - 20, 50, LblFileSts[0], LblFileSts[1] + 20, True, '']
    BtnRunSts = [WinSts[0] - 20, 30, TxbMultiJaSts[2], TxbMultiJaSts[3] + TxbMultiJaSts[1] + 10, ClickRun, "日本語→英語"]
    # TxbMultiEnSts = [WinSts[0] - 20, 50, TxbMultiJaSts[2], BtnRunSts[3] + BtnRunSts[1] + 10, False, '']
    
    Win_TK = wCtrl.SetWindow(WinSts[0], WinSts[1], WinSts[2], WinSts[3], WinSts[4])
    LblFile_TK = wCtrl.SetLabel(LblFileSts[0], LblFileSts[1], LblFileSts[2])
    TxbMultiJa_TK = wCtrl.SetTxbMultiLine(TxbMultiJaSts[0], TxbMultiJaSts[1], TxbMultiJaSts[2], TxbMultiJaSts[3], TxbMultiJaSts[4], TxbMultiJaSts[5])
    BtnRun_TK = wCtrl.SetBtn(BtnRunSts[0], BtnRunSts[1], BtnRunSts[2], BtnRunSts[3], BtnRunSts[4], BtnRunSts[5])
    # TxbMultiEn_TK = wCtrl.SetTxbMultiLine(TxbMultiEnSts[0], TxbMultiEnSts[1], TxbMultiEnSts[2], TxbMultiEnSts[3], TxbMultiEnSts[4], TxbMultiEnSts[5])

    wCtrl.WindowLoopStart(TK1)
    print('日本語→英語　Quit')
    resetSts()


# *******************************************************************************
def main_enable():
    global Loop_Main
    global t_main
    Loop_Main = True
    print('main enable')

    # *******************************************************************************
def main_disable():
    global Loop_Main
    global t_main
    Loop_Main = False
    print('main disable')

# *******************************************************************************
def thread_task_icon():
    global t_icon
    global icon_
    #-----------------------
    # メニュー
    #-----------------------
    options_map = {'main enable':lambda:main_enable(), 'main disable':lambda:main_disable(), 'help': lambda: displayHelp(True), 'Quit': lambda: quit_system()}
        
    items = []
    for option, callback in options_map.items():
            items.append(MenuItem(option, callback, default=True if option == 'Show' else False))

    menu = Menu(*items)
    #-----------------------
    # アイコン表示
    #-----------------------
    print("icon start")
    image = Image.open("umdrct2.ico")
    # icon=pystray.Icon("name", image, "My System Tray Icon")
    icon_=pystray.Icon("name", image, "My System Tray Icon", menu)
    icon_.run()


# *******************************************************************************
def thread_main():
    global pressCnt
    global ActionSts
    global Loop_Main
    global sys_sts
    global aryKeys

    print('system start')
    displayHelp(False)
    # ActionSts = 4#ヘルプ画面表示からスタート
    # print("%s\r\n%s\r\n%s\r\n%s" % (aryMsg[0], aryMsg[1], aryMsg[2], aryMsg[3]))
    # wCtrl.MsgBox_Inf('help', "%s\r\n%s\r\n%s\r\n%s" % (aryMsg[0], aryMsg[1], aryMsg[2], aryMsg[3]))
    # ActionSts = 6
    while sys_sts:
         if Loop_Main:   
            # =================================================================
            if ActionSts == 0:
                # クリップボードの画像からテキストを抽出
                if kCtrl.CheckPress_CS(aryKeys[0]):
                    pressCnt[0] += 1
                    if pressCnt[0] > 150:
                        if ActionSts == 0: ActionSts = 1
                else: 
                    pressCnt[0] = 0
                # クリップボードの英語を日本語に翻訳
                if kCtrl.CheckPress_CS(aryKeys[1]):
                    pressCnt[1] += 1
                    if pressCnt[1] > 150:
                        if ActionSts == 0: ActionSts = 2
                else: 
                    pressCnt[1] = 0
                
                # 選択画像内のテキストを抽出（ウインドウ）
                if kCtrl.CheckPress_CS(aryKeys[2]):
                    pressCnt[2] += 1
                    if pressCnt[2] > 150:
                        if ActionSts == 0: ActionSts = 3
                else: 
                    pressCnt[2] = 0
                # ヘルプ  
                if kCtrl.CheckPress_CS(aryKeys[3]):
                    pressCnt[3] += 1
                    if pressCnt[3] > 150:
                        if ActionSts == 0: ActionSts = 4
                else: 
                    pressCnt[3] = 0
                    
                # 終了  
                if kCtrl.CheckPress_CS(aryKeys[4]):
                    pressCnt[4] += 1
                    if pressCnt[4] > 150:
                        if ActionSts == 0: ActionSts = 5
                else: 
                    pressCnt[4] = 0
                
                # 日本語→英語変換ツールの起動  
                if kCtrl.CheckPress_CS(aryKeys[5]):
                    pressCnt[5] += 1
                    if pressCnt[5] > 150:
                        if ActionSts == 0: ActionSts = 6
                else: 
                    pressCnt[5] = 0

            # =================================================================
            # クリップボードのイメージからテキストを抽出
            elif ActionSts == 1:
                SerchText_ClipImg()

            # =================================================================
            # クリップボードの英語を日本語に翻訳
            elif ActionSts == 2:
                Translat_ja_to_en()
            
            # =================================================================
            # 選択画像内のテキストを抽出（ウインドウ）
            elif ActionSts == 3:
                SerchText_Window()

            elif ActionSts == 4:
                displayHelp(True)
                # wCtrl.MsgBox_Inf('help', "%s\r\n%s\r\n%s\r\n%s" % (aryMsg[0], aryMsg[1], aryMsg[2], aryMsg[3]))

                # pressCnt = [0, 0, 0, 0]
                # ActionSts = 0
                
            # =================================================================
            # 終了
            elif ActionSts == 5:
                resetSts()
                quit_system()
            
            # =================================================================
            # 日本語→英語翻訳ツール
            elif ActionSts == 6:
                Translat_en_to_ja_Win()
                
# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************

t_icon = threading.Thread(target=thread_task_icon)
t_main = threading.Thread(target=thread_main)

t_icon.start()
t_main.start()



