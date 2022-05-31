import WindowCtrl as wCtrl
import SysCtrl as sCtrl

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
        print('日本語 → 英語　実行')
        # print(en_txt)

    print('英語変換ツール起動')
    WinSts = [600, 130, 10, 10, "日本語 → 英語"]
    LblFileSts = [10, 10, '日本語']
    TxbMultiJaSts = [WinSts[0] - 20, 50, LblFileSts[0], LblFileSts[1] + 20, True, '']
    BtnRunSts = [WinSts[0] - 20, 30, TxbMultiJaSts[2], TxbMultiJaSts[3] + TxbMultiJaSts[1] + 10, ClickRun, "日本語 → 英語"]
    # TxbMultiEnSts = [WinSts[0] - 20, 50, TxbMultiJaSts[2], BtnRunSts[3] + BtnRunSts[1] + 10, False, '']
    
    Win_TK = wCtrl.SetWindow(WinSts[0], WinSts[1], WinSts[2], WinSts[3], WinSts[4])
    LblFile_TK = wCtrl.SetLabel(LblFileSts[0], LblFileSts[1], LblFileSts[2])
    TxbMultiJa_TK = wCtrl.SetTxbMultiLine(TxbMultiJaSts[0], TxbMultiJaSts[1], TxbMultiJaSts[2], TxbMultiJaSts[3], TxbMultiJaSts[4], TxbMultiJaSts[5])
    BtnRun_TK = wCtrl.SetBtn(BtnRunSts[0], BtnRunSts[1], BtnRunSts[2], BtnRunSts[3], BtnRunSts[4], BtnRunSts[5])

    wCtrl.WindowLoopStart(TK1)
    print('日本語 → 英語　Quit')

Translat_en_to_ja_Win()