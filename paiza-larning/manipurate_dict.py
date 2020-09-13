# dict(辞書) の使い方
# 参考URL: https://docs.python.org/ja/3/tutorial/datastructures.html 

# dict は、他の言語でのハッシュとか連想配列、JavaではMapと呼ばれるもの。
# key と value を紐づけてデータを表現する
# {"key1": value1, "key2": value2} のように、{} で囲んで key と value をコロン記号でついにして表現する

score = {"English": 80, "Math": 75, "Science": 100}

# for ... in 構文の対象オブジェクトとして与えると、キー名を取り出すことができる
print("-------- print 3 subjects score of my exam --------")
for i in score:
	print("score[{}]: {}".format(i, score[i]))
print()

# dictに限らずlist や tapple でもそうだが、 print(dict) でオブジェクト全体を出力できる
print(score)

# 個別の値にはdict["key"] の形式でアクセスできる
# 要素の追加をしたい場合にも、 dict["newKey"] = "newValue" と表現する
score["Social"] = 60

# アクセスはできるが、存在しないキーを参照しようとするとエラーになって処理が止まるのであまりよくない
# print(score["Scienc"]) <- 末尾に'e'を付け忘れ
# -> KeyError: 'Scienc' となる

# 存在しないキーに対するアクセスでエラーを出さないために、dict.get(key) を利用するのがよい
print(score.get("Scienc")) # -> None
print(score.get("Science")) # -> 100

print()

# "key" in dict で、そのキーがdict内にあるかを返す
print("score of 'Japanese' exist in dict? -> {}".format("Japanese" in score))
print("score of 'Math' exist in dict? -> {}".format("Math" in score))

