# ラムダ式（無名関数）の使いかた
# Λ ← ラムダ記号。素粒子物理学においてラムダ粒子を表したり、宇宙定数の記号に使われたりする
# 無名関数は、名前を指定せずに実行できるまとまった一連の処理のこと
# 関数の引数に、多くない処理をした結果を与えたい…というような場合に利用される

# 以下引用
# lambda(ラムダ式:無名関数)は『無名関数』と言われるように関数の名前を持たず、そして関数のような役割を持っていますが基本的には式です。
# そのため通常の関数のように機能を使い回したりすることができず1回限りの実行処理となります。
# 参考URL: https://dot-blog.jp/news/python-lambda-basic/


# lambda式 を使って、偶数なら""even", 奇数なら"odd" を返す例
# ラムダ式では複数行にまたがる文を使うことはできないが、if文に相当する三項演算子は使用可能
even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"
print("print(even_or_odd(3): {})".format(even_or_odd(1))) # -> "odd"
print("print(even_or_odd(2): {})".format(even_or_odd(2))) # -> "even"
print("print(even_or_odd(5*3+2): {})".format(even_or_odd(5*3+2))) # -> "odd"
print()

# Pythonのコーディング規約PEP8 においては、上記の例 のようにラムダ式に名前をつけるのは非推奨
# 名前を付けて繰り返し呼び出す必要のあるものは、むしろdefを使ってユーザー関数を定義すべき

# lambda式で、値を2乗した結果をmap関数に渡す
map_square = map(lambda x: x**2, [1, 2, 4, 8, 16, 32])

print(list(map_square))