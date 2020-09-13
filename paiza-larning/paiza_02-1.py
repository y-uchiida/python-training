import random

# 条件分岐のif 構文は　if elif else の3つ
# if トークンの後、条件式に() は不要。。。代わりに、条件式の後ろには:をつける

rand_num = random.random()
# print()での文字列と数値の結合は、それぞれを, でつなぐことでも可能
print("rand_num is:", rand_num)
if rand_num > 0.5:
	# ブロックはタブ文字または半角スペース4つで表現される
	print("rand_num > 0.5")
elif rand_num > 0.3:
	# else if は "elif" これはなかなか慣れない……
	print ("0.3 < rand_num <= 0.5")
else:
	print ("rand_num <= 0.3")