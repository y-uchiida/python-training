# 例外の伝播
# メソッド内で発生した例外は、呼び出し元の関数でも例外として持ち上げられる

def raise_error():
	raise Exception("任意に発生させたエラー")

def func_massage():
	raise_error()

try:
	func_massage()

# raise_error()で発生させた例外は、func_massageでも検出される
# 例外は呼出しもとに対して伝播していき、tryブロックなどで検出がされていれば、最終的にはおおもとのブロックまで戻っていく
except Exception as e:
	print(e)