# -*- coding: utf-8 -*-

#*****************************************************************************
#windowをセット
#SetWindow(tkinter, '300', '200')
def SetWindow(point_x, point_y, size_x, size_y, title_ = 'window'):
    import tkinter
    win_tki = tkinter.Tk()
    win_tki.geometry(str(size_x) + 'x' + str(size_y) + "+" + str(point_x) + "+" + str(point_y))
    win_tki.title(title_)
    return win_tki

#*****************************************************************************
#ボタンセット
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
    messagebox.showinfo(title_, mess_)

#*****************************************************************************
def MsgBox_err( title_, mess_):
    from tkinter import messagebox
    res = messagebox.showerror(title=title_, message=mess_)
    
#*****************************************************************************
def MsgBox_yn(title_, mess_):
    from tkinter import messagebox
    MsgBox_ = messagebox.askquestion(title_, mess_)
    return True if MsgBox_ == 'yes' else False 

#================================================================


def test_():
    MsgBox_err('title', 'mess')


if __name__ == "__main__":
    #clsComm = Common.cls_Common()
    import tkinter as tk0
    import tkinter.scrolledtext as st
    import Common

    Win_tk_= SetWindow(tk0, 400, 200, 10, 10)
    Lbl_tk = SetLabel(tk0, 5, 10-5, 'file')
    Txb_tk = SetTxbEntry(tk0, 50, 40, 10, False, 'aaaaaaa')
    Btn_tk = SetBtn(tk0, 5, 350, 10-5,test_, 'read')
    TxbMulti_tk = SetTxbMultiLine(tk0, st, 50, 10, 10, 40, False, 'aaaaaaaaaaaaaaaaaaa')
    tk0.mainloop()
