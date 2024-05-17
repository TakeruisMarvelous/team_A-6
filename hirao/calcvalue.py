import sys#sysのインポート
args = sys.argv#argsにsysを設定

n = int(args[1])
m = int(args[2])
l = int(args[3])
def calcvalue(num):
    if(num%2 == 0):
        print(str(num)+"は偶数")
    else:
        print(str(num)+"は奇数")

calcvalue(n)
calcvalue(m)