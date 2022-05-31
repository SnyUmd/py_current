 
import WindowCtrl as wCtrl
import SysCtrl as sCtrl
 
def set():
    try:
        print('クリップボード内の英語テキストを日本語に翻訳')
        isStr = sCtrl.CheckClipBoad_Str()#クリップボードがテキストであるか確認
        if not isStr:#テキストでは無いとき
            wCtrl.MsgBox_err('errer', 'not text')
        else:#イメージだった時、翻訳を実行
            import Translation
            wCtrl.MsgBox_Inf('', 'Webブラウザに翻訳結果を表示します。')
            cStr = sCtrl.getClipBoad_str()
            Translation.GetTR(cStr)
    except:
        print('Error　Translat_ja_to_en')
        print('Error　翻訳')
        wCtrl.MsgBox_err('Error', '翻訳に失敗しました。')
        
    print('Translat ja to en end')
    

set()