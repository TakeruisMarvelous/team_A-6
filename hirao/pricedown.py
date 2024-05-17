import sys#sysのインポート
args = sys.argv#argsにsysを設定
price_down_class = "果物類"#args[1]
price_down = 100#int(args[2])

def cal(price,down):
    if price-down < 1:
        return 1
    return price-down

item = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

fruits = ["リンゴ","みかん","バナナ"]
alcohol = ["ビール","日本酒"]
noodles = ["ラーメン","うどん"]


if price_down_class == "果物類":
    item["リンゴ"] = cal(item["リンゴ"],price_down)
    item["みかん"] = cal(item["みかん"],price_down)
    item["バナナ"] = cal(item["バナナ"],price_down)
elif price_down_class == "酒類":
    item["ビール"] = cal(item["ビール"],price_down)
    item["日本酒"] = cal(item["日本酒"],price_down)
else:
    item["ラーメン"] = cal(item["ラーメン"],price_down)
    item["パスタ"] = cal(item["パスタ"],price_down)
    item["うどん"] = cal(item["うどん"],price_down)


print(item,end = "")




