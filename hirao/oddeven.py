import sys#sysのインポート
args = sys.argv#argsにsysを設定

number = int(args[1])

if number %2 == 0 : #偶奇判定
    print("偶数",end = "")
else:
    print("奇数",end = "")