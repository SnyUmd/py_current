from sklearn import tree
import ImgCtrl as iCtrl
import WindowCtrl as WCtrl
import SysCtrl as SCtrl

isImg = iCtrl.CheckClipBoad_Img()

if isImg:
    Img_ = iCtrl.GetClipImg()
    text_ = iCtrl.GetImgText_Image(Img_)
    SCtrl.TextCopyToClip(text_, True)
    WCtrl.MsgBox_Inf(mess_=text_, title_="")
else:
    WCtrl.MsgBox_err("", "not Image")