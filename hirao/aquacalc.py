import sys#sysのインポート
from datetime import datetime


args = sys.argv#argsにsysを設定

today = int(args[1])#もろもろの読み込みと初期化
adult = int(args[2])
children = int(args[3])

Adult_price_weekday = 2000
Adult_price_weekend = 2400

children_price_weekday = 1200
children_price_weekend = 1500

sum = 0

day = today%100#日の取得
today = int(today/100)

month = today%100#月の取得
today = int(today/100)

year = today#年の取得

today = datetime(year,month,day)#date型に変換

if today.strftime('%a') == "Sat" or today.strftime('%a') == "Sun":#条件判定
    sum = Adult_price_weekend*adult + children_price_weekend * children
else:
    sum = Adult_price_weekday*adult + children_price_weekday * children

print(sum,end = "")#出力