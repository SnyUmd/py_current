
import cls_Common as CMM
import FileCtrl as FC
import TextCtrl as TC
import WindowCtrl as WC

import tkinter as tk0

cmm = CMM.ClsCommon()
cmm.RunDir = FC.Get_DirName(__file__)

def Click_DirSelect():
    import FileCtrl as FC
    SelectDir = FC.FolderSelect(cmm.RunDir)
    WC.TxbValueSet(txbFolder_tk, SelectDir)



def click_debug():
    txt = 'test.txt'


window_tk = WC.SetWindow(cmm.WinInf[cmm.sizeX], 
                         cmm.WinInf[cmm.sizeY], 
                         cmm.WinInf[cmm.pointX], 
                         cmm.WinInf[cmm.pointY], 
                         cmm.WinInf[cmm.content_])

lblFolder_tk = WC.SetLabel(cmm.LblFolderInf[cmm.pointX], 
                           cmm.LblFolderInf[cmm.pointY], 
                           cmm.LblFolderInf[cmm.content_])

txbFolder_tk = WC.SetTxbEntry(cmm.TxbFolderInf[cmm.sizeX], 
                              cmm.TxbFolderInf[cmm.sizeY], 
                              cmm.TxbFolderInf[cmm.pointX], 
                              cmm.TxbFolderInf[cmm.pointY], 
                              cmm.TxbFolderInf[cmm.content_])

btnFolder_tk = WC.SetBtn(cmm.BtnFolderInf[cmm.sizeX], 
                         cmm.BtnFolderInf[cmm.sizeY], 
                         cmm.BtnFolderInf[cmm.pointX], 
                         cmm.BtnFolderInf[cmm.pointY], 
                         Click_DirSelect,
                         cmm.BtnFolderInf[cmm.content_])




#------------デバッグ-------------
Btn_Debug_tk = WC.SetBtn(cmm.BtnDebugInf[cmm.sizeX], 
                         cmm.BtnDebugInf[cmm.sizeY], 
                         cmm.BtnDebugInf[cmm.pointX], 
                         cmm.BtnDebugInf[cmm.pointY], 
                         click_debug,
                         cmm.BtnDebugInf[cmm.content_])


#*****************************************************************************
#*****************************************************************************
if __name__ == "__main__":
    tk0.mainloop()