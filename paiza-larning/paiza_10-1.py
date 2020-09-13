# 例外処理
# 参考: Pythonの基本的なエラー一覧とその原因の確認方法
# https://note.nkmk.me/python-error-message/

# 参考: 組み込み例外(python3 公式ドキュメント)
# https://docs.python.org/ja/3/library/exceptions.htm#

# スタックトレースを扱うために、tracebackをインポート
import traceback

# 標準エラーにwriteするために、sysをインポート
import sys

# エラー処理の方法としてtry ~ except 文がある
try:
	print("this is error scanning block")
	items = []
	print(items[100]) # 存在しないインデックスへのアクセス = IndexErrorが発生

# IndexErrorが発生したときの処理ブロック
except IndexError as error_msg: # エラーの内容をerror_msgに格納している
	print("インデックスの値が不正です")
	
	sys.stderr.write("\n")
	sys.stderr.write("-------- detected IndexError!!! --------\n")
	sys.stderr.write("type(error_msg): {}\n".format(type(error_msg))) # classとして例外が定義されているのか～
	sys.stderr.write(str(error_msg) + "\n")
	sys.stderr.write(traceback.format_exc() + "\n") # 標準エラー出力にスタックトレースの内容を出力

# Exception クラスは、すべての例外の親になっているクラス。
# 例外の候補の最後に記述しておくと、対応漏れがなくなる
except Exception as error_msg:
	print("予期せぬ例外を検出しました")

finally:
	print("error scan end")


# raise Exception("message") で例外を発生させる

a = 1
b = 2

try:
	# tryブロックの中でraise() を使うと、例外を任意に発生させることができる
	if (a < b):
		raise Exception("Error!: bがaより大きいのはダメ")

except Exception as e:
	sys.stderr.write("{}\n".format(str(e)))

finally:
	print("exception check end.")