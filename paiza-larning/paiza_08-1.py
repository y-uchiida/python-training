# クラスの宣言とオブジェクト生成

# class [クラス名]: でクラスを定義できる
# クラス名は慣習的に先頭を大文字にする
class Myclass:
	def func_test(self):
		print("calld func_test()")

# オブジェクトの生成は、[クラス名]()
my_obj = Myclass()

# メンバメソッドの実行は、 [オブジェクト名].[メソッド名]
my_obj.func_test()

# いままでメンバメソッドとか、メンバ変数と書いてきたけど、
# pythonの語法としては「インスタンス変数」とか「インスタンスメソッド」というのが正しいみたい

# pythonのクラスのコンストラクタは def __init__(self, arg1, arg2, ~~~): 
class Student:
	def __init__(self, name, number, weight, tall): # <- 最初の引数にselfを指定するのを忘れずに！
		self.name = name
		self.number = number
		self.__weight = weight # インスタンス変数名の先頭に「__」をつけると、プライベート変数になる
		self.__tall = tall

	def eat(self, food): # <- ここも、selfを最初に指定するの忘れないように！
		print("{} ate {}".format(self.name, food))
		self.__fat(1)

	def __fat(self, incremantal): # メソッド名の先頭に「__」をつけると、プライベートメソッドになる
		self.__weight += incremantal

	def measure(self):
		print("{} weight is: {}".format(self.name, self.__weight))

student1 = Student("Charlie", 1, 65, 175)
student1.eat("chicken")
student1.measure()