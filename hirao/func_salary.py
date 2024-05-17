import sys#sysのインポート
args = sys.argv#argsにsysを設定


from decimal import Decimal, ROUND_HALF_UP

tax_rate_less_than_a_milion = 0.1#100万以下の税率
tax_rate_over_than_a_milion = 0.2#100万より大きい時の税率

allowance = 0#支給額の初期化
tax = 0#税額の初期化
salary = 10000

def calc_salary(salary):
    if(salary<=1000000):
        tax = salary * tax_rate_less_than_a_milion#税額の計算
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        allowance = salary - tax#支給額の計算
    else:
        salary = salary - 1000000#給与ー１００万円
        tax =  1000000* tax_rate_less_than_a_milion + salary * tax_rate_over_than_a_milion#税額の計算
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        allowance = salary + 1000000 - tax#支給額の計算
    return allowance,tax

allowance,tax = calc_salary(salary)

print("支給額:" + str(allowance) + "、" +"税額:" + str(tax),end = "")#支給額と税額の表示


