# 変動する複数行のデータが標準入力から入ってくる場合に、1行ずつデータを処理する

import sys

array = []
for i in sys.stdin.readlines():
	print(i.rstrip())
    array.append(int(i.rstrip()))
# print(array)