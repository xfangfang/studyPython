# coding:utf-8
import shelve
import json


# addr = "/Users/FANGs/Documents/项目/各种语言/python/2012.txt"
# f = open(addr)
# q = f.read()
# f.close()
# q = json.loads(q)

db = shelve.open('student.shelve', writeback = True)
for i in db:
    # print db[i]
    for j in db[i]:
        print db[i][j].encode('utf-8'),
    print

db.close()
