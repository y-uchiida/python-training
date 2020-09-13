# tuple(タプル) の使い方
# 参考URL: https://docs.python.org/ja/3/tutorial/datastructures.html

# tuple は、最初に宣言した内容から変更ができない配列のようなもの
# 他の言語では、類似のデータ構造はないこともある。。。

myhand = ("thumb", "index finger", "middle finger", "ring finger", "little finger")

# 基本はlistと同じなので、for ... in にオブジェクトとして与えれば、順番に値が取れる
print("-------- print fingers in my hand --------")
for finger in myhand:
	print(finger)
print()

# tuple[i] で要素にアクセスできるのも同じ
print(myhand[3] + "\n")

# 要素の内容を変更したり、追加や削除はできない
myhand.append("another finger") # エラーになる