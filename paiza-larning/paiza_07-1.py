# 関数 

# 関数名の制限
# ・1文字目：英語または、「_」(アンダーバー)
# ・2文字目以降：英語の大文字・小文字・数字「_」(アンダーバー)

# 関数の定義は　def 関数名():
# 忘れずに末尾にコロンをつけること！
def seyHello(name):
	print("hello, {}!!".format(name))

print("-------- call seyHello(\"charlie\") --------")
seyHello("charlie")
print()

# 関数の戻り値はreturn で設定できる
def func_square(n):
	return n*n

print("-------- call func_square(9) --------")
n = func_square(9)
print(n)
print()

# 関数のスコープ
# 関数内で宣言された変数(ローカル変数)は、その関数内でのみ利用できる
# 関数の処理が終了した時点でローカル変数は値が消える
def func_set_num(num):
	num = 100
	print("in func_set_num, num = 100")

num = 10
print("-------- call func_set_num(num) --------")
func_set_num(num)
print("after calling, num = {}".format(num)) # 関数内で宣言したnumではなく、グローバル領域で定義したnum = 10 が表示される