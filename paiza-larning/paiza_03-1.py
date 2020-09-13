# for v in <オブジェクト>: 構文
# 変数v に <オブジェクト>の要素を先頭から順番に代入して処理を行う
# ここでも、構文の末尾にコロンが必要
# 例:文字列が含まれた配列の先頭から順番にprint()する
for ordinal in ["first", "second", "third"]:
	print(ordinal)

# for i in range(n): range(n)は、0からn-1までのn個の整数を要素に持つ配列を生成する関数
# 他の言語でよくある、 for(i=0; i<n; i++) というのと同じような動作をする
for i in range(10):
	print(i)

# while <条件式>: 構文
# 条件式の内容を満たす限り、ブロック内の処理を繰り返す
i = 0
while i < 100:
	if i % 6 == 0:
		print(i, "is multiples of 6.")
	# インクリメントとかデクリメントを、 i++　とか i-- って書けないっぽい…？
	# += は使える
	i += 1