


def GetTR(text_:str, source_Language:str = 'en', target_Language:str = 'ja'):
    #モジュールの読み込み
    from webbrowser import open

    url = "https://script.google.com/macros/s/AKfycbwZKnRrH2tF4o147NLkId4xilXCabm4lS5o-nbo8QvAW31jsHZ9/exec"
    url += "?text=%s" % text_
    url += "&source=%s"  % source_Language
    url += "&target=%s"  % target_Language
    
    
    #指定したURLのサイトをブラウザで表示
    open(url)


# GetTR('Hello', 'en', 'ja')