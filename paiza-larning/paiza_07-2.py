# 引数のデフォルト値は、関数宣言時に val = default の形で設定する
def func_power(num, power=2):
	return num ** power

print("-------- call func_power(2) --------")
print(func_power(2)) # -> 4
print("-------- call func_power(2, 3) --------")
print(func_power(2, 3)) # -> 8
print()

# 可変長引数
# 引数名にひとつ*をつけると、tupleとして値を受け取る
# 引数名にふたつ*をつけると、dictとして値を受け取る

# リストの例
def func_sum(*num):
	ret = 0
	for i in num:
		ret += i
	return ret

print("-------- call func_sum(1, 1) --------")
print(func_sum(1, 1))
print("-------- call func_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) --------")
print(func_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print()

# 辞書の例
def func_showPrice(**products):
	for name, price in products.items():
		print("{}:\t{}".format(name, price))

print("-------- call(func_showPrice(camera = '100000', lens = '25000', film = '6980')) --------")
func_showPrice(camera = '100000', lens = '25000', film = '6980')
print()

# 渡す値はあくまで変数なので、文字列は渡せないっぽい
# func_showPrice("カメラ" = '100000', "レンズ" = '25000', "フィルム" = '6980') # <-これだとエラーになる

# 可変長引数はその引数の数が不定なので、何番目以降が可変長引数に入るものか分からない
# 分かるようにするには、ふつうの引数よりも後に引数を定義する必要がある
def func_set_va(arg, *v_arg):
	print("arg: {}".format(arg))
	print("v_arg: " + str(v_arg))

print("-------- call func_set_va(1, 2, 3) --------")
func_set_va(1, 2, 3)
print()

# ちなみに…デフォルト付き引数と組み合わせると？？
def func_set_va2(arg1 = 0, arg2 = 0, *v_arg):
	print("arg1: {}".format(arg1))
	print("arg2: {}".format(arg2))
	print("v_arg: " + str(v_arg))

print("-------- call func_set_va2(1, 2) --------")
func_set_va2(1, 2, 3, 4,)
print()
# 引数のデフォルト値は「引数の値が、もしなかったら代理で使う値」なので、
# 可変長引数の前に指定された引数の数だけちゃんと指定しないといけない
