import sys#sysのインポート
args = sys.argv#argsにsysを設定

start_point = args[1]
end_point = args[2]

distance = {
    "東京" : 0.00,"品川": 6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}

a = distance[start_point]
b = distance[end_point]
print(abs(round((a-b),2)),end = "")