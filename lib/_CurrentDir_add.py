import  os
import sys

#ライブラリディレクトリ追加
# sys.path.append("C:\Users\E324595\Documents\_umd\soft\_py\lib")
# sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append("C:/Users/E324595/Documents/_umd/soft/_py/lib")
# print(os.path.dirname(__file__))

# ライブラリディレクトリを確認
import pprint
import sys
pprint.pprint( sys.path )