import sys#sysのインポート
args = sys.argv#argsにsysを設定

n = int(args[1])#saralyに金額を入力

for i in range(n):
    print("ひつじが" + str(i+1) + "匹")
