import pandas as pd
import matplotlib.pyplot as plt

#CSVファイルをUTF-8形式で読み込む
data = pd.read_csv('h04_40.csv',encoding = 'shift_jis')
#dataを出力
data.plot()