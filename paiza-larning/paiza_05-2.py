# リストの並べ替え（ソート）
# sorted(list) で、昇順並べ替えされた新しいリストを返す
# list.sort()は、引数で与えられたリスト自体のデータを並べ替える

# リストの整列
weapons = ["イージスソード", "ウィンドスピア", "アースブレイカー", "イナズマハンマー"]
print(weapons)

# 組み込み関数sorted() は新しいリストを返す
sorted_weapons = sorted(weapons)
reverse_sorted_weapons = sorted(weapons, reverse=True)

print(sorted_weapons)
print(reverse_sorted_weapons)

# リストのメンバメソッド list.sort() は、自身を並べ替えする
weapons2 = ["4.イージスソード", "1.ウィンドスピア", "3.アースブレイカー", "2.イナズマハンマー"]
weapons2.sort()
print(weapons2)