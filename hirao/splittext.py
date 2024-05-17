import sys#sysのインポート
args = sys.argv#argsにsysを設定

text = args[1]
n = int(args[2])

print_text = text.split()#textの分割
print(print_text[n-1],end = "")