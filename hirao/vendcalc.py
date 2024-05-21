import math
item = {"お茶":110,"コーヒー":100,"ソーダ":160,"コーンポタージュ":130}



def print_items():
    for name,price in item.items():#購入できる商品の一覧表示
        print(name + ":" + str(price) + "円")
    return

def check_amount (amount):
    
    judge = False
    while judge == False:
        if amount > 10000:#処理概要3
            print("10.000円を超える金額は投入できません。再度金額を入力してください") 
            amount = int(input()) 
            check_amount (amount)
        elif amount < min(item.values()):#処理概要4
            print(str(amount)+"円では購入できる商品がありません。再度投入金額を入力してください")
            amount = int(input())
            check_amount (amount)
        elif amount%10 != 0:#処理概要5
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
            amount = int(input())
            check_amount (amount)
        else:
            judge = True
    return amount

def check_goods(goods):#cancel確認
    if goods =="cancel":
        return False
    return True

def check_change(amount):#残金の確認
    if amount < min(item.values()):
        print("もう購入できません")
        return False
    return True

def select_goods(amount):#処理概要6
    if check_change(amount) == False:#残金の確認
        return amount
    
    print("何を購入しますか(商品名/cancel)")
    print_items()
    goods = str(input())
    judge = check_goods(goods)
    if judge ==False:
        return amount
    if  judge == True and check_change(amount) == True:
        print(amount-item[goods])
        amount = amount-item[goods]
        print("残金:"+str(amount))
        print("続けて購入しますか？(Y/N)")
        yes_or_no = str(input())
        if yes_or_no == "Y":
            amount = select_goods(amount)
    
    return amount

def calc_sauce(amount):
    sauce = {#それぞれの硬貨を数えて辞書型に保持
        "５０００円札" : 0,
        "１０００円札" : 0,
        "５００円玉" : 0,
        "１００円玉" : 0,
        "５０円玉" :0,
        "１０円玉":0
    }

    if amount>5000:#それぞれのおつりの計算
        sauce["５０００円札"] = math.floor(amount/5000)
        amount = amount%5000
    if amount> 1000:
        sauce["１０００円札"] = math.floor(amount/1000)
        amount = amount % 1000
    if amount>500:
        sauce["５００円玉"] = math.floor(amount/500)
        amount = amount % 500
    if amount > 100:
        sauce["１００円玉"] = math.floor(amount/100)
        amount = amount % 100 
    if amount > 50:
        sauce["５０円玉"] = math.floor(amount/50)
        amount = amount % 50
    if amount >10:
        sauce["１０円玉"] = math.floor(amount/10)
        amount = amount % 10
    
    for name in sauce.keys():#０枚でないものだけ表示
        if sauce[name] != 0:
            print(name +":" + str(sauce[name]) + "枚")
    
    return

def sauce(amount):
    print("おつり")
    if amount==0:
        print(0)
    else:
        calc_sauce(amount)
    return

print_items()
print("投入金額を入力")#処理概要１
amount = int(input())
check_amount(amount) 
amount = select_goods(amount)#処理概要6
sauce(amount)#処理概要6-3

