import sys

from tkinter import Image
import KeyCtrl as kCtrl
import FileCtrl as fCtrl
import WindowCtrl as wCtrl
import ImgCtrl as iCtrl

while True:
    if kCtrl.Loop_CheckPress_Ctrl_Shift("\\", 0):
        blResult = iCtrl.CheckClipBoad_Img()
        print(blResult)
        if not blResult:
            wCtrl.MsgBox_err('errer', 'not image')
        else:
            save_dir = fCtrl.FolderSelect('')
            if not save_dir == "":
                if iCtrl.SaveClipImg(save_dir):
                    wCtrl.MsgBox_Inf('completed', 'save completed')
                    print('save completed')
                else:
                    wCtrl.MsgBox_err('errer', 'save errer')
                    print('save errer')
            else:
                wCtrl.MsgBox_Inf('cancel', 'cancel save')
                print('Cancel save')
    else:
        print("time out")
        break
