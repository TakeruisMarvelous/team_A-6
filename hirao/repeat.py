import sys#sysのインポート
args = sys.argv#argsにsysを設定

number = int(args[1])#saralyに金額を入力

sum = 0


while(sum<100):
    sum += number
    if(sum == 100):
        print("Just 100!",end = "")
        
    elif(sum > 100):
        print("Over!",end = "")
        

