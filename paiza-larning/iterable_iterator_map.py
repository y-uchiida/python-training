import numpy as np

# イテラブル、イテレータとmap() の使いかた
# 参考URL: https://dot-blog.jp/news/python-iterable-iterator/

# イテラブル(Iterable)とイテレータ(Iterator)

# イテラブル(Iterable): for 文の in に書き込めるオブジェクト... Iterable は「繰り返し可能な」という意味
# 参考URL: https://python.ms/iterable/

# 以下、公式ドキュメントの日本語訳を引用：
# 一度に一つずつ、自分が持つ要素を返すことができるオブジェクトです。iterable の例には、次の型に属するオブジェクトが含まれます
# まず list, str, tuple などの全てのシーケンス型や、また dict, file object などのシーケンスでない型、
# あるいはユーザが __iter__ メソッドもしくはシーケンスの動作をする __getitem__ メソッドを実装した全てのクラスです

for v in [1, 2, 3]:
	print(v) # 1 -> 2 -> 3 と、順番が記憶されているので、listはIterableといえる
print()

# イテレータ(Iterator): list, tuple, set などの集合を表現するオブジェクトを  iter 関数  を使って  コピー したようなもの
# 参考URL: https://python.ms/iterator/

# イテレータは、組み込み関数 next() を通じて、含まれる要素を一つずつ取り出すことができる -> つまり、「次の要素」を記憶しているオブジェクト
# 『イテラブルなオブジェクト』と『イテレータ』の違いは『イテレーションした状態を記憶しておく』ことができること
my_iterator = iter([1, 2, 3, 4])
print("-------- print iterator --------")
print(next(my_iterator)) # -> 1
print(next(my_iterator)) # -> 2
print(next(my_iterator)) # -> 3
print(next(my_iterator)) # -> 4
print()

# 最後まで到達した状態で、next()を呼ばれると例外を発生する
# print(next(my_iterator)) # -> StopIteration

# map(callable, *iterable)
# iterableに入れられた繰り返し可能なオブジェクトの要素それぞれに対して、callableで渡されたオブジェクトの適用結果を、イテレータ(mapオブジェクト)として返す
# 参考URL: https://qiita.com/conf8o/items/0cb02bc504b51af09099


# 返り値をfor xxx in ループのオブジェクトに入れられる　->　返り値はIterableなオブジェクト（っていうかイテレータ）
print("-------- print result of map(np.square, [1, 3, 5, 7, 9]) --------")
for i, v in enumerate( map(np.square, [1, 3, 5, 7, 9]) ):
	print("{}: {}".format(i, v))
print()

# 与えられたリストの各要素を2乗した要素をふくむイテレータ(mapオブジェクト)を返す
num_square = map(np.square, [1, 3, 5, 7, 9])

# そのままだとmapオブジェクトなので、print()で中身を表示はできない
print("return map() is: ", end="")
print(num_square)
print("return type of map(): {}".format(type(num_square))) # type()で見てみる

print()

# listに変換すれば、printで一覧を表示できる
print("print(list(num_square)): -> ", end="")
print(list(num_square))

# ！！！ ここで注意 ！！！
# mapオブジェクトはイテレータであるので、最初の位置には戻れない
# ここでもう一回print()をしてみると、、、すでに末尾に達しているので何も表示されない
print("once more print(list(num_square)): -> ", end="")
print(list(num_square)) # -> []
print()

# mapの処理結果を何度も使いたい場合は、listなどにキャストしておく必要がある
num_square2 = list(map(np.square, [1, 3, 5, 7, 9]))

print("print(num_square2): -> ", end="")
print(list(num_square2))
print("once more print(num_square2): -> ", end="")
print(list(num_square2)) # -> 2回目でもちゃんと結果が出てくる
print()
