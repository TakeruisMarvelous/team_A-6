import sys#sysのインポート
args = sys.argv#argsにsysを設定

n = int(args[1])

population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
print_tuple =  population[n]
print(print_tuple,end="")