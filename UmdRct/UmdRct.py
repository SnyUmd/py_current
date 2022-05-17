# from sklearn import tree
from argparse import Action
import ImgCtrl as iCtrl
import WindowCtrl as wCtrl
import SysCtrl as sCtrl
import KeyCtrl as kCtrl

ActionSts = 0
pressCnt = [0, 0, 0]



# *******************************************************************************
def ClickFile():
    wCtrl.ClickFileRead(TxbFileTK,'Image file','*.jpg *.Png *.png *.ico')

# *******************************************************************************
def ClickTextRead():
    text_ = iCtrl.GetImgText_File(TxbFileTK.get())
    sCtrl.TextCopyToClip(text_, True, str_message="抽出したテキストを、クリップボードにコピーしました。\n\n\n %s" % text_)
    # WCtrl.MsgBox_Inf(mess_=text_, title_="")




print('start')
while True:
    if ActionSts == 0:
        if kCtrl.CheckPress_CS("["):
            pressCnt[0] += 1
            if pressCnt[0] > 150:
                if ActionSts == 0: ActionSts = 1
        else: 
            pressCnt[0] = 0

        if kCtrl.CheckPress_CS("\\"):
            pressCnt[1] += 1
            if pressCnt[1] > 150:
                if ActionSts == 0: ActionSts = 2
        else: 
            pressCnt[1] = 0
        
        if kCtrl.CheckPress_CS("]"):
            pressCnt[2] += 1
            if pressCnt[2] > 150:
                if ActionSts == 0: ActionSts = 3
        else: 
            pressCnt[2] = 0


    elif ActionSts == 1:
        isImage = sCtrl.CheckClipBoad_Img()#クリップボードがイメージであるか判定
        print(isImage)
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
        print('1 End')
        pressCnt = [0, 0, 0]
        ActionSts = 0


    elif ActionSts == 2:
        isStr = sCtrl.CheckClipBoad_Str()#クリップボードがテキストであるか確認
        print(isStr)
        if not isStr:#テキストでは無いとき
            wCtrl.MsgBox_err('errer', 'not text')
        else:#イメージだった時、翻訳を実行
            import Translation
            wCtrl.MsgBox_Inf('', 'Webブラウザに翻訳結果を表示します。')
            cStr = sCtrl.getClipBoad_str()
            Translation.GetTR(cStr)
        print('2 End')
        pressCnt = [0, 0, 0]
        ActionSts = 0
    

    elif ActionSts == 3:
        import tkinter as tk0
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

        wCtrl.WindowLoopStart(tk0)
        print('3 End')
        pressCnt = [0, 0, 0]
        ActionSts = 0








