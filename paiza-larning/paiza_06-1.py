# for xxx in で2次元リストを作る

# 0 で初期化したリストを作成する
# for ... in の末尾に:を置かない場合、 forの前に書かれた処理を実行する
# range(i) は、0からi未満の整数を持つリストを返すので、forの前に書かれた処理をi回繰り返すことができる
# このような記法を、Pythonではリスト内方表記と呼ぶ
# 参考URL: https://note.nkmk.me/python-list-comprehension/
numbers = [0 for i in range(10)]
print(numbers)
print()

# 2n+1の等比数列をのリストを作成する
geometric_progression = [2*n+1 for n in range(10)]
print("-------- print 2n+1 geometric progression --------")
print(geometric_progression)
print()

# 2次元配列を生成する
# for xxx in を配列に入れ子にする
# [[for j in range(m)] for i in range(n)]
# 処理が右から進むのでわかりづらいが…
# 外側のiのforループで、配列の中に配列をn個作る
# iのforループで作られた配列の中に、jのforループの処理結果が格納される

# 8*8のオセロの盤面を作る想定
othello_board = [[0 for j in range(8)] for i in range(8)]
print()

# ドット絵を表示する
enemy_img = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]

print("-------- print enemy_image --------")
for line in enemy_img:
	for dot in line:
		if dot:
			print("#", end="")
		else:
			print(" ", end="")
	print()

print()


# enumrate() 関数：リストやタプルなどのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる
# 参考URL: https://note.nkmk.me/python-enumerate-start/

landmap = [["森" for i in range(20)] for j in range(10)]
landmap[0][0] = "城"
landmap[0][19] = "町"
landmap[9][19] = "町"

# i, line in enumerate(landmap) は
# enumerate() で取り出されたインデックス番号と値をそれぞれiとlineに格納し、
# for ループの中で利用することができる
# dict だと、 dict.items() のメンバメソッドが使えるが、listにはない
# for ループの中でlistのインデックスを使いたい場合、組み込み関数enumerate()を利用する

print("-------- print landmap --------")
for i, line in enumerate(landmap):
	print(str(i) + ":", end="")
	for j, area in enumerate(line): # lineの内部のインデックス番号をjで取り出す
		if (i % 2 == 0 or j % 3 == 0) and area == "森":
			print("＋", end="")
		else:
			print(area, end="")
	print()

# dict と list で利用可能な関数が違うのちょっとわかりづらいな…慣れの問題かな…