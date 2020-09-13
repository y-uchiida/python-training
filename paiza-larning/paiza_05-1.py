# dictをそのままobjectに入れて for in ループすると、keyを値にとってループする
skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}

for key in skills:
	print(key)
print()

# valueでループしたいときは、dict.values() と書く
for value in skills.values():
	print(value)
print()

# なお、keyで繰り返し処理することを明示的に書くこともできる
for key in skills.keys():
	print(key)
print()

# keyとvalue別々に両方、値を取りたい場合は key, value in dict.items()
for k, v in skills.items():
	print(k, v)
print()