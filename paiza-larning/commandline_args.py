# コマンドライン引数は、sysモジュールをimportし、argv()関数から受け取ることができる
import sys

argv = sys.argv

# C言語と同じく、argvの配列の0番目にはスクリプトファイル名が入る
print("filename:", argv[0])

# C言語のargcのように、いくつの引数が与えられたかを教えてくれる引数はない
# そのため、len()を使って配列（Pythonでは「リスト」というらしい）の要素数を取得する
for i in range(1, len(argv)):
	# C言語のprintf的な変数展開。
	print("[%d]: %s" % (i, argv[i]))

# さらに調べてみたら、もっとすっきりかけるということが分かった。
# in <オブジェクト> はそのまま sys.argvの返り値のリスト？を取れる
j = 0
for arg in sys.argv:
	# "文字列{}".format() : 文字列の中にある'{}'という部分を、後ろの.format()関数に指定された変数で置き換える
	# 複数の'{}'が埋め込まれている場合は、format()で指定されたものの先頭から順番に置き換えられる
	print("argv[{}]: {}".format(j, arg))
	j += 1