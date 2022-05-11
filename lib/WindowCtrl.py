# -*- coding: utf-8 -*-

#*****************************************************************************
#windowをセット
#SetWindow(tkinter, '300', '200')
import tkinter

#*****************************************************************************
def WindowLoopStart(tk_ :tkinter):
    tk_.mainloop()

#*****************************************************************************
def HideWindow_tk(win_tk):
    win_tk.withdraw()

#*****************************************************************************
def CloseWindow_tk(win_tk):
    win_tk.destroy()

#*****************************************************************************
def SetWindow(size_x, size_y, point_x, point_y, title_ = 'window'):
    import tkinter
    win_tki = tkinter.Tk()
    win_tki.geometry(str(size_x) + 'x' + str(size_y) + "+" + str(point_x) + "+" + str(point_y))
    win_tki.title(title_)
    return win_tki

#*****************************************************************************
#ラベルセット
def SetLabel(point_x, point_y, value_ = 'label'):
    import tkinter
    lbl = tkinter.Label(text = value_)
    lbl.place(x = point_x, y = point_y)
    return lbl

def ChangeLabelValue(label_tk, value_):
    label_tk['text'] = value_

#*****************************************************************************
#テキストボックスをセット
#SetTxbEntry(tkinter, 50, 10, 10)
def SetTxbEntry(width_, height_, point_x, point_y, write_sts, value_ = ''):
    import tkinter
    txb = tkinter.Entry()
    txb.place(x=point_x, y=point_y, height=height_, width=width_)
    txb.insert(tkinter.END, value_)

    if not write_sts:
        #txb.configure(state = 'disable')
        txb.bind("<Key>", lambda a: "break")
    return txb

#*****************************************************************************
# 複数行のテキストボックスをセット
def SetTxbMultiLine(width_, height_, point_X, point_y, write_sts, value_ = ''):
    import tkinter
    from tkinter.scrolledtext import ScrolledText
    txb_multi = ScrolledText()
    #txb_multi.insert(tkinter.END,"\n".join([str(x) + '行' for x in range(15)]))
    txb_multi.insert(tkinter.END, value_)
    txb_multi.configure(state='normal')
    #txb_multi.grid(row=2,column=2,columnspan=2)
    txb_multi.place(x = point_X, y = point_y, width=width_,height=height_)
    if not write_sts:
        #txb.configure(state = 'disable')
        txb_multi.bind("<Key>", lambda a: "break")
    return txb_multi

#*****************************************************************************
# ボタンをセット
def SetBtn(width_, height_, point_x, point_y, command_, value = 'Button'):
    import tkinter
    btn = tkinter.Button(text = value ,
                          command = command_)
    btn.place(x = point_x, y = point_y, width=width_, height=height_)
    return btn

#*****************************************************************************
# フレームをセット
def SetFream(width_, height_, point_x, point_y):
    import tkinter
    Frm = tkinter.Frame(pady=5, padx=5, relief=tkinter.SOLID, bd=1, bg="white")#FLAT, RAISED, SUNKEN, GROOVE, RIDGE, SOLID
    Frm.place(x = point_x, y = point_y, width=width_, height=height_)
    return Frm

#*****************************************************************************
# テキストボックスの中身をセット
def TxbValueSet(txb_tk, value_):
    import tkinter
    txb_tk.delete(0, tkinter.END)
    txb_tk.insert(tkinter.END, value_)

#*****************************************************************************
# 複数行テキストボックスの中身を取得
def GetValue_ScrolledText(tk_scrolled_text):
    return tk_scrolled_text.get("1.0", "end-1c")

#*****************************************************************************
# 複数行テキストボックスの中身削除
def DelValue_ScrolledText(tk_scrolled_text):
    return tk_scrolled_text.delete("1.0", "end")

#*****************************************************************************
# 複数行テキストボックスの中身を追加
# def AddValue_ScrolledText(tkinter_, tk_scrolled_text, value_, bl_nl = False):
def AddValue_ScrolledText(tk_scrolled_text, value_, bl_nl = False):
    import tkinter
    result = ''
    if bl_nl:
        result = "\n"
    tk_scrolled_text.insert(tkinter.END, result + value_)

#*****************************************************************************
def MsgBox_Inf(title_, mess_):
    from tkinter import messagebox
    win_ = SetWindow(0, 0, 10, 10)
    messagebox.showinfo(title_, mess_)
    win_.withdraw()#ウインドウを非表示
    win_.destroy()

#*****************************************************************************
def MsgBox_err( title_, mess_):
    from tkinter import messagebox
    win_ = SetWindow(0, 0, 10, 10)
    messagebox.showerror(title=title_, message=mess_)
    win_.withdraw()#ウインドウを非表示
    # win_.destroy()
    
#*****************************************************************************
def MsgBox_yn(title_, mess_):
    from tkinter import messagebox
    win_ = SetWindow(0, 0, 10, 10)
    MsgBox_ = messagebox.askquestion(title_, mess_)
    win_.withdraw()#ウインドウを非表示
    win_.destroy()

    return True if MsgBox_ == 'yes' else False 

#*****************************************************************************
# ファイルを読み込む
def ClickFileRead(Txb_tk : tkinter.Entry, read_file_sts:str, read_file_extension:str):
    import tkinter as tk0
    import FileCtrl as FCtrl

    print("Click file")
    path = ""
    if not (Txb_tk.get() == ""):
        path = FCtrl.Get_DirName(Txb_tk.get())

    # SelectFilePath = FCtrl.FileSelect(path,'Image file','*.jpg *.Png *.png *.ico')
    SelectFilePath = FCtrl.FileSelect(path, read_file_sts, read_file_extension)
    if SelectFilePath == "":
        return
    Txb_tk.delete(0, tk0.END)
    Txb_tk.insert(tk0.END, SelectFilePath)


#================================================================


def test_():
    MsgBox_Inf('title', 'mess')
    while True:
        a = 1

if __name__ == "__main__":
    test_()
