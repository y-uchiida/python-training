# list の使い方
# 参考URL : http://www.tohoho-web.com/python/list.html
# 参考URL2: https://docs.python.org/ja/3/tutorial/datastructures.html 

# リストは、他の言語でいうところの配列みたいなもの
# [] の中に、各要素をコンマ区切りで定義する
my_list = [0, 2, 4, 8, 16, 32, 64]

# list[0] のように、添え字で要素を指定できる
# 変数内容の変更も可能
my_list[0] = 1

# for ... in 構文に、オブジェクトと渡して各要素に対して処理を実行できる

print("-------- print power of 2 --------")
for i in my_list:
	print(i)

# list.append(v) で、リストの末尾に要素を追加できる
my_list.append(128)

# list.insert(i, v) で、 list[i] の位置に要素を挿入し、それ以降の要素の添え字を一つずらして格納する
alphabets = ["a", "b", "d", "e", "f"]
alphabets.insert(2, "c")

#list.extend([]) で、listの末尾に引数で与えられたリストを追加する
alphabets.extend(["g", "h", "i", "j"])

print("\n-------- print alphabets from a to j --------")
for char in alphabets:
	print(char)

# list.copy() はリストの複製(shallow copy)を返す
alphabets2 = alphabets.copy()

# list.reverse() はリストを逆順にする。in place方式なので、list自体の内容が変わる
alphabets2.reverse()

# list.pop(i) は、指定の添え字の要素を削除して、その値を返す。
# 他の言語と同じく、スタックのデータ処理に利用できる
print("\nlast elmemnt of alphabets2: {}".format(alphabets2.pop()))

print("\n-------- print alphabets from j to b --------")
for char in alphabets2:
	print(char)

# 添え字で要素を指定して削除する場合は、 del list[i] とする
# リストの関数としてrelが用意されているわけではないので注意
del alphabets2[0]

# delで削除すると、添え字は詰められる
print()
print("after del alphabets2[0]")
print("alphabets2[0] is -> {}".format(alphabets2[0]))