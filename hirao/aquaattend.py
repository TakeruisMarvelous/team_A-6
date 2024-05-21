import sys#sysのインポート
from datetime import datetime
from database import session
from tables import Number_of_Visitors

today = datetime(2024,5,21)
adult = 5
child = 5

def day_check(today):#日にちの被りがあるか確認
    list_day = session.query(Number_of_Visitors).filter_by(entry_date = today).all()
    if list_day != None:
        return False
    return True

def insert_Number_of_Visitors(today,adult_num,childlen_num):
    insert_date = Number_of_Visitors(
        entry_date = today,
        seq = 1,
        adult = adult_num,
        child = childlen_num
    )
    session.add(insert_date)
    session.commit()

def update_Number_of_Visitors(today,adult_num,childlen_num):
    update_date = session.query(Number_of_Visitors).filter_by(entry_date = today).first()
    Number_of_Visitors.seq = Number_of_Visitors.seq+1
    Number_of_Visitors.adult =  Number_of_Visitors.adult + adult_num
    Number_of_Visitors.child = Number_of_Visitors.child + childlen_num
    session.add(update_date)
    session.commit()

if day_check(today) == True:
    print("insert")
    insert_Number_of_Visitors(today,adult,child)
else:
    print("update")
    update_Number_of_Visitors(today,adult,child)