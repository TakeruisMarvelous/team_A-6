import sys#sysのインポート
args = sys.argv#argsにsysを設定

input1 = args[1]
input2 = args[2]
input3 = args[3]

input1 = int(input1)
input2 = int(input2)
input3 = int(input3)
calc = input1+input2+input3
print(calc,end = "")#3つの数字の計算
