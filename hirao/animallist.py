import sys#sysのインポート
args = sys.argv#argsにsysを設定

animals = [ "giraffe", "tiger", "zebra", "elephant", "lion"]
search_animals_index =int(args[1])
insert_animals = args[2]

animals.insert(search_animals_index,str(insert_animals))
animals.remove(len(animals)-1)
animals.sort(key = None,reverse=False)


print(animals,end = "")


