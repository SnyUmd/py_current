import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('テキストボックス')

lbl = tkinter.Label(text='数値')
lbl.place(x=30, y=70)

# テキストボックス
txt = tkinter.Entry(width=20)
txt.place(x=90, y=70)
txt.insert(tkinter.END,"1234")

# 表示
root.mainloop()


while(True):
    print("test")
