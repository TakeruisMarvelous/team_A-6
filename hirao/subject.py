import sys#sysのインポート
args = sys.argv#argsにsysを設定

math = int(args[1])
japanese = int(args[2])
english = int(args[3])

if math < 50 or japanese < 50 or english <50:
    print("不合格",end= "")
else:
    if math + japanese + english >= 220:
        print("合格",end = "")
    else:
        if math>=70 and japanese >= 70 and english >= 70:
            print("合格",end = "")
        else:
            print("不合格",end= "")
        
    

        