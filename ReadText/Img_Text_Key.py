# from sklearn import tree
import ImgCtrl as iCtrl
import WindowCtrl as wCtrl
import SysCtrl as sCtrl
import KeyCtrl as kCtrl

while True:
    print('start')
    if kCtrl.Loop_CheckPress_CS('\\', 0):
        isImage = iCtrl.CheckClipBoad_Img()#クリップボードがイメージであるか判定
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
                    # sCtrl.TextCopyToClip(text_, True)#クリップボードに保存
                else:
                    msg_ = "イメージの中に、テキスト判定できるものがありませんでした"
                
                wCtrl.MsgBox_Inf(mess_=msg_, title_="")#メッセージボックス表示
    else:
        print("time out")
        break








