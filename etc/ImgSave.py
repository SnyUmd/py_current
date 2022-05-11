import sys

from tkinter import Image
import KeyCtrl as kCtrl
import FileCtrl as fCtrl
import WindowCtrl as wCtrl
import ImgCtrl as iCtrl

import pystray
from pystray import Icon, Menu, MenuItem
from PIL import Image

import threading
import schedule

icon_ = 0
status_ = True

def thread_quit():
    global icon_
    icon_.stop()
    # quit()

# ************************************************************
def SetMenu():
    result_menu = Menu(
                    MenuItem('Exit', thread_quit),
                )
    return result_menu

# ************************************************************
def SetIcon(img_icon, menu_):
    #-----------------------
    # アイコン
    #-----------------------
    img_ = Image.open(img_icon)
    result_icon = pystray.Icon('name', img_,  "ImgSave", menu_)
    return result_icon

# ************************************************************
def runSchedule():
    global status_
     ## 5秒毎にタスクを実行する。
    schedule.every(1).seconds.do(main)
    ## status が True である間実行する。
    while status_:
        schedule.run_pending()


# ************************************************************
def thread0():
    ## スケジュールの実行
    task_thread = threading.Thread(target = runSchedule)
    task_thread.start()

# ************************************************************
def main():
    global icon_

    if kCtrl.Loop_CheckPress3(0):
        blResult = iCtrl.CheckClipBoad_Img()
        if not blResult:
            wCtrl.MsgBox_err('errer', 'not image')
            print('not image')
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
                
    icon_.run()



mnu = SetMenu()
icon_ = SetIcon('Img2.ico', mnu)
runSchedule()
# icon_.run()