# キーワード引数
# 関数呼び出しの際、引数名を指定できる！
def func_calc(num1 = 1, oparator = "+", num2 = 1):
	if oparator == "-":
		return num1 - num2
	elif oparator == "/":
		return num1 / num2
	elif oparator == "%":
		return num1 % num2
	elif oparator == "*":
		return num1 * num2
	elif oparator == "**":
		return num1 ** num2
	else:
		return num1 + num2

# 引数名を指定しないと、順番に設定される
print(func_calc(1, "*", 10)) # -> 1 * 10

# 引数名を指定すれば、その引数に値が代入される！
print(func_calc(num2 = 10, oparator = "/")) # -> 1 / 10

# 可変長引数と組み合わせられるかな…
def func_set_va(*v_arg, arg = 0):
	print("arg: {}".format(arg))
	print("v_arg: {}".format(v_arg))

# ふつうの引数を後に指定しておくと、先に可変長引数の値を取ってくれるようになる
print("-------- func_set_va() --------")
func_set_va()
print("-------- func_set_va(1, 2, 3) --------")
func_set_va(1, 2, 3)
print("-------- func_set_va(1, 2, 3, arg = 100) --------")
func_set_va(1, 2, 3, arg = 100)

# 可変長引数よりも後ろに指定された引数は、引数名を指定して（キーワード引数として）
# 値を渡さないといけなくなるが…
# ちなみに、こういうテクニックをキーワード限定引数とか言うらしい
# あと、さっきから「ふつうの引数」と呼んでいたものは、「位置引数」と名前がつけられている
# 引数を指定した順番（位置）が、関数の中での処理のされ方と結びついているから、ということだろうか…