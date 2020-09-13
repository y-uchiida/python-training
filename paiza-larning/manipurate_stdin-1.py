# 標準入力からデータを受け取るには、input()関数を使う
inputs = "string"

# do while 構文が無いようなので、 True させつつ終了条件でbreakする
while True:
	print("入力された内容を標準出力に表示します。キーボードから文字を入力してください")
	print("終了する場合は空文字でEnterを入力してください")
	inputs = input("入力内容(入力無しでEnterは処理終了): ") # input()の引数に文字列を入れると、入力待ち受けの際の入力業に表示される
	if inputs == "":
		break
	print("入力されたキー: {}\n".format(inputs))

print("空文字列を受け取りました。終了します\n")