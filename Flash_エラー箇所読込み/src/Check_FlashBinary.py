# -*- config: utf-8 -*-

# import tkinter
import tkinter as tk0

# from wcwidth import wcswidth
#import tkinter.scrolledtext as st
import WindowCtrl as WC
import FileCtrl as FC
import BinaryCtrl as BC
# import os
import Common
import time

SelectFilePath = ''
InitDir = ''

cmm = Common.cls_Common()
InitDirName = FC.Get_ScriptDir()
InitDir = FC.Get_ScriptDir()

#*****************************************************************************
# アドレス情報、ファイル情報をログに記入
def SetInf(file_path):
    StartMsg = cmm.GetStartMessage()
    # WC.AddValue_ScrolledText(tk0, Txb_Log_tk, StartMsg)
    WC.AddValue_ScrolledText(Txb_Log_tk, StartMsg)
    WC.AddValue_ScrolledText(Txb_Log_tk, '\n')
    WC.AddValue_ScrolledText(Txb_Log_tk, '\n-----File info-----\n')
    WC.AddValue_ScrolledText(Txb_Log_tk, 'Title : %s\n' % Txb_Title_tk.get())
    WC.AddValue_ScrolledText(Txb_Log_tk, 'File name   : %s\n' % FC.Get_FileName(file_path))
    WC.AddValue_ScrolledText(Txb_Log_tk, 'Num address : %s\n' % Lbl_FileSizeValue_tk['text'])
    WC.AddValue_ScrolledText(Txb_Log_tk, 'Memo\n')
    WC.AddValue_ScrolledText(Txb_Log_tk, '%s\n' % WC.GetValue_ScrolledText(Txb_Memo_tk))
    WC.AddValue_ScrolledText(Txb_Log_tk, '\n')
    

#*****************************************************************************
# selectボタンをクリックでの動作
# ファイル選択ダイアログの表示　選択されたファイルpathをテキストボックスに表示
def click_file_read():
    path = InitDir
    if not (Txb_File_tk.get() == ""):
        path = FC.Get_DirName(Txb_File_tk.get())

    SelectFilePath = FC.FileSelect(path,'Binary file','*.BIN')
    if SelectFilePath == "":
        return
    Txb_File_tk.delete(0, tk0.END)
    Txb_File_tk.insert(tk0.END, SelectFilePath)
    WC.ChangeLabelValue(Lbl_FileNameValue_tk, FC.Get_FileName(SelectFilePath))
    WC.ChangeLabelValue(Lbl_FileSizeValue_tk, hex(BC.GetAddressNum(Txb_File_tk.get())))

#*****************************************************************************
# Checkボタンクリックでの動作
# Binaryチェックを実行
def click_BadB_AllCheck():

    f = Txb_File_tk.get()
    if not FC.FileCheck(f):
        WC.MsgBox_err('エラー', 'ファイルが存在しません。')
        return
    
    
    if not WC.GetValue_ScrolledText(Txb_Log_tk) == '': 
        log_del = not WC.MsgBox_yn('確認', "現在のLogを残しますか？")
        if log_del:
            Txb_Log_tk.delete("1.0","end") 
        else:
            split_word = "**********************************************************"
            WC.AddValue_ScrolledText(Txb_Log_tk, '\n%s\n%s\n\n' % (split_word, split_word))

    t_start = time.process_time()#開始時間をセット
    SetInf(f)
    result_1st = cmm.Checkking(f, cmm.Adr_Start, cmm.Adr_Step, cmm.Adr_End, False, False)
    WC.AddValue_ScrolledText(Txb_Log_tk, result_1st)

    t_end = time.process_time()#終了時間をセット
    time_ = t_end - t_start
    print("Processing time = %ss" % time_)
    WC.AddValue_ScrolledText(Txb_Log_tk, '\n%s' % str(time_))


#*****************************************************************************
# ログの保存ボタンクリックでの動作
# ファイル保存ダイアログを表示
def click_save_log():
    txt_value = WC.GetValue_ScrolledText(Txb_Log_tk)
    # print(txt_value)
    save_file_path = FC.SaveFile_decide('', 'Text file', '.txt')
    # print(save_file_path)

    if not save_file_path == '' and not save_file_path == '.txt':
        create_sts = FC.CreateFile(save_file_path, txt_value)
        if create_sts:
            WC.MsgBox_Inf("書込成功", 'ファイル書込完了')
            print("Successful creation")
        else:
            WC.MsgBox_err("書込失敗", 'ファイル書込失敗')
            print("Creation error")
    else:
        print('Cancellation')

#*****************************************************************************
# デバッグ用ボタン
def click_debug():
    txt = 'test.txt'
    print(txt.find(''))
    # print(WC.GetValue_ScrolledText(Txb_Log_tk))
    # if WC.MsgBox_yn('確認', "Logを削除しますか？"):        
    #     Txb_Log_tk.delete("1.0","end") 

#*****************************************************************************
# def click_BadB_Check():
#     #Txb_Log_tk.insert(tk0.END, Txb_Log_tk.get() + "\n" + 'BatB_Check')
#     Txb_Log_tk.insert(tk0.END, "\n" + 'BatB_Check')
#     print('BatB_Check')

#*****************************************************************************
# def click_BatB_MarkCheck():
#     Txb_Log_tk.insert(tk0.END, "\n" + 'BatB_MarkCheck')
#     print('BatB_MarkCheck')

#*****************************************************************************
# def CheckBadBlocks(file_path):
#     if not FC.FileCheck(file_path):
#         print('no file')
#         return False

#     check_value = BC.Get_BinValue_All(file_path)


#*****************************************************************************
#*****************************************************************************
#*****************************************************************************
#*****************************************************************************
# cmm = Common.cls_Common(tk0)
# InitDirName = FC.Get_ScriptDir()
# InitDir = FC.Get_ScriptDir()


# ↓↓■■■■■■■プログラムスタート■■■■■■■■↓↓

# ウインドウ作成
Win_tk_= WC.SetWindow(      cmm.windowSts[0], 
                            cmm.windowSts[1],
                            cmm.windowSts[2], 
                            cmm.windowSts[3], 
                            cmm.windowSts[4])

#------------ステージ0-------------ファイル読込み部
Lbl_tk = WC.SetLabel(       cmm.LBL_File_Sts[2], 
                            cmm.LBL_File_Sts[3], 
                            cmm.LBL_File_Sts[4])

Txb_File_tk = WC.SetTxbEntry(    cmm.TXB_FilePath_Sts[0], 
                            cmm.TXB_FilePath_Sts[1],
                            cmm.TXB_FilePath_Sts[2], 
                            cmm.TXB_FilePath_Sts[3], 
                            cmm.TXB_FilePath_Sts[5], 
                            cmm.TXB_FilePath_Sts[4])

Btn_tk = WC.SetBtn(         cmm.Btn_FileRead_Sts[0], 
                            cmm.Btn_FileRead_Sts[1], 
                            cmm.Btn_FileRead_Sts[2],
                            cmm.Btn_FileRead_Sts[3], 
                            click_file_read,  
                            cmm.Btn_FileRead_Sts[4])

#------------ステージ1-------------ファイルインフォメーション部
Frm_Info_tk = WC.SetFream(      cmm.Frm_Info_tk[0], 
                                cmm.Frm_Info_tk[1], 
                                cmm.Frm_Info_tk[2], 
                                cmm.Frm_Info_tk[3])

Lbl_Title_tk = WC.SetLabel(     cmm.Lbl_Title_tk[2],
                                cmm.Lbl_Title_tk[3],
                                cmm.Lbl_Title_tk[4])

Txb_Title_tk = WC.SetTxbEntry(  cmm.Txb_Title_tk[0], 
                                cmm.Txb_Title_tk[1],
                                cmm.Txb_Title_tk[2], 
                                cmm.Txb_Title_tk[3], 
                                cmm.Txb_Title_tk[5], 
                                cmm.Txb_Title_tk[4])

Lbl_FileName_tk = WC.SetLabel(      cmm.Lbl_FileName_tk[2],
                                    cmm.Lbl_FileName_tk[3],
                                    cmm.Lbl_FileName_tk[4])

Lbl_FileNameValue_tk = WC.SetLabel( cmm.Lbl_FileNameValue_tk[2],
                                    cmm.Lbl_FileNameValue_tk[3],
                                    cmm.Lbl_FileNameValue_tk[4])
                                
Lbl_FileSize_tk = WC.SetLabel(      cmm.Lbl_FileSize_tk[2],
                                    cmm.Lbl_FileSize_tk[3],
                                    cmm.Lbl_FileSize_tk[4])

Lbl_FileSizeValue_tk = WC.SetLabel( cmm.Lbl_FileSizeValue_tk[2],
                                    cmm.Lbl_FileSizeValue_tk[3],
                                    cmm.Lbl_FileSizeValue_tk[4])

Lbl_FileSize_tk = WC.SetLabel(      cmm.Lbl_Memo_tk[2],
                                    cmm.Lbl_Memo_tk[3],
                                    cmm.Lbl_Memo_tk[4])

Txb_Memo_tk = WC.SetTxbMultiLine(    cmm.Txb_Memo_tk[0], 
                                    cmm.Txb_Memo_tk[1], 
                                    cmm.Txb_Memo_tk[2],
                                    cmm.Txb_Memo_tk[3], 
                                    cmm.Txb_Memo_tk[5], 
                                    cmm.Txb_Memo_tk[4])

#------------ステージ2-------------実行ボタン
Btn_tk_BatB_AllCheck = WC.SetBtn(   cmm.Btn_BatB_Sts[0], 
                                    cmm.Btn_BatB_Sts[1], 
                                    cmm.Btn_BatB_Sts[2],
                                    cmm.Btn_BatB_Sts[3], 
                                    click_BadB_AllCheck, 
                                    cmm.Btn_BatB_Sts[4])

#------------ステージ3-------------ログ部
Txb_Log_tk = WC.SetTxbMultiLine(    cmm.Txb_Log_Sts[0], 
                                    cmm.Txb_Log_Sts[1], 
                                    cmm.Txb_Log_Sts[2],
                                    cmm.Txb_Log_Sts[3], 
                                    cmm.Txb_Log_Sts[5], 
                                    cmm.Txb_Log_Sts[4])

Btn_tk_Save_Log_tk = WC.SetBtn(     cmm.Btn_SaveLog[0], 
                                    cmm.Btn_SaveLog[1], 
                                    cmm.Btn_SaveLog[2], 
                                    cmm.Btn_SaveLog[3], 
                                    click_save_log, 
                                    cmm.Btn_SaveLog[4])


#------------デバッグ-------------
# Btn_Debug_tk = WC.SetBtn(           cmm.Btn_Debug_Sts[0], 
#                                     cmm.Btn_Debug_Sts[1], 
#                                     cmm.Btn_Debug_Sts[2],
#                                     cmm.Btn_Debug_Sts[3], 
#                                     click_debug, 
#                                     cmm.Btn_Debug_Sts[4])

 
#*****************************************************************************
if __name__ == "__main__":
    #print(InitDir)
    # ウインドウ表示
    tk0.mainloop()
