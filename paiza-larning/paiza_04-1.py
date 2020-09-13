# 取り込んだデータをリストに格納する

#rstrip() で行末の改行文字を削除する
input_str = input(",(コンマ)で区切って複数の値を入力してください: ").rstrip()
print()

# split("separator") で、セパレータとして指定した文字で釘ってリストに変換できる
input_values = input_str.split(",")

print("入力された値を一つずつ出力")
for v in input_values:
	print(v)