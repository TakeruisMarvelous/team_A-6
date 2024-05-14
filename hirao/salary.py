"""
import sys#sysのインポート
args = sys.argv#argsにsysを設定

salary = int(args[1])#saralyに金額を入力
"""
salary = 6
tax_rate_less_than_a_milion = 10#100万以下の税率
tax_rate_over_than_a_milion = 20#100万より大きい時の税率

allowance = 0#支給額の初期化
tax = 0#税額の初期化

if(salary<=100):
    tax = round(salary * tax_rate_less_than_a_milion / 100)#税額の計算
    allowance = salary - round(tax)#支給額の計算
else:
    salary = salary - 100#給与ー１００万円
    tax = round(100 * tax_rate_less_than_a_milion/100 + salary * tax_rate_over_than_a_milion / 100)#税額の計算
    allowance = salary - tax#支給額の計算

print("支給額:" + str(allowance) + "、" +"税額:" + str(tax),end = "")#支給額と税額の表示


